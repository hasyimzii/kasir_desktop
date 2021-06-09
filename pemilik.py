import wx
import wx.xrc
import wx.grid
import conn
import View
import main

class Pemilik(View.PemilikFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def showToko( self, event ):
            self.subframe = View.PemilikFrame(parent=None)
            self.subframe.Show()
            self.Destroy()

    def createToko( self, event ):
            self.subframe = View.TambahTokoFrame(parent=None)
            self.subframe.Show()
            self.Destroy()

    def showManager( self, event ):
            self.Hide()
            frame=DataManagerFrame(None)
            frame.Show()

    def createManager( self, event ):
            self.Hide()
            frame=TambahManagerFrame(None)
            frame.Show()

    def exit( self, event ):
            event.Skip()

