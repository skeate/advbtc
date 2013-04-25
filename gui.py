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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"advbtc"), pos = wx.DefaultPosition, size = wx.Size( 850,460 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		self.sb = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
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
		addrSizer.SetFlexibleDirection( wx.BOTH )
		addrSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.addrList = AddressListControl(self.addrPanel, wx.ID_ANY, style=wx.LC_SINGLE_SEL | wx.LC_REPORT | wx.SUNKEN_BORDER)
		addrSizer.Add( self.addrList, wx.GBPosition( 0, 0 ), wx.GBSpan( 8, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		addrSizer.AddSpacer( ( 10, 10 ), wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.showAddr = wx.Button( self.addrPanel, wx.ID_ANY, _(u"Refresh Address List"), wx.DefaultPosition, wx.DefaultSize, 0 )
		addrSizer.Add( self.showAddr, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.newAddr = wx.Button( self.addrPanel, wx.ID_ANY, _(u"Create New Address"), wx.DefaultPosition, wx.DefaultSize, 0 )
		addrSizer.Add( self.newAddr, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( self.addrPanel, wx.ID_ANY, _(u"Show Empty Labeled:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		addrSizer.Add( self.m_staticText15, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.showLabeled = wx.CheckBox( self.addrPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.showLabeled.SetValue(True) 
		addrSizer.Add( self.showLabeled, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.addrPanel, wx.ID_ANY, _(u"Show All:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		addrSizer.Add( self.m_staticText11, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.showAll = wx.CheckBox( self.addrPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		addrSizer.Add( self.showAll, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.addrPanel, wx.ID_ANY, _(u"Number of Addresses:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		addrSizer.Add( self.m_staticText12, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.numAddrs = wx.StaticText( self.addrPanel, wx.ID_ANY, _(u"?"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.numAddrs.Wrap( -1 )
		addrSizer.Add( self.numAddrs, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.newTxBtn = wx.Button( self.addrPanel, wx.ID_ANY, _(u"New Transaction from\nSelected Address"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.newTxBtn.Enable( False )
		
		addrSizer.Add( self.newTxBtn, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.copyAddrBtn = wx.Button( self.addrPanel, wx.ID_ANY, _(u"Copy Address\nto Clipboard"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.copyAddrBtn.Enable( False )
		
		addrSizer.Add( self.copyAddrBtn, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		addrSizer.AddSpacer( ( 10, 10 ), wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		addrSizer.AddGrowableCol( 0 )
		addrSizer.AddGrowableRow( 1 )
		addrSizer.AddGrowableRow( 2 )
		
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
		
		self.m_listbook1 = wx.Listbook( self.ctxPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_LEFT )
		m_listbook1ImageSize = wx.Size( 16,16 )
		m_listbook1Index = 0
		m_listbook1Images = wx.ImageList( m_listbook1ImageSize.GetWidth(), m_listbook1ImageSize.GetHeight() )
		self.m_listbook1.AssignImageList( m_listbook1Images )
		self.txSimplePanel = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.txSimplePanel, _(u"Simple"), True )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.txDepositPanel = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.txDepositPanel, _(u"Deposit"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-retweet.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.txEscrowPanel = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.txEscrowPanel, _(u"Escrow"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-skip.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.txAssurancePanel = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.txAssurancePanel, _(u"Assurance"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-join.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.txMicroPanel = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.txMicroPanel, _(u"Micro"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-000-small.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.txCustomPanel = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.txCustomPanel, _(u"Custom"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-transition.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		
		bSizer6.Add( self.m_listbook1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
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
		self.showAddr.Bind( wx.EVT_BUTTON, self.listAddresses )
		self.newAddr.Bind( wx.EVT_BUTTON, self.createAddress )
		self.newTxBtn.Bind( wx.EVT_BUTTON, self.newTxWithAddress )
		self.copyAddrBtn.Bind( wx.EVT_BUTTON, self.copyAddress )
	
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
	
	def listAddresses( self, event ):
		pass
	
	def createAddress( self, event ):
		pass
	
	def newTxWithAddress( self, event ):
		pass
	
	def copyAddress( self, event ):
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
	

###########################################################################
## Class SettingsWindow
###########################################################################

class SettingsWindow ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Settings"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"bitcoin.conf location:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer1.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.bccloc = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), u"bitcoin.conf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fgSizer1.Add( self.bccloc, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, _(u"bitcoind Address:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer1.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.bcdaddr = wx.TextCtrl( self, wx.ID_ANY, _(u"localhost:8332"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.bcdaddr, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, _(u"Secure (SSL) Connection:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer1.Add( self.m_staticText13, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.useSSL = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.useSSL, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( fgSizer1, 3, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button7, 1, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button8, 1, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.open )
		self.m_button7.Bind( wx.EVT_BUTTON, self.saveSettings )
		self.m_button8.Bind( wx.EVT_BUTTON, self.close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def open( self, event ):
		pass
	
	def saveSettings( self, event ):
		pass
	
	def close( self, event ):
		pass
	

###########################################################################
## Class PasswordWindow
###########################################################################

class PasswordWindow ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Enter Password"), pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, _(u"Enter password to unlock wallet:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer10.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.m_textCtrl2.SetMinSize( wx.Size( 300,-1 ) )
		
		bSizer10.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button9, 1, wx.ALL, 5 )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button10, 1, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer10 )
		self.Layout()
		bSizer10.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

