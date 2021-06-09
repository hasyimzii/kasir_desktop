import mysql.connector
import wx
import wx.xrc
import wx.grid
import conn
import View

# connection & cursor database
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="pbo2_toko"
)
curs = conn.cursor()

class Login(View.LoginFrame):
    def __init__(self, parent):
        super().__init__(parent)
    def login(self, event):
        username = input("Username: ")
        password = input("Password: ")
        query = f'SELECT * FROM user WHERE username = "{username}" AND password = "{password}"'
        hasil = curs.execute(query)
        wx.MessageBox(hasil)
        # for row in hasil:
        #     if username and password in row:
        #         # jabatan = 
        # #         if username == "pemilik" 
                    
        # else:
        #     wx.MessageBox(f'Username dan Password Salah')

app = wx.App()
frame = Login(None)
frame.Show()
app.MainLoop()



