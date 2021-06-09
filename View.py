# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class LoginFrame
###########################################################################

class LoginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 375,159 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.login_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.login_input1, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.login_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		fgSizer1.Add( self.login_input2, 0, wx.ALL, 5 )

		self.loginBtn = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.loginBtn, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.loginBtn.Bind( wx.EVT_BUTTON, self.login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login( self, event ):
		event.Skip()


###########################################################################
## Class PemilikFrame
###########################################################################

class PemilikFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu", pos = wx.DefaultPosition, size = wx.Size( 338,394 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Data Toko", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Tambah Toko", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Data Manager", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Tambah Manager", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		self.m_button8.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_ERROR, wx.ART_BUTTON ) )
		self.m_button8.SetBitmapMargins( wx.Size( 5,-1 ) )
		self.m_button8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_button8.SetBackgroundColour( wx.Colour( 255, 62, 62 ) )

		fgSizer2.Add( self.m_button8, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.showToko )
		self.m_button3.Bind( wx.EVT_BUTTON, self.createToko )
		self.m_button5.Bind( wx.EVT_BUTTON, self.showManager )
		self.m_button6.Bind( wx.EVT_BUTTON, self.createManager )
		self.m_button8.Bind( wx.EVT_BUTTON, self.exit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def showToko( self, event ):
		event.Skip()

	def createToko( self, event ):
		event.Skip()

	def showManager( self, event ):
		event.Skip()

	def createManager( self, event ):
		event.Skip()

	def exit( self, event ):
		event.Skip()


###########################################################################
## Class DataTokoFrame
###########################################################################

class DataTokoFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Toko", pos = wx.DefaultPosition, size = wx.Size( 514,264 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid6.CreateGrid( 5, 5 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )

		# Columns
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 30 )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelSize( 80 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.m_grid6, 0, wx.ALL, 5 )

		self.m_button50 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button50.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		bSizer1.Add( self.m_button50, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class TambahTokoFrame
###########################################################################

class TambahTokoFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Toko", pos = wx.DefaultPosition, size = wx.Size( 338,118 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Alamat Toko", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.alamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.alamat, 0, wx.ALL, 5 )

		self.m_button56 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button56.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		fgSizer5.Add( self.m_button56, 0, wx.ALL, 5 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button32, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button32.Bind( wx.EVT_BUTTON, self.createToko )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def createToko( self, event ):
		event.Skip()


###########################################################################
## Class DataManagerFrame
###########################################################################

class DataManagerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Manager", pos = wx.DefaultPosition, size = wx.Size( 514,264 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid6.CreateGrid( 5, 5 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )

		# Columns
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 30 )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelSize( 80 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.m_grid6, 0, wx.ALL, 5 )

		self.m_button50 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button50.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		bSizer1.Add( self.m_button50, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class TambahManagerFrame
###########################################################################

class TambahManagerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Manager", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.usernameManager = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer6.Add( self.usernameManager, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.passwordManager = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer6.Add( self.passwordManager, 0, wx.ALL, 5 )

		self.m_button55 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button55.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		fgSizer6.Add( self.m_button55, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Tambah Manager", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button21.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_MENU ) )
		fgSizer6.Add( self.m_button21, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button21.Bind( wx.EVT_BUTTON, self.createManager )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def createManager( self, event ):
		event.Skip()


###########################################################################
## Class ManagerFrame
###########################################################################

class ManagerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu", pos = wx.DefaultPosition, size = wx.Size( 336,394 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Data Produk", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Tambah Produk", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Data Kasir", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Tambah Kasir", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		self.m_button8.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_ERROR, wx.ART_BUTTON ) )
		self.m_button8.SetBitmapMargins( wx.Size( 5,-1 ) )
		self.m_button8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_button8.SetBackgroundColour( wx.Colour( 255, 62, 62 ) )

		fgSizer2.Add( self.m_button8, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.showProduk )
		self.m_button3.Bind( wx.EVT_BUTTON, self.createProduk )
		self.m_button5.Bind( wx.EVT_BUTTON, self.showKasir )
		self.m_button6.Bind( wx.EVT_BUTTON, self.createKasir )
		self.m_button8.Bind( wx.EVT_BUTTON, self.exit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def showProduk( self, event ):
		event.Skip()

	def createProduk( self, event ):
		event.Skip()

	def showKasir( self, event ):
		event.Skip()

	def createKasir( self, event ):
		event.Skip()

	def exit( self, event ):
		event.Skip()


###########################################################################
## Class DataProdukFrame
###########################################################################

class DataProdukFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Produk", pos = wx.DefaultPosition, size = wx.Size( 514,264 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid6.CreateGrid( 5, 5 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )

		# Columns
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 30 )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelSize( 80 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.m_grid6, 0, wx.ALL, 5 )

		self.m_button50 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button50.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		bSizer1.Add( self.m_button50, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class TambahProdukFrame
###########################################################################

class TambahProdukFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Produk", pos = wx.DefaultPosition, size = wx.Size( 347,217 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Kode Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer8.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.kodeBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer8.Add( self.kodeBarang, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer8.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.jumlahBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer8.Add( self.jumlahBarang, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer8.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.hargaBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer8.Add( self.hargaBarang, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Jenis Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer8.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.jenisBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer8.Add( self.jenisBarang, 0, wx.ALL, 5 )

		self.m_button42 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button42.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		fgSizer8.Add( self.m_button42, 0, wx.ALL, 5 )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button27.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_MENU ) )
		fgSizer8.Add( self.m_button27, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class DataKasirFrame
###########################################################################

class DataKasirFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Kasir", pos = wx.DefaultPosition, size = wx.Size( 514,264 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid6.CreateGrid( 5, 5 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )

		# Columns
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 30 )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelSize( 80 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.m_grid6, 0, wx.ALL, 5 )

		self.m_button50 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button50.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		bSizer1.Add( self.m_button50, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class TambahKasirFrame
###########################################################################

class TambahKasirFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Kasir", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.usernameKasir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer6.Add( self.usernameKasir, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.passwordKasir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer6.Add( self.passwordKasir, 0, wx.ALL, 5 )

		self.m_button54 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button54.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		fgSizer6.Add( self.m_button54, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Tambah Kasir", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )

		self.m_button21.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_MENU ) )
		fgSizer6.Add( self.m_button21, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button21.Bind( wx.EVT_BUTTON, self.createKasir )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def createKasir( self, event ):
		event.Skip()


###########################################################################
## Class KasirFrame
###########################################################################

class KasirFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu", pos = wx.DefaultPosition, size = wx.Size( 498,239 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Data Transaksi", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Tambah Transaksi", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Laporan Penjualan", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer2.Add( self.m_button7, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		self.m_button8.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_ERROR, wx.ART_BUTTON ) )
		self.m_button8.SetBitmapMargins( wx.Size( 5,-1 ) )
		self.m_button8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_button8.SetBackgroundColour( wx.Colour( 255, 62, 62 ) )

		fgSizer2.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.showTransaksi )
		self.m_button6.Bind( wx.EVT_BUTTON, self.createTransaksi )
		self.m_button7.Bind( wx.EVT_BUTTON, self.showLaporan )
		self.m_button8.Bind( wx.EVT_BUTTON, self.exit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def showTransaksi( self, event ):
		event.Skip()

	def createTransaksi( self, event ):
		event.Skip()

	def showLaporan( self, event ):
		event.Skip()

	def exit( self, event ):
		event.Skip()


###########################################################################
## Class DataTransaksiFrame
###########################################################################

class DataTransaksiFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Transaksi", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid5 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid5.CreateGrid( 5, 5 )
		self.m_grid5.EnableEditing( True )
		self.m_grid5.EnableGridLines( True )
		self.m_grid5.EnableDragGridSize( False )
		self.m_grid5.SetMargins( 0, 0 )

		# Columns
		self.m_grid5.EnableDragColMove( False )
		self.m_grid5.EnableDragColSize( True )
		self.m_grid5.SetColLabelSize( 30 )
		self.m_grid5.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid5.EnableDragRowSize( True )
		self.m_grid5.SetRowLabelSize( 80 )
		self.m_grid5.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid5.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer5.Add( self.m_grid5, 0, wx.ALL, 5 )

		self.m_button49 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button49.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_TOOLBAR ) )
		bSizer5.Add( self.m_button49, 0, wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class TambahTransaksiFrame
###########################################################################

class TambahTransaksiFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Transaksi", pos = wx.DefaultPosition, size = wx.Size( 411,349 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Kode Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		fgSizer12.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.kodeBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer12.Add( self.kodeBarang, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		fgSizer12.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.jumlahBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer12.Add( self.jumlahBarang, 0, wx.ALL, 5 )


		fgSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button31 = wx.Button( self, wx.ID_ANY, u"Tambahkan", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )

		self.m_button31.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_MENU ) )
		fgSizer12.Add( self.m_button31, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Total Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		fgSizer12.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.total = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer12.Add( self.total, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Total Bayar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer12.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.totalBayar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer12.Add( self.totalBayar, 0, wx.ALL, 5 )


		fgSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button311 = wx.Button( self, wx.ID_ANY, u"Bayar", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )

		self.m_button311.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_MENU ) )
		fgSizer12.Add( self.m_button311, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Sisa Kembalian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer12.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer12.Add( self.m_textCtrl26, 0, wx.ALL, 5 )

		self.m_button43 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button43.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		fgSizer12.Add( self.m_button43, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


