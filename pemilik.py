import sqlite3
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
            self.Hide()
            frame=DataTokoFrame(None)
            frame.Show()

    def createToko( self, event ):
            self.Hide()
            frame=TambahTokoFrame(None)
            frame.Show()

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

