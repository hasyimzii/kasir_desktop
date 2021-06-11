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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"#######################################", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Sistem Kasir Toko Elektronik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Carda Bold Italic" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.login_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login_input1.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer1.Add( self.login_input1, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.login_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.login_input2.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer1.Add( self.login_input2, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.Size( 245,-1 ), 0 )
		self.m_button4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer3.Add( self.m_button4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"#######################################", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( bSizer13, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.login )

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,492 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"MENU PEMILIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,170 ) )
		self.m_button22 = wx.Button( self, wx.ID_ANY, u"DATA TOKO", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"TAMBAH TOKO", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"DATA MANAGER", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"TAMBAH MANAGER", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button25, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 191, 23, 23 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button22.Bind( wx.EVT_BUTTON, self.showToko )
		self.m_button23.Bind( wx.EVT_BUTTON, self.createToko )
		self.m_button24.Bind( wx.EVT_BUTTON, self.showManager )
		self.m_button25.Bind( wx.EVT_BUTTON, self.createManager )
		self.m_button51.Bind( wx.EVT_BUTTON, self.exit )

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"DATA TOKO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )

		self.m_staticText1011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		fgSizer29 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataToko = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataToko.CreateGrid( 0, 2 )
		self.dataToko.EnableEditing( True )
		self.dataToko.EnableGridLines( True )
		self.dataToko.EnableDragGridSize( False )
		self.dataToko.SetMargins( 0, 0 )

		# Columns
		self.dataToko.EnableDragColMove( False )
		self.dataToko.EnableDragColSize( True )
		self.dataToko.SetColLabelSize( 30 )
		self.dataToko.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataToko.EnableDragRowSize( True )
		self.dataToko.SetRowLabelSize( 80 )
		self.dataToko.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataToko.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer29.Add( self.dataToko, 0, wx.ALL, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, u"MASUKKAN ID", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText86.Wrap( -1 )

		bSizer41.Add( self.m_staticText86, 0, wx.ALL, 5 )

		self.dataToko_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		bSizer41.Add( self.dataToko_input, 0, wx.ALL, 5 )

		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button48, 0, wx.ALL, 5 )


		fgSizer29.Add( bSizer41, 1, wx.EXPAND, 5 )


		bSizer38.Add( fgSizer29, 0, wx.EXPAND, 5 )

		self.m_button44 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer38.Add( self.m_button44, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button48.Bind( wx.EVT_BUTTON, self.detailToko )
		self.m_button44.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def detailToko( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class DetailTokoFrame
###########################################################################

class DetailTokoFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"DETAIL TOKO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,80 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"ID TOKO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.dtoko_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dtoko_input1, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"ALAMAT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.dtoko_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dtoko_input2, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.Colour( 255, 51, 56 ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 79, 203, 12 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.deleteToko )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def deleteToko( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class TambahTokoFrame
###########################################################################

class TambahTokoFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"TAMBAH TOKO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,30 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.toko_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.toko_input.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.toko_input, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Tambahkan", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 191, 23, 23 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.createToko )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def createToko( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class DataManagerFrame
###########################################################################

class DataManagerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"DATA MANAGER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )

		self.m_staticText1011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		fgSizer29 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataManager = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataManager.CreateGrid( 0, 3 )
		self.dataManager.EnableEditing( True )
		self.dataManager.EnableGridLines( True )
		self.dataManager.EnableDragGridSize( False )
		self.dataManager.SetMargins( 0, 0 )

		# Columns
		self.dataManager.EnableDragColMove( False )
		self.dataManager.EnableDragColSize( True )
		self.dataManager.SetColLabelSize( 30 )
		self.dataManager.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataManager.EnableDragRowSize( True )
		self.dataManager.SetRowLabelSize( 80 )
		self.dataManager.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataManager.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer29.Add( self.dataManager, 0, wx.ALL, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, u"MASUKKAN ID", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText86.Wrap( -1 )

		bSizer41.Add( self.m_staticText86, 0, wx.ALL, 5 )

		self.dataManager_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		bSizer41.Add( self.dataManager_input, 0, wx.ALL, 5 )

		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button48, 0, wx.ALL, 5 )


		fgSizer29.Add( bSizer41, 1, wx.EXPAND, 5 )


		bSizer38.Add( fgSizer29, 0, wx.EXPAND, 5 )

		self.m_button44 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer38.Add( self.m_button44, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button48.Bind( wx.EVT_BUTTON, self.detailManager )
		self.m_button44.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def detailManager( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class DetailManagerFrame
###########################################################################

class DetailManagerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"DETAIL MANAGER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,80 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"ID USER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.dmanager_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dmanager_input1, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"USERNAME", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.dmanager_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dmanager_input2, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u"ALAMAT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		self.m_staticText141.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText141.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.dmanager_input3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dmanager_input3, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.Colour( 255, 51, 56 ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 79, 203, 12 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.deleteManager )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def deleteManager( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class TambahManagerFrame
###########################################################################

class TambahManagerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Tambah Manager", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Carda" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,120 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.manager_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.manager_input1.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.manager_input1, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.manager_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.manager_input2.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.manager_input2, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Id Toko", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.manager_input3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.manager_input3.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.manager_input3, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Tambahkan", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 248, 58, 63 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.createManager )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def createManager( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class ManagerFrame
###########################################################################

class ManagerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,492 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"MENU MANAGER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,170 ) )
		self.m_button22 = wx.Button( self, wx.ID_ANY, u"DATA PRODUK", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"TAMBAH PRODUK", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"DATA KASIR", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"TAMBAH KASIR", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button25, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 191, 23, 23 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button22.Bind( wx.EVT_BUTTON, self.showProduk )
		self.m_button23.Bind( wx.EVT_BUTTON, self.createProduk )
		self.m_button24.Bind( wx.EVT_BUTTON, self.showKasir )
		self.m_button25.Bind( wx.EVT_BUTTON, self.createKasir )
		self.m_button51.Bind( wx.EVT_BUTTON, self.exit )

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"DATA PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )

		self.m_staticText1011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		fgSizer29 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataProduk = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataProduk.CreateGrid( 0, 5 )
		self.dataProduk.EnableEditing( True )
		self.dataProduk.EnableGridLines( True )
		self.dataProduk.EnableDragGridSize( False )
		self.dataProduk.SetMargins( 0, 0 )

		# Columns
		self.dataProduk.EnableDragColMove( False )
		self.dataProduk.EnableDragColSize( True )
		self.dataProduk.SetColLabelSize( 30 )
		self.dataProduk.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataProduk.EnableDragRowSize( True )
		self.dataProduk.SetRowLabelSize( 80 )
		self.dataProduk.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataProduk.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer29.Add( self.dataProduk, 0, wx.ALL, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, u"MASUKKAN ID", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText86.Wrap( -1 )

		bSizer41.Add( self.m_staticText86, 0, wx.ALL, 5 )

		self.dataProduk_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		bSizer41.Add( self.dataProduk_input, 0, wx.ALL, 5 )

		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button48, 0, wx.ALL, 5 )


		fgSizer29.Add( bSizer41, 1, wx.EXPAND, 5 )


		bSizer38.Add( fgSizer29, 0, wx.EXPAND, 5 )

		self.m_button44 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer38.Add( self.m_button44, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button48.Bind( wx.EVT_BUTTON, self.detailProduk )
		self.m_button44.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def detailProduk( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class DetailProdukFrame
###########################################################################

class DetailProdukFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"DETAIL PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,80 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"JENIS PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.dproduk_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dproduk_input1, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"MERK PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.dproduk_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dproduk_input2, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u"HARGA PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		self.m_staticText141.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText141.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.dproduk_input3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dproduk_input3, 0, wx.ALL, 5 )

		self.m_staticText1411 = wx.StaticText( self, wx.ID_ANY, u"STOK PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1411.Wrap( -1 )

		self.m_staticText1411.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1411.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText1411, 0, wx.ALL, 5 )

		self.dproduk_input4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dproduk_input4, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.Colour( 129, 83, 223 ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button52 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		self.m_button52.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button52.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button52.SetBackgroundColour( wx.Colour( 255, 51, 56 ) )

		bSizer5.Add( self.m_button52, 0, wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 79, 203, 12 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.editProduk )
		self.m_button52.Bind( wx.EVT_BUTTON, self.deleteProduk )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def editProduk( self, event ):
		event.Skip()

	def deleteProduk( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class TambahProdukFrame
###########################################################################

class TambahProdukFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"TAMBAH PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,170 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Jenis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.produk_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.produk_input1.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.produk_input1, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Merk Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.produk_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.produk_input2.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.produk_input2, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.produk_input3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.produk_input3.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.produk_input3, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.produk_input4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.produk_input4.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.produk_input4, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Tambahkan", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 191, 23, 23 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.createProduk )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def createProduk( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class DataKasirFrame
###########################################################################

class DataKasirFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"DATA KASIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )

		self.m_staticText1011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		fgSizer29 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataKasir = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataKasir.CreateGrid( 0, 3 )
		self.dataKasir.EnableEditing( True )
		self.dataKasir.EnableGridLines( True )
		self.dataKasir.EnableDragGridSize( False )
		self.dataKasir.SetMargins( 0, 0 )

		# Columns
		self.dataKasir.EnableDragColMove( False )
		self.dataKasir.EnableDragColSize( True )
		self.dataKasir.SetColLabelSize( 30 )
		self.dataKasir.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataKasir.EnableDragRowSize( True )
		self.dataKasir.SetRowLabelSize( 80 )
		self.dataKasir.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataKasir.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer29.Add( self.dataKasir, 0, wx.ALL, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, u"MASUKKAN ID", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText86.Wrap( -1 )

		bSizer41.Add( self.m_staticText86, 0, wx.ALL, 5 )

		self.dataKasir_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		bSizer41.Add( self.dataKasir_input, 0, wx.ALL, 5 )

		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button48, 0, wx.ALL, 5 )


		fgSizer29.Add( bSizer41, 1, wx.EXPAND, 5 )


		bSizer38.Add( fgSizer29, 0, wx.EXPAND, 5 )

		self.m_button44 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer38.Add( self.m_button44, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button48.Bind( wx.EVT_BUTTON, self.detailKasir )
		self.m_button44.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def detailKasir( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class DetailKasirFrame
###########################################################################

class DetailKasirFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"DETAIL KASIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,80 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"ID USER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.dkasir_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dkasir_input1, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"USERNAME", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.dkasir_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dkasir_input2, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u"ALAMAT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		self.m_staticText141.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText141.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.dkasir_input3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.dkasir_input3, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.Colour( 255, 51, 56 ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 79, 203, 12 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.deleteKasir )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def deleteKasir( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class TambahKasirFrame
###########################################################################

class TambahKasirFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Tambah Kasir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Carda" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,120 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.kasir_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kasir_input1.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.kasir_input1, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.kasir_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kasir_input2.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.kasir_input2, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Id Toko", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.kasir_input3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kasir_input3.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.kasir_input3, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Tambahkan", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 248, 58, 63 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.createKasir )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def createKasir( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class KasirFrame
###########################################################################

class KasirFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,492 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"MENU KASIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,170 ) )
		self.m_button22 = wx.Button( self, wx.ID_ANY, u"DATA TRANSAKSI", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"TAMBAH TRANSAKSI", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"LAPORAN PENJUALAN", wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer5.Add( self.m_button24, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 191, 23, 23 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button22.Bind( wx.EVT_BUTTON, self.showTransaksi )
		self.m_button23.Bind( wx.EVT_BUTTON, self.createTransaksi )
		self.m_button24.Bind( wx.EVT_BUTTON, self.showLaporan )
		self.m_button51.Bind( wx.EVT_BUTTON, self.exit )

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"DATA TRANSAKSI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )

		self.m_staticText1011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		fgSizer29 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataTransaksi = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataTransaksi.CreateGrid( 0, 3 )
		self.dataTransaksi.EnableEditing( True )
		self.dataTransaksi.EnableGridLines( True )
		self.dataTransaksi.EnableDragGridSize( False )
		self.dataTransaksi.SetMargins( 0, 0 )

		# Columns
		self.dataTransaksi.EnableDragColMove( False )
		self.dataTransaksi.EnableDragColSize( True )
		self.dataTransaksi.SetColLabelSize( 30 )
		self.dataTransaksi.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataTransaksi.EnableDragRowSize( True )
		self.dataTransaksi.SetRowLabelSize( 80 )
		self.dataTransaksi.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataTransaksi.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer29.Add( self.dataTransaksi, 0, wx.ALL, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, u"MASUKKAN ID", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText86.Wrap( -1 )

		bSizer41.Add( self.m_staticText86, 0, wx.ALL, 5 )

		self.dataTransaksi_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		bSizer41.Add( self.dataTransaksi_input, 0, wx.ALL, 5 )

		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button48, 0, wx.ALL, 5 )


		fgSizer29.Add( bSizer41, 1, wx.EXPAND, 5 )


		bSizer38.Add( fgSizer29, 0, wx.EXPAND, 5 )

		self.m_button44 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer38.Add( self.m_button44, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button48.Bind( wx.EVT_BUTTON, self.detailTransaksi )
		self.m_button44.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def detailTransaksi( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


###########################################################################
## Class DetailTransaksiFrame
###########################################################################

class DetailTransaksiFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"DETAIL TRANSAKSI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )

		self.m_staticText1011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		self.detailTransaksi = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.detailTransaksi.CreateGrid( 0, 4 )
		self.detailTransaksi.EnableEditing( True )
		self.detailTransaksi.EnableGridLines( True )
		self.detailTransaksi.EnableDragGridSize( False )
		self.detailTransaksi.SetMargins( 0, 0 )

		# Columns
		self.detailTransaksi.EnableDragColMove( False )
		self.detailTransaksi.EnableDragColSize( True )
		self.detailTransaksi.SetColLabelSize( 30 )
		self.detailTransaksi.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.detailTransaksi.EnableDragRowSize( True )
		self.detailTransaksi.SetRowLabelSize( 80 )
		self.detailTransaksi.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.detailTransaksi.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer38.Add( self.detailTransaksi, 0, wx.ALL, 5 )

		self.m_button44 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer38.Add( self.m_button44, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button44.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def back( self, event ):
		event.Skip()


###########################################################################
## Class TambahTransaksiFrame
###########################################################################

class TambahTransaksiFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"TAMBAH TRANSAKSI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,200 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"ID PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.transaksi_input1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.transaksi_input1.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.transaksi_input1, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"JUMLAH PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.transaksi_input2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.transaksi_input2.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.transaksi_input2, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button67 = wx.Button( self, wx.ID_ANY, u"Tambahkan", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer5.Add( self.m_button67, 0, wx.ALL, 5 )

		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"TOTAL HARGA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		self.m_staticText121.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText121.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.totalHarga = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.totalHarga.Wrap( -1 )

		self.totalHarga.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.totalHarga.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.totalHarga, 0, wx.ALL, 5 )

		self.m_staticText123 = wx.StaticText( self, wx.ID_ANY, u"TOTAL BAYAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText123.Wrap( -1 )

		self.m_staticText123.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText123.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText123, 0, wx.ALL, 5 )

		self.transaksi_input3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer5.Add( self.transaksi_input3, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button68 = wx.Button( self, wx.ID_ANY, u"Bayar", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer5.Add( self.m_button68, 0, wx.ALL, 5 )

		self.m_staticText124 = wx.StaticText( self, wx.ID_ANY, u"SISA KEMBALIAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText124.Wrap( -1 )

		self.m_staticText124.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText124.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText124, 0, wx.ALL, 5 )

		self.sisaKembalian = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sisaKembalian.Wrap( -1 )

		self.sisaKembalian.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.sisaKembalian.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.sisaKembalian, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 191, 23, 23 ) )

		bSizer5.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button67.Bind( wx.EVT_BUTTON, self.tambahOrder )
		self.m_button68.Bind( wx.EVT_BUTTON, self.bayar )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tambahOrder( self, event ):
		event.Skip()

	def bayar( self, event ):
		event.Skip()

	def back( self, event ):
		event.Skip()


