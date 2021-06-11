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
		self.m_button4.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )

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

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Regristasi Manager", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.m_button5.SetBackgroundColour( wx.Colour( 253, 249, 89 ) )

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

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Regristasi Kasir", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.m_button5.SetBackgroundColour( wx.Colour( 253, 249, 89 ) )

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
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer102 = wx.BoxSizer( wx.VERTICAL )

		bSizer102.SetMinSize( wx.Size( -1,50 ) )
		self.m_staticText371 = wx.StaticText( self, wx.ID_ANY, u"Daftar Pilihan Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )

		self.m_staticText371.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText371.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer102.Add( self.m_staticText371, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer7.Add( bSizer102, 0, wx.EXPAND, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		bSizer7.Add( fgSizer7, 0, wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.tabelkeberuntungan = wx.grid.Grid( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,320 ), 0 )

		# Grid
		self.tabelkeberuntungan.CreateGrid( 0, 10 )
		self.tabelkeberuntungan.EnableEditing( False )
		self.tabelkeberuntungan.EnableGridLines( True )
		self.tabelkeberuntungan.EnableDragGridSize( False )
		self.tabelkeberuntungan.SetMargins( 0, 35 )

		# Columns
		self.tabelkeberuntungan.SetColSize( 0, 80 )
		self.tabelkeberuntungan.SetColSize( 1, 241 )
		self.tabelkeberuntungan.SetColSize( 2, 159 )
		self.tabelkeberuntungan.SetColSize( 3, 159 )
		self.tabelkeberuntungan.SetColSize( 4, 100 )
		self.tabelkeberuntungan.SetColSize( 5, 80 )
		self.tabelkeberuntungan.SetColSize( 6, 112 )
		self.tabelkeberuntungan.SetColSize( 7, 80 )
		self.tabelkeberuntungan.SetColSize( 8, 80 )
		self.tabelkeberuntungan.EnableDragColMove( False )
		self.tabelkeberuntungan.EnableDragColSize( True )
		self.tabelkeberuntungan.SetColLabelSize( 30 )
		self.tabelkeberuntungan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelkeberuntungan.AutoSizeRows()
		self.tabelkeberuntungan.EnableDragRowSize( False )
		self.tabelkeberuntungan.SetRowLabelSize( 80 )
		self.tabelkeberuntungan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelkeberuntungan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelkeberuntungan.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer10.Add( self.tabelkeberuntungan, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 8, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button9 = wx.Button( self.m_panel6, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button9.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer9.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button92 = wx.Button( self.m_panel6, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button92.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button92.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button92.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer9.Add( self.m_button92, 0, wx.ALL, 5 )

		self.m_button91 = wx.Button( self.m_panel6, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button91.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button91.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button91.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer9.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		fgSizer9.Add( self.m_staticText48, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		fgSizer9.Add( self.m_staticText49, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer9.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self.m_panel6, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button5.SetBackgroundColour( wx.Colour( 215, 0, 0 ) )

		fgSizer9.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( fgSizer9, 0, wx.EXPAND, 5 )


		gbSizer1.Add( bSizer10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		self.m_panel6.SetSizer( gbSizer1 )
		self.m_panel6.Layout()
		gbSizer1.Fit( self.m_panel6 )
		bSizer7.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabelkeberuntungan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelkeberuntunganOnGridCmdSelectCell )
		self.m_button9.Bind( wx.EVT_BUTTON, self.button_tambah )
		self.m_button92.Bind( wx.EVT_BUTTON, self.button_edit )
		self.m_button91.Bind( wx.EVT_BUTTON, self.refresh )
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_keluar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
		event.Skip()

	def button_tambah( self, event ):
		event.Skip()

	def button_edit( self, event ):
		event.Skip()

	def refresh( self, event ):
		event.Skip()

	def button_keluar( self, event ):
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

		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"TOTAL BIAYA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		self.m_staticText121.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText121.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.m_staticText122 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText122.Wrap( -1 )

		self.m_staticText122.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText122.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText122, 0, wx.ALL, 5 )

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

		self.m_staticText125 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText125.Wrap( -1 )

		self.m_staticText125.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText125.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText125, 0, wx.ALL, 5 )


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
		self.transaksi_input3.Bind( wx.EVT_TEXT, self.transaksi_input3 )
		self.m_button68.Bind( wx.EVT_BUTTON, self.bayar )
		self.m_button51.Bind( wx.EVT_BUTTON, self.back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tambahOrder( self, event ):
		event.Skip()

	def transaksi_input3( self, event ):
		event.Skip()

	def bayar( self, event ):
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
		self.dataKasir.CreateGrid( 5, 5 )
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
		self.dataManager.CreateGrid( 5, 5 )
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
		self.dataToko.CreateGrid( 5, 5 )
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
		self.dataProduk.CreateGrid( 5, 5 )
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
		self.dataTransaksi.CreateGrid( 5, 5 )
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
		self.dataTransaksi.CreateGrid( 5, 5 )
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
## Class MyFrame51
###########################################################################

class MyFrame51 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"==================================================", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"Ubah Data Manger", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )

		self.m_staticText1011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.tabelkeberuntungan = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 375,200 ), 0 )

		# Grid
		self.tabelkeberuntungan.CreateGrid( 0, 10 )
		self.tabelkeberuntungan.EnableEditing( False )
		self.tabelkeberuntungan.EnableGridLines( True )
		self.tabelkeberuntungan.EnableDragGridSize( False )
		self.tabelkeberuntungan.SetMargins( 0, 35 )

		# Columns
		self.tabelkeberuntungan.SetColSize( 0, 80 )
		self.tabelkeberuntungan.SetColSize( 1, 241 )
		self.tabelkeberuntungan.SetColSize( 2, 159 )
		self.tabelkeberuntungan.SetColSize( 3, 159 )
		self.tabelkeberuntungan.SetColSize( 4, 100 )
		self.tabelkeberuntungan.SetColSize( 5, 80 )
		self.tabelkeberuntungan.SetColSize( 6, 112 )
		self.tabelkeberuntungan.SetColSize( 7, 80 )
		self.tabelkeberuntungan.SetColSize( 8, 80 )
		self.tabelkeberuntungan.EnableDragColMove( False )
		self.tabelkeberuntungan.EnableDragColSize( True )
		self.tabelkeberuntungan.SetColLabelSize( 30 )
		self.tabelkeberuntungan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelkeberuntungan.AutoSizeRows()
		self.tabelkeberuntungan.EnableDragRowSize( False )
		self.tabelkeberuntungan.SetRowLabelSize( 80 )
		self.tabelkeberuntungan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelkeberuntungan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelkeberuntungan.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer12.Add( self.tabelkeberuntungan, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer11.SetMinSize( wx.Size( -1,-200 ) )
		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.m_toggleBtn1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_toggleBtn1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_toggleBtn1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer11.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )

		self.m_toggleBtn11 = wx.ToggleButton( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.m_toggleBtn11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_toggleBtn11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_toggleBtn11.SetBackgroundColour( wx.Colour( 255, 106, 106 ) )

		fgSizer11.Add( self.m_toggleBtn11, 0, wx.ALL, 5 )


		bSizer12.Add( fgSizer11, 1, wx.EXPAND, 5 )


		gbSizer2.Add( bSizer12, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,200 ) )
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Kode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		self.m_staticText111.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Nama Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Jenis Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL )
		self.m_textCtrl6.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Harga Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl7.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		self.m_staticText151.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText151.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText151, 0, wx.ALL, 5 )


		bSizer13.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button5.SetMinSize( wx.Size( 130,50 ) )

		fgSizer12.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 191, 23, 23 ) )

		fgSizer12.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer13.Add( fgSizer12, 1, wx.EXPAND, 5 )


		gbSizer2.Add( bSizer13, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		bSizer4.Add( gbSizer2, 1, wx.EXPAND, 5 )

		self.m_staticText1012 = wx.StaticText( self, wx.ID_ANY, u"==================================================", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1012.Wrap( -1 )

		self.m_staticText1012.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1012.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1012, 0, wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabelkeberuntungan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelkeberuntunganOnGridCmdSelectCell )
		self.m_toggleBtn1.Bind( wx.EVT_TOGGLEBUTTON, self.button_Refresh2 )
		self.m_toggleBtn11.Bind( wx.EVT_TOGGLEBUTTON, self.button_kembali )
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_simpanEdit )
		self.m_button51.Bind( wx.EVT_BUTTON, self.button_hapus )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
		event.Skip()

	def button_Refresh2( self, event ):
		event.Skip()

	def button_kembali( self, event ):
		event.Skip()

	def button_simpanEdit( self, event ):
		event.Skip()

	def button_hapus( self, event ):
		event.Skip()


