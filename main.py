import mysql.connector
import wx
import wx.xrc
import wx.grid
import View

conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="pbo2_toko")
curs = conn.cursor()

class Login(View.LoginFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def login(self, event):
        username = self.login_input1.GetValue()
        password = self.login_input2.GetValue()
        query = f'SELECT * FROM user WHERE username = "{username}" AND password = "{password}"'
        curs.execute(query)
        data = curs.fetchall()
        if data[0][3] == "pemilik":
            from Pemilik import Pemilik
            self.Destroy()
            app = wx.App()
            frame = Pemilik(None)
            frame.Show()
            app.MainLoop()
        elif data[0][3] == "manager":
            from Manager import Manager
            self.Destroy()
            app = wx.App()
            frame = Manager(None)
            frame.Show()
            app.MainLoop()
        elif data[0][3] == "kasir":
            from Kasir import Kasir
            self.Destroy()
            app = wx.App()
            frame = Kasir(parent=None, idUser=data[0][0])
            frame.Show()
            app.MainLoop()
        else:
            wx.MessageBox(f'Username dan Password Salah')



app = wx.App()
frame = Login(None)
frame.Show()
app.MainLoop()



