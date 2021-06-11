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
        for a in range (5) :
            self.baris = 0
            for row in hasil:
                self.dataProduk.SetCellValue(self.baris, a, str(row[a]))
                self.baris = self.baris+1
        
    def back( self,event):
        frame = Manager(None)
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
        self.dataKasir.CreateGrid( 5, 3 )
        self.dataKasir.SetColLabelValue( 0, u"ID" )
        self.dataKasir.SetColLabelValue( 1, u"Username" )
        self.dataKasir.SetColLabelValue( 2,u"ID Toko" )
        query = f'SELECT idUser,username,idToko FROM user WHERE (jabatan="kasir")'
        curs.execute(query)
        hasil = curs.fetchall()
        for a in range (3) :
            self.baris = 0
            for row in hasil:
                self.dataKasir.SetCellValue(self.baris, a, str(row[a]))
                self.baris = self.baris+1
                
    def back( self,event):
        frame = Manager(None)
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
        
