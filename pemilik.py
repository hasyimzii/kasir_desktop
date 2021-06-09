import wx
import wx.xrc
import wx.grid
import conn
import View

class Pemilik(View.PemilikFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def showToko( self, event ):
            self.subframe = View.DataTokoFrame(parent=None)
            self.subframe.Show()
            self.Destroy()

    def createToko( self, event ):
            self.subframe = View.TambahTokoFrame(parent=None)
            self.subframe.Show()
            self.Destroy()

    def showManager( self, event ):
            self.subframe = View.DataManagerFrame(parent=None)
            self.subframe.Show()
            self.Destroy()
    def createManager( self, event ):#error perlu perbaikan
            self.subframe = View.TambahManagerFrame(parent=None)
            self.subframe.Show()
            self.Destroy()
    def back(self,event):
            self.Hide()
            Frame=PemilikFrame(None)
            Frame.Show()
    def exit( self, event ):
            event.Skip()

app = wx.App()
frame = Pemilik(None)
frame.Show()
app.MainLoop()





