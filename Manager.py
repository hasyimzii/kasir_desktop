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
        self.subframe =TambahProduk(None)
        self.subframe.Show()
        self.Destroy()

    def showKasir(self,event):
        self.subframe =DataKasir(None)
        self.subframe.Show()
        self.Destroy()

    def createKasir(self,event):
        self.subframe=TambahKasir(None)
        self.subframe.Show()
        self.Destroy()

    def exit(self,event):
        self.Destroy()
        from main import Login

class DataProduk(View.DataProdukFrame):
    def __init__(self,parent):
        super().__init__(parent)
        query = f'SELECT * FROM produk'
        curs.execute(query)
        hasil = curs.fetchall()
        for a in range (5) :
            b = 0
            for row in hasil:
                self.dataProduk.SetCellValue(b, a, str(row[a]))
                b = b+1
        
    def back( self,event):
        self.subframe = Manager(None)
        self.subframe.Show()
        self.Destroy()        

class TambahProduk(View.TambahProdukFrame):
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
    def __init__(self,parent):
        super().__init__(parent)
        query = f'SELECT idUser,username,idToko FROM user'
        curs.execute(query)
        hasil = curs.fetchall()
        for a in range (3) :
            b = 0
            for row in hasil:
                self.dataKasir.SetCellValue(b, a, str(row[a]))
                b = b+1
                
    def back( self,event):
        self.subframe = Manager(None)
        self.subframe.Show()
        self.Destroy()

class TambahKasir(View.TambahKasirFrame):
    def back( self,event):
        self.subframe = Manager(None)
        self.subframe.Show()
        self.Destroy()
    
    def createKasir( self, event ):
        username = self.kasir_input1.GetValue()
        password = self.kasir_input2.GetValue()
        idToko = self.kasir_input3.GetValue()
        query = f'INSERT INTO user(username,password,jabatan,idToko) VALUES("{username}", "{password}","{"kasir"}","{idToko}")'
        curs.execute(query)
        conn.commit()
        wx.MessageBox(f'Berhasil Menambahkan!')
        
