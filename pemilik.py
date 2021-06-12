import mysql.connector
import wx
import wx.xrc
import wx.grid
import View

conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="pbo2_toko")
curs = conn.cursor()

class Pemilik(View.PemilikFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def showToko( self, event ):
        frame = DataToko(None)
        frame.Show()
        self.Destroy()

    def createToko( self, event ):
        frame = TambahToko(None)
        frame.Show()
        self.Destroy()

    def showManager( self, event ):
        frame = DataManager(None)
        frame.Show()
        self.Destroy()

    def createManager( self, event ):
        frame = TambahManager(None)
        frame.Show()
        self.Destroy()
        
    def exit( self, event ):
        self.Destroy()
        from main import Login
        frame=Login(None)
        frame.Show()

class DataToko(View.DataTokoFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.dataToko.SetColLabelValue( 0, u"ID" )
        self.dataToko.SetColLabelValue( 1, u"Alamat" )
        query = f'SELECT * FROM toko WHERE idToko>=2'
        curs.execute(query)
        hasil = curs.fetchall()
        for baris in hasil:
             self.dataToko.AppendRows(1)
        for a in range (2) :
            baris = 0
            for row in hasil:
                self.dataToko.SetCellValue(baris, a, str(row[a]))
                baris = baris+1
    
    def detailToko( self, event ):
        idToko = self.dataToko_input.GetValue()
        frame = DetailToko(parent=None, id=idToko)
        frame.Show()
        self.Destroy()

    def back( self,event):
        frame = Pemilik(None)
        frame.Show()
        self.Destroy()

class DetailToko(View.DetailTokoFrame):
    def __init__(self, parent, id):
        super().__init__(parent)
        self.idToko = id

        query = f'SELECT * FROM toko WHERE idToko = {self.idToko}'
        curs.execute(query)
        hasil = curs.fetchall()

        self.dtoko_input1.SetValue(str(hasil[0][0]))
        self.dtoko_input2.SetValue(str(hasil[0][1]))
    
    def deleteToko(self, event):
        dlg = wx.MessageDialog(self, 'Hapus Data?', 'Information', style=wx.YES_NO)
        retval = dlg.ShowModal()
        if retval == wx.ID_YES:
            query = f'DELETE FROM toko WHERE idToko = {self.idToko}'
            curs.execute(query)
            conn.commit()
            wx.MessageBox(f'Berhasil Menghapus!')
            frame = DataToko(None)
            frame.Show()
            self.Destroy()
        else :
            pass
    
    def back( self,event):
        frame = DataToko(None)
        frame.Show()
        self.Destroy()

class TambahToko(View.TambahTokoFrame):
	def __init__(self, parent):
		super().__init__(parent)
		
	def back( self,event):
		frame = Pemilik(None)
		frame.Show()
		self.Destroy()

	def createToko( self, event ):
		alamat = self.toko_input.GetValue()
		query = f'INSERT INTO toko VALUES("", "{alamat}")'
		curs.execute(query)
		conn.commit()
		wx.MessageBox(f'Berhasil Menambahkan!')
		frame = Pemilik(None)
		frame.Show()
		self.Destroy()
		
class DataManager(View.DataManagerFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.dataManager.SetColLabelValue( 0, u"ID" )
        self.dataManager.SetColLabelValue( 1, u"Username" )
        self.dataManager.SetColLabelValue( 2, u"IdToko" )
        query = f'SELECT idUser,username,idToko FROM user WHERE (jabatan="manager")'
        curs.execute(query)
        hasil = curs.fetchall()
        for baris in hasil:
             self.dataManager.AppendRows(1)
        for a in range (3) :
            baris = 0
            for row in hasil:
                self.dataManager.SetCellValue(baris, a, str(row[a]))
                baris = baris+1

    def detailManager(self, event):
        idManager = self.dataManager_input.GetValue()
        frame = DetailManager(parent=None, id=idManager)
        frame.Show()
        self.Destroy()

    def back( self,event):
        frame = Pemilik(None)
        frame.Show()
        self.Destroy()

class DetailManager(View.DetailManagerFrame):
    def __init__(self, parent, id):
        super().__init__(parent)
        self.idManager = id

        query = f'SELECT user.idUser, user.username, toko.alamat FROM user INNER JOIN toko ON user.idToko = toko.idToko WHERE user.idUser = {self.idManager}'
        curs.execute(query)
        hasil = curs.fetchall()

        self.dmanager_input1.SetValue(str(hasil[0][0]))
        self.dmanager_input2.SetValue(str(hasil[0][1]))
        self.dmanager_input3.SetValue(str(hasil[0][2]))
    
    def deleteManager(self, event):
        dlg = wx.MessageDialog(self, 'Hapus Data?', 'Information', style=wx.YES_NO)
        retval = dlg.ShowModal()
        if retval == wx.ID_YES:
            query = f'DELETE FROM user WHERE idUser = {self.idManager}'
            curs.execute(query)
            conn.commit()
            wx.MessageBox(f'Berhasil Menghapus!')
            frame = DataManager(None)
            frame.Show()
            self.Destroy()
        else :
            pass
    
    def back( self,event):
        frame = DataManager(None)
        frame.Show()
        self.Destroy()
    
class TambahManager(View.TambahManagerFrame):
    def back( self,event):
        frame = Pemilik(None)
        frame.Show()
        self.Destroy()

    def createManager( self, event ):
            username = self.manager_input1.GetValue()
            password = self.manager_input2.GetValue()
            idT = self.manager_input3.GetValue()
            try:
                idToko = int(idT)
                query = f'INSERT INTO user(username,password,jabatan,idToko) VALUES("{username}", "{password}","{"manager"}","{idToko}")'
                curs.execute(query)
                conn.commit()
                wx.MessageBox(f'Berhasil Menambahkan!')
                frame = Pemilik(None)
                frame.Show()
                self.Destroy()
            except:
                wx.MessageBox(f'Data yang dimasukkan salah')
                self.manager_input3.Clear()
                    
                


