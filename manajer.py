import wx
import wx.xrc
import wx.grid
import conn
import View

class Manager(View.ManagerFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def showProduk(self,event):
        self.Hide()
        frame=DataProdukFrame(None)
        frame.Show()

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
        event.Skip()
        
