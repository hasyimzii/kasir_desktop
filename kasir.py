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
        frame = DataTransaksi(parent=None, idUser=self.idUser)
        frame.Show()
        self.Destroy()

    def createTransaksi(self,event):
        tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        idUser = self.idUser
        query = f'INSERT INTO transaksi VALUES("","{tanggal}","{idUser}")'
        curs.execute(query)
        conn.commit()

        frame = TambahTransaksi(parent=None, idUser=self.idUser)
        frame.Show()
        self.Destroy()

    def showLaporan(self,event):
        query = "SELECT SUM(produk.harga * order_transaksi.jumlahProduk) FROM produk INNER JOIN order_transaksi ON produk.idProduk = order_transaksi.idProduk INNER JOIN transaksi ON order_transaksi.idTransaksi = transaksi.idTransaksi where month(transaksi.tanggal) = month(CURDATE())"
        curs.execute(query)
        bulan = curs.fetchall()

        query2 = "SELECT SUM(produk.harga * order_transaksi.jumlahProduk) FROM produk INNER JOIN order_transaksi ON produk.idProduk = order_transaksi.idProduk INNER JOIN transaksi ON order_transaksi.idTransaksi = transaksi.idTransaksi where year(transaksi.tanggal) = year(CURDATE())"
        curs.execute(query2)
        tahun = curs.fetchall()

        wx.MessageBox(f'Total penjualan bulan ini : {bulan[0][0]} \nTotal penjualan tahun ini : {tahun[0][0]}')

    def exit(self,event):
        self.Destroy()
        from main import Login
        frame=Login(None)
        frame.Show()
        
class DataTransaksi(View.DataTransaksiFrame):
    def __init__(self, parent, idUser):
        super().__init__(parent)
        self.idUser = idUser

        self.dataTransaksi.SetColLabelValue( 0, u"ID" )
        self.dataTransaksi.SetColLabelValue( 1, u"Tanggal" )
        self.dataTransaksi.SetColLabelValue( 2, u"ID User" )
        query = f'SELECT * FROM transaksi'
        curs.execute(query)
        hasil = curs.fetchall()
        for baris in hasil:
             self.dataTransaksi.AppendRows(1)
        for a in range (3) :
            baris = 0
            for row in hasil:
                self.dataTransaksi.SetCellValue(baris, a, str(row[a]))
                baris = baris+1
    
    def detailTransaksi(self, event):
        idTransaksi = self.dataTransaksi_input.GetValue()
        frame = DetailTransaksi(parent=None, idUser=self.idUser, id=idTransaksi)
        frame.Show()
        self.Destroy()
    
    def back( self,event):
        frame = Kasir(parent=None, idUser=self.idUser)
        frame.Show()
        self.Destroy()

class DetailTransaksi(View.DetailTransaksiFrame):
    def __init__(self, parent, idUser, id):
        super().__init__(parent)
        self.idUser = idUser
        self.idTransaksi = id

        self.detailTransaksi.SetColLabelValue( 0, u"ID" )
        self.detailTransaksi.SetColLabelValue( 1, u"ID Transaksi" )
        self.detailTransaksi.SetColLabelValue( 2, u"Produk" )
        self.detailTransaksi.SetColLabelValue( 3, u"Jumlah Produk" )
        
        query = f'SELECT order_transaksi.idOrder, order_transaksi.idTransaksi, produk.merk, order_transaksi.jumlahProduk FROM order_transaksi INNER JOIN produk ON order_transaksi.idProduk = produk.idProduk WHERE order_transaksi.idTransaksi = {self.idTransaksi}'
        curs.execute(query)
        hasil = curs.fetchall()

        for baris in hasil:
             self.detailTransaksi.AppendRows(1)
        for a in range (4) :
            baris = 0
            for row in hasil:
                self.detailTransaksi.SetCellValue(baris, a, str(row[a]))
                baris = baris+1

    def back( self,event):
        frame = DataTransaksi(parent=None, idUser=self.idUser)
        frame.Show()
        self.Destroy()

class TambahTransaksi(View.TambahTransaksiFrame):
    def __init__(self, parent, idUser):
        super().__init__(parent)
        self.idUser = idUser
        self.total = 0

    def back( self,event):
        frame = Kasir(parent=None, idUser=self.idUser)
        frame.Show()
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
