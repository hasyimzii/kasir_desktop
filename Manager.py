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
        self.subframe = DataProduk(None)
        self.subframe.Show()
        self.Destroy()

    def createProduk(self,event):
        self.Hide()
        frame=TambahProdukFrame(None)
        frame.Show()

    def showKasir(self,event):
        self.Hide()
        frame=DataKasirFrame(None)
        frame.Show()

    def createKasir(self,event):
        self.Hide()
        frame=TambahKasirFrame(None)
        frame.Show()

    def exit(self,event):
        self.Destroy()
        from main import Login

class DataProduk(View.DataProdukFrame):
    def back( self,event):
        self.subframe = Manager(None)
        self.subframe.Show()
        self.Destroy()

class TambahProduk(View.TambahProdukFrame):
	def __init__(self, parent):
		super().__init__(parent)
		
	def back( self,event):
		self.subframe = Manager(None)
		self.subframe.Show()
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
    def back( self,event):
        self.subframe = Pemilik(None)
        self.subframe.Show()
        self.Destroy()

class TambahKasir(View.TambahKasirFrame):
    def back( self,event):
        self.subframe = Pemilik(None)
        self.subframe.Show()
        self.Destroy()
        
