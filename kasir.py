import wx
import wx.xrc
import wx.grid
import View

conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="pbo2_toko")
curs = conn.cursor()

class Kasir(View.KasirFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def showTransaksi(self,event):
        self.Hide()
        frame=DataTransaksi(None)
        frame.Show()

    def createTransaksi(self,event):
        self.Hide()
        frame=TambahTransaksi(None)
        frame.Show()

    def showLaporan(self,event):
        self.Hide()
        #dialog
        
    def exit(self,event):
        event.Skip()

class DataTransaksi(View.DataTokoFrame):
    def back( self,event):
        self.subframe = Pemilik(None)
        self.subframe.Show()
        self.Destroy()

class TambahTransaksi(View.TambahTokoFrame):
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
		

        
