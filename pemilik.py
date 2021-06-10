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
        self.subframe = DataToko(None)
        self.subframe.Show()
        self.Destroy()

    def createToko( self, event ):
        self.subframe = TambahToko(None)
        self.subframe.Show()
        self.Destroy()

    def showManager( self, event ):
        self.subframe = DataManager(None)
        self.subframe.Show()
        self.Destroy()
    def createManager( self, event ):
        self.subframe = TambahManager(None)
        self.subframe.Show()
        self.Destroy()
    def exit( self, event ):
        self.Destroy()
        import main

class DataToko(View.DataTokoFrame):
    def back( self,event):
        self.subframe = Pemilik(None)
        self.subframe.Show()
        self.Destroy()

class TambahToko(View.TambahTokoFrame):
	def __init__(self, parent):
		super().__init__(parent)
		
	def back( self,event):
		self.subframe = Pemilik(None)
		self.subframe.Show()
		self.Destroy()

	def createToko( self, event ):
		alamat = self.toko_input.GetValue()
		query = f'INSERT INTO toko VALUES("", "{alamat}")'
		curs.execute(query)
		conn.commit()
		wx.MessageBox(f'Berhasil Menambahkan!')
		
class DataManager(View.DataManagerFrame):
    def back( self,event):
        self.subframe = Pemilik(None)
        self.subframe.Show()
        self.Destroy()

class TambahManager(View.TambahManagerFrame):
    def back( self,event):
        self.subframe = Pemilik(None)
        self.subframe.Show()
        self.Destroy()

    def createManager( self, event ): #error id toko gaenek ho :v
            username = self.manager_input1.GetValue()
            password = self.manager_input2.GetValue()
            idToko =self.id_toko.GetValue()
            query = f'INSERT INTO user(username,password,jabatan,idToko) VALUES("{username}", "{password}","{"manager"}","{idToko}")'
            curs.execute(query)
            conn.commit()
            wx.MessageBox(f'Berhasil Menambahkan!')

# app = wx.App()
# frame = Pemilik(None)
# frame.Show()
# app.MainLoop()





