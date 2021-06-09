import sqlite3
import wx
import wx.xrc
import wx.grid
import conn
import View

class Login(View.LoginFrame):
    def __init__(self, parent):
        super().__init__(parent)
    def login(self,event):
        while True:
            username = input("Username: ")
            password = input("Password: ")
            query = f'SELECT*FROM user WHERE username = "{username}" AND password = "{password}"'
            hasil = self.execute(query)
            for row in hasil:
                if username and password in row:
                    #pindah halaman
                    import pemilik
                        
            else:
                wx.MessageBox(f'Username dan Password Salah')

app = wx.App()
frame = Login(None)
frame.Show()
app.MainLoop()



