import sqlite3
import wx
import wx.xrc
import wx.grid
import conn
import View

class Kasir(View.KasirFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def showTransaksi(self,event):
        self.Hide()
        frame=DataTransaksiFrame(None)
        frame.Show()

    def createTransaksi(self,event):
        self.Hide()
        frame=TambahTransaksiFrame(None)
        frame.Show()

    def showLaporan(self,event):
        self.Hide()
        #dialog
    def exit(self,event):
        event.Skip()
        
