import mysql.connector
import wx
import wx.xrc
import wx.grid
import View

conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="pbo2_toko")
curs = conn.cursor()

class Manager(View.ManagerFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def showProduk(self,event):
        frame = DataProduk(None)
        frame.Show()
        self.Destroy()
        
    def createProduk(self,event):
        frame =TambahProduk(None)
        frame.Show()
        self.Destroy()

    def showKasir(self,event):
        frame =DataKasir(None)
        frame.Show()
        self.Destroy()

    def createKasir(self,event):
        frame=TambahKasir(None)
        frame.Show()
        self.Destroy()

    def exit(self,event):
        self.Destroy()
        from main import Login
        frame=Login(None)
        frame.Show()

class DataProduk(View.DataProdukFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.dataProduk.SetColLabelValue( 0, u"ID" )
        self.dataProduk.SetColLabelValue( 1, u"Jenis" )
        self.dataProduk.SetColLabelValue( 2, u"Merk" )
        self.dataProduk.SetColLabelValue( 3, u"Harga" )
        self.dataProduk.SetColLabelValue( 4, u"Stok" )
        query = f'SELECT * FROM produk'
        curs.execute(query)
        hasil = curs.fetchall()
        for baris in hasil:
             self.dataProduk.AppendRows(1)
        for a in range (5) :
            baris = 0
            for row in hasil:
                self.dataProduk.SetCellValue(baris, a, str(row[a]))
                baris = baris+1

    def detailProduk( self, event ):
        idProduk = self.dataProduk_input.GetValue()
        frame = DetailProduk(parent=None, id=idProduk)
        frame.Show()
        self.Destroy()
        
    def back( self,event):
        frame = Manager(None)
        frame.Show()
        self.Destroy()

class DetailProduk(View.DetailProdukFrame):
    def __init__(self, parent, id):
        super().__init__(parent)
        self.idProduk = id

        query = f'SELECT * FROM produk WHERE idProduk = {self.idProduk}'
        curs.execute(query)
        hasil = curs.fetchall()

        self.dproduk_input1.SetValue(str(hasil[0][1]))
        self.dproduk_input2.SetValue(str(hasil[0][2]))
        self.dproduk_input3.SetValue(str(hasil[0][3]))
        self.dproduk_input4.SetValue(str(hasil[0][4]))
    
    def editProduk(self, event):
        jenis = self.dproduk_input1.GetValue()
        merk = self.dproduk_input2.GetValue()
        harga = self.dproduk_input3.GetValue()
        stok = self.dproduk_input4.GetValue()
        query = f'UPDATE produk SET jenis="{jenis}", merk="{merk}", harga="{harga}", stok="{stok}" WHERE idProduk = {self.idProduk}'
        curs.execute(query)
        conn.commit()
        wx.MessageBox(f'Berhasil Mengedit!')
    
    def deleteProduk(self, event):
        dlg = wx.MessageDialog(self, 'Hapus Data?', 'Information', style=wx.YES_NO)
        retval = dlg.ShowModal()
        if retval == wx.ID_YES:
            query = f'DELETE FROM produk WHERE idProduk = {self.idProduk}'
            curs.execute(query)
            conn.commit()
            wx.MessageBox(f'Berhasil Menghapus!')
        else :
            pass
    
    def back( self,event):
        frame = DataProduk(None)
        frame.Show()
        self.Destroy()

class TambahProduk(View.TambahProdukFrame):
    def back( self,event):
        frame = Manager(None)
        frame.Show()
        self.Destroy()
        
    def createProduk( self, event ):
        jenis = self.produk_input1.GetValue()
        merk = self.produk_input2.GetValue()
        harga = self.produk_input3.GetValue()
        stok = self.produk_input4.GetValue()
        query = f'INSERT INTO produk(jenis,merk,harga,stok) VALUES("{jenis}", "{merk}","{harga}","{stok}")'
        curs.execute(query)
        conn.commit()
        wx.MessageBox(f'Berhasil Menambahkan!')
		
class DataKasir(View.DataKasirFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.dataKasir.SetColLabelValue( 0, u"ID" )
        self.dataKasir.SetColLabelValue( 1, u"Username" )
        self.dataKasir.SetColLabelValue( 2,u"ID Toko" )
        query = f'SELECT idUser,username,idToko FROM user WHERE (jabatan="kasir")'
        curs.execute(query)
        hasil = curs.fetchall()
        for baris in hasil:
             self.dataKasir.AppendRows(1)
        for a in range (3) :
            baris = 0
            for row in hasil:
                self.dataKasir.SetCellValue(baris, a, str(row[a]))
                baris = baris+1

    def detailKasir(self, event):
        idKasir = self.dataKasir_input.GetValue()
        frame = DetailKasir(parent=None, id=idKasir)
        frame.Show()
        self.Destroy()
                
    def back( self,event):
        frame = Manager(None)
        frame.Show()
        self.Destroy()

class DetailKasir(View.DetailKasirFrame):
    def __init__(self, parent, id):
        super().__init__(parent)
        self.idKasir = id

        query = f'SELECT user.idUser, user.username, toko.alamat FROM user INNER JOIN toko ON user.idToko = toko.idToko WHERE user.idUser = {self.idKasir}'
        curs.execute(query)
        hasil = curs.fetchall()

        self.dkasir_input1.SetValue(str(hasil[0][0]))
        self.dkasir_input2.SetValue(str(hasil[0][1]))
        self.dkasir_input3.SetValue(str(hasil[0][2]))
    
    def deleteKasir(self, event):
        dlg = wx.MessageDialog(self, 'Hapus Data?', 'Information', style=wx.YES_NO)
        retval = dlg.ShowModal()
        if retval == wx.ID_YES:
            query = f'DELETE FROM user WHERE idUser = {self.idKasir}'
            curs.execute(query)
            conn.commit()
            wx.MessageBox(f'Berhasil Menghapus!')
        else :
            pass
    
    def back( self,event):
        frame = DataKasir(None)
        frame.Show()
        self.Destroy()

class TambahKasir(View.TambahKasirFrame):
    def back( self,event):
        frame = Manager(None)
        frame.Show()
        self.Destroy()
    
    def createKasir( self, event ):
        username = self.kasir_input1.GetValue()
        password = self.kasir_input2.GetValue()
        idToko = self.kasir_input3.GetValue()
        query = f'INSERT INTO user(username,password,jabatan,idToko) VALUES("{username}", "{password}","{"kasir"}","{idToko}")'
        curs.execute(query)
        conn.commit()
        wx.MessageBox(f'Berhasil Menambahkan!')
        
