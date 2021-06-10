import mysql.connector
import wx
import wx.xrc
import wx.grid
import View
from datetime import datetime

conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="pbo2_toko")
curs = conn.cursor()

class Kasir(View.KasirFrame):
    def __init__(self, parent, idUser):
        super().__init__(parent)
        self.idUser = idUser

    def showTransaksi(self,event):
        self.subframe = DataTransaksi(parent=None, idUser=self.idUser)
        self.subframe.Show()
        self.Destroy()

    def createTransaksi(self,event):
        tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        idUser = self.idUser
        query = f'INSERT INTO transaksi VALUES("","{tanggal}","{idUser}")'
        curs.execute(query)
        conn.commit()

        self.subframe = TambahTransaksi(parent=None, idUser=self.idUser)
        self.subframe.Show()
        self.Destroy()

    def showLaporan(self,event):
        self.Hide()
        #dialog

    def exit(self,event):
        self.Destroy()
        from main import Login
        
class DataTransaksi(View.DataTransaksiFrame):
    def __init__(self, parent, idUser):
        super().__init__(parent)
        self.idUser = idUser
    
    def back( self,event):
        self.subframe = Kasir(parent=None, idUser=self.idUser)
        self.subframe.Show()
        self.Destroy()

class TambahTransaksi(View.TambahTransaksiFrame):
    def __init__(self, parent, idUser):
        super().__init__(parent)
        self.idUser = idUser
        self.total = 0

    def back( self,event):
        self.subframe = Kasir(parent=None, idUser=self.idUser)
        self.subframe.Show()
        self.Destroy()

    def tambahOrder( self, event ):
        # get id transaksi
        query = "SELECT idTransaksi FROM transaksi ORDER BY idTransaksi DESC LIMIT 1"
        curs.execute(query)
        idTransaksi = curs.fetchall()

        # add to db
        idProduk = self.transaksi_input1.GetValue()
        jumlahProduk = self.transaksi_input2.GetValue()
        query = f'INSERT INTO order_transaksi(idTransaksi, idProduk, jumlahProduk) VALUES("{idTransaksi[0][0]}", "{idProduk}","{jumlahProduk}")'
        curs.execute(query)
        conn.commit()

        # get sum produk
        query2 = f'SELECT harga FROM produk WHERE idProduk = {idProduk}'
        curs.execute(query2)
        data = curs.fetchall()
        harga = data[0][0]
        
        # set value total harga
        self.total += (int(jumlahProduk) * int(harga))
        self.totalHarga.SetLabel(str(self.total))

    def bayar( self, event ):
        totalHarga = self.total
        totalBayar = self.transaksi_input3.GetValue()
        kembalian = int(totalBayar) - totalHarga
        self.sisaKembalian.SetLabel(str(kembalian))