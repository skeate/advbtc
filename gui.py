# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from AddressListControl import AddressListControl

import gettext
_ = gettext.gettext

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"advbtc"), pos = wx.DefaultPosition, size = wx.Size( 850,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Backup Wallet"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem2.SetBitmap( wx.Bitmap( u"icons/wallet--arrow.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"E&xit"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem3.SetBitmap( wx.Bitmap( u"icons/cross.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu1.AppendItem( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu1, _(u"&File") ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, _(u"Encrypt Wallet"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem4.SetBitmap( wx.Bitmap( u"icons/lock.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, _(u"Change Passphrase"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem5.SetBitmap( wx.Bitmap( u"icons/lock--pencil.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.AppendItem( self.m_menuItem5 )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menuItem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, _(u"Options"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem6.SetBitmap( wx.Bitmap( u"icons/gear--pencil.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.AppendItem( self.m_menuItem6 )
		
		self.m_menubar1.Append( self.m_menu2, _(u"&Settings") ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, _(u"About"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem7.SetBitmap( wx.Bitmap( u"icons/question-white.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu3.AppendItem( self.m_menuItem7 )
		
		self.m_menubar1.Append( self.m_menu3, _(u"&Help") ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_notebook1ImageSize = wx.Size( 16,16 )
		m_notebook1Index = 0
		m_notebook1Images = wx.ImageList( m_notebook1ImageSize.GetWidth(), m_notebook1ImageSize.GetHeight() )
		self.m_notebook1.AssignImageList( m_notebook1Images )
		self.overPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		overSizer = wx.GridBagSizer( 0, 0 )
		overSizer.SetFlexibleDirection( wx.BOTH )
		overSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		
		overSizer.AddSpacer( ( 10, 10 ), wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self.overPanel, wx.ID_ANY, _(u"Wallet"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		overSizer.Add( self.m_staticText9, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self.overPanel, wx.ID_ANY, _(u"Confirmed Total Balance:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		overSizer.Add( self.m_staticText6, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.cBalance = wx.StaticText( self.overPanel, wx.ID_ANY, _(u"loading..."), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cBalance.Wrap( -1 )
		overSizer.Add( self.cBalance, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.overPanel, wx.ID_ANY, _(u"Unconfirmed Total Balance:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		overSizer.Add( self.m_staticText5, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.ucBalance = wx.StaticText( self.overPanel, wx.ID_ANY, _(u"loading..."), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ucBalance.Wrap( -1 )
		overSizer.Add( self.ucBalance, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.overPanel, wx.ID_ANY, _(u"Recent Transactions"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		overSizer.Add( self.m_staticText10, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		
		overSizer.Add( bSizer5, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		overSizer.AddGrowableCol( 3 )
		
		self.overPanel.SetSizer( overSizer )
		self.overPanel.Layout()
		overSizer.Fit( self.overPanel )
		self.m_notebook1.AddPage( self.overPanel, _(u"Overview"), True )
		m_notebook1Bitmap = wx.Bitmap( u"icons/block.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		self.addrPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		addrSizer = wx.GridBagSizer( 0, 0 )
		addrSizer.SetFlexibleDirection( wx.HORIZONTAL )
		addrSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.addrList = AddressListControl(self.addrPanel, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
		addrSizer.Add( self.addrList, wx.GBPosition( 0, 0 ), wx.GBSpan( 6, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		addrSizer.AddSpacer( ( 10, 10 ), wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.showAddr = wx.Button( self.addrPanel, wx.ID_ANY, _(u"Refresh Address List"), wx.DefaultPosition, wx.DefaultSize, 0 )
		addrSizer.Add( self.showAddr, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self.addrPanel, wx.ID_ANY, _(u"Show Empty Addresses:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		addrSizer.Add( self.m_staticText11, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.showZero = wx.CheckBox( self.addrPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		addrSizer.Add( self.showZero, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.addrPanel, wx.ID_ANY, _(u"Number of Addresses:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		addrSizer.Add( self.m_staticText12, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.numAddrs = wx.StaticText( self.addrPanel, wx.ID_ANY, _(u"?"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.numAddrs.Wrap( -1 )
		addrSizer.Add( self.numAddrs, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.addrPanel, wx.ID_ANY, _(u"New Transaction from\nSelected Address"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.Enable( False )
		
		addrSizer.Add( self.m_button3, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self.addrPanel, wx.ID_ANY, _(u"Copy Selected\nAddress"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.Enable( False )
		
		addrSizer.Add( self.m_button4, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		addrSizer.AddSpacer( ( 10, 10 ), wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		addrSizer.AddGrowableCol( 0 )
		addrSizer.AddGrowableRow( 1 )
		
		self.addrPanel.SetSizer( addrSizer )
		self.addrPanel.Layout()
		addrSizer.Fit( self.addrPanel )
		self.m_notebook1.AddPage( self.addrPanel, _(u"Addresses"), False )
		m_notebook1Bitmap = wx.Bitmap( u"icons/address-book-blue.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		self.ctxPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listbook1 = wx.Listbook( self.ctxPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		m_listbook1ImageSize = wx.Size( 16,16 )
		m_listbook1Index = 0
		m_listbook1Images = wx.ImageList( m_listbook1ImageSize.GetWidth(), m_listbook1ImageSize.GetHeight() )
		self.m_listbook1.AssignImageList( m_listbook1Images )
		self.m_panel7 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.m_panel7, _(u"Simple"), True )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.m_panel8 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.m_panel8, _(u"Deposit"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-retweet.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.m_panel9 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.m_panel9, _(u"Escrow"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-skip.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.m_panel10 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.m_panel10, _(u"Assurance"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-join.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.m_panel11 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.m_panel11, _(u"Micro"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-000-small.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		
		bSizer6.Add( self.m_listbook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.ctxPanel.SetSizer( bSizer6 )
		self.ctxPanel.Layout()
		bSizer6.Fit( self.ctxPanel )
		self.m_notebook1.AddPage( self.ctxPanel, _(u"Create Tx"), False )
		m_notebook1Bitmap = wx.Bitmap( u"icons/mail-send.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		self.ltxPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.ltxPanel, _(u"Load Tx"), False )
		m_notebook1Bitmap = wx.Bitmap( u"icons/mail-open-document-text.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		self.txhPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl2 = wx.ListCtrl( self.txhPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		bSizer8.Add( self.m_listCtrl2, 1, wx.EXPAND, 5 )
		
		
		self.txhPanel.SetSizer( bSizer8 )
		self.txhPanel.Layout()
		bSizer8.Fit( self.txhPanel )
		self.m_notebook1.AddPage( self.txhPanel, _(u"Tx History"), False )
		m_notebook1Bitmap = wx.Bitmap( u"icons/receipts-text.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		
		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.menu_backup, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_exit, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_encrypt, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_changePassphrase, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_settings, id = self.m_menuItem6.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_about, id = self.m_menuItem7.GetId() )
		self.showAddr.Bind( wx.EVT_BUTTON, self.loadAddresses )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def menu_backup( self, event ):
		pass
	
	def menu_exit( self, event ):
		pass
	
	def menu_encrypt( self, event ):
		pass
	
	def menu_changePassphrase( self, event ):
		pass
	
	def menu_settings( self, event ):
		pass
	
	def menu_about( self, event ):
		pass
	
	def loadAddresses( self, event ):
		pass
	

###########################################################################
## Class AboutWindow
###########################################################################

class AboutWindow ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"About"), pos = wx.DefaultPosition, size = wx.Size( 221,78 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_hyperlink5 = wx.HyperlinkCtrl( self, wx.ID_ANY, _(u"advbtc 0.2"), u"https://github.com/skeate/advbtc", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer3.Add( self.m_hyperlink5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Some icons by "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer4.Add( self.m_staticText3, 0, 0, 5 )
		
		self.m_hyperlink3 = wx.HyperlinkCtrl( self, wx.ID_ANY, _(u"Yusuke Kamiyamane."), u"http://p.yusukekamiyamane.com/", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer4.Add( self.m_hyperlink3, 0, 0, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

