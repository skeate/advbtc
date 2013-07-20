# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from AddressListControl import AddressListControl
import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"advbtc"), pos = wx.DefaultPosition, size = wx.Size( 850,460 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.menu = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.menu_file, wx.ID_ANY, _(u"Backup Wallet"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem2.SetBitmap( wx.Bitmap( u"icons/wallet--arrow.png", wx.BITMAP_TYPE_ANY ) )
		self.menu_file.AppendItem( self.m_menuItem2 )
		
		self.menu_file.AppendSeparator()
		
		self.m_menuItem3 = wx.MenuItem( self.menu_file, wx.ID_ANY, _(u"E&xit"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem3.SetBitmap( wx.Bitmap( u"icons/cross.png", wx.BITMAP_TYPE_ANY ) )
		self.menu_file.AppendItem( self.m_menuItem3 )
		
		self.menu.Append( self.menu_file, _(u"&File") ) 
		
		self.menu_settings = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.menu_settings, wx.ID_ANY, _(u"Encrypt Wallet"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem4.SetBitmap( wx.Bitmap( u"icons/lock.png", wx.BITMAP_TYPE_ANY ) )
		self.menu_settings.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.menu_settings, wx.ID_ANY, _(u"Change Passphrase"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem5.SetBitmap( wx.Bitmap( u"icons/lock--pencil.png", wx.BITMAP_TYPE_ANY ) )
		self.menu_settings.AppendItem( self.m_menuItem5 )
		
		self.menu_settings.AppendSeparator()
		
		self.m_menuItem6 = wx.MenuItem( self.menu_settings, wx.ID_ANY, _(u"Options"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem6.SetBitmap( wx.Bitmap( u"icons/gear--pencil.png", wx.BITMAP_TYPE_ANY ) )
		self.menu_settings.AppendItem( self.m_menuItem6 )
		
		self.menu.Append( self.menu_settings, _(u"&Settings") ) 
		
		self.menu_help = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.menu_help, wx.ID_ANY, _(u"About"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem7.SetBitmap( wx.Bitmap( u"icons/question-white.png", wx.BITMAP_TYPE_ANY ) )
		self.menu_help.AppendItem( self.m_menuItem7 )
		
		self.menu.Append( self.menu_help, _(u"&Help") ) 
		
		self.SetMenuBar( self.menu )
		
		self.status_bar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_notebook1ImageSize = wx.Size( 16,16 )
		m_notebook1Index = 0
		m_notebook1Images = wx.ImageList( m_notebook1ImageSize.GetWidth(), m_notebook1ImageSize.GetHeight() )
		self.m_notebook1.AssignImageList( m_notebook1Images )
		self.overview = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		overSizer = wx.GridBagSizer( 0, 0 )
		overSizer.SetFlexibleDirection( wx.BOTH )
		overSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		
		overSizer.AddSpacer( ( 10, 10 ), wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self.overview, wx.ID_ANY, _(u"Wallet"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		overSizer.Add( self.m_staticText9, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self.overview, wx.ID_ANY, _(u"Confirmed Total Balance:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		overSizer.Add( self.m_staticText6, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.overview_cbalance = wx.StaticText( self.overview, wx.ID_ANY, _(u"loading..."), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.overview_cbalance.Wrap( -1 )
		overSizer.Add( self.overview_cbalance, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.overview, wx.ID_ANY, _(u"Unconfirmed Total Balance:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		overSizer.Add( self.m_staticText5, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.overview_ucbalance = wx.StaticText( self.overview, wx.ID_ANY, _(u"loading..."), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.overview_ucbalance.Wrap( -1 )
		overSizer.Add( self.overview_ucbalance, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.overview, wx.ID_ANY, _(u"Recent Transactions"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		overSizer.Add( self.m_staticText10, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		
		overSizer.Add( bSizer5, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		overSizer.AddGrowableCol( 3 )
		
		self.overview.SetSizer( overSizer )
		self.overview.Layout()
		overSizer.Fit( self.overview )
		self.m_notebook1.AddPage( self.overview, _(u"Overview"), True )
		m_notebook1Bitmap = wx.Bitmap( u"icons/block.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		self.paddrs = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		addrSizer = wx.GridBagSizer( 0, 0 )
		addrSizer.SetFlexibleDirection( wx.BOTH )
		addrSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		addrSizer.AddSpacer( ( 10, 10 ), wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.paddrs_refresh_btn = wx.Button( self.paddrs, wx.ID_ANY, _(u"Refresh Address List"), wx.DefaultPosition, wx.DefaultSize, 0 )
		addrSizer.Add( self.paddrs_refresh_btn, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.paddrs_create_btn = wx.Button( self.paddrs, wx.ID_ANY, _(u"Create New Address"), wx.DefaultPosition, wx.DefaultSize, 0 )
		addrSizer.Add( self.paddrs_create_btn, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( self.paddrs, wx.ID_ANY, _(u"Show Empty Labeled:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		addrSizer.Add( self.m_staticText15, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.paddrs_showlabeled = wx.CheckBox( self.paddrs, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.paddrs_showlabeled.SetValue(True) 
		addrSizer.Add( self.paddrs_showlabeled, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.paddrs, wx.ID_ANY, _(u"Show All:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		addrSizer.Add( self.m_staticText11, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.paddrs_showall = wx.CheckBox( self.paddrs, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		addrSizer.Add( self.paddrs_showall, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.paddrs, wx.ID_ANY, _(u"Number of Addresses:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		addrSizer.Add( self.m_staticText12, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.paddrs_count = wx.StaticText( self.paddrs, wx.ID_ANY, _(u"?"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.paddrs_count.Wrap( -1 )
		addrSizer.Add( self.paddrs_count, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.paddrs_newtx_btn = wx.Button( self.paddrs, wx.ID_ANY, _(u"New Transaction from\nSelected Address"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.paddrs_newtx_btn.Enable( False )
		
		addrSizer.Add( self.paddrs_newtx_btn, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.paddrs_copy_btn = wx.Button( self.paddrs, wx.ID_ANY, _(u"Copy Address\nto Clipboard"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.paddrs_copy_btn.Enable( False )
		
		addrSizer.Add( self.paddrs_copy_btn, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		addrSizer.AddSpacer( ( 10, 10 ), wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.paddrs_list = AddressListControl( self.paddrs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		addrSizer.Add( self.paddrs_list, wx.GBPosition( 0, 0 ), wx.GBSpan( 7, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		addrSizer.AddGrowableCol( 0 )
		addrSizer.AddGrowableRow( 1 )
		addrSizer.AddGrowableRow( 2 )
		
		self.paddrs.SetSizer( addrSizer )
		self.paddrs.Layout()
		addrSizer.Fit( self.paddrs )
		self.m_notebook1.AddPage( self.paddrs, _(u"Personal Addresses"), False )
		m_notebook1Bitmap = wx.Bitmap( u"icons/address-book-blue.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		self.ctx = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listbook1 = wx.Listbook( self.ctx, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_LEFT )
		m_listbook1ImageSize = wx.Size( 16,16 )
		m_listbook1Index = 0
		m_listbook1Images = wx.ImageList( m_listbook1ImageSize.GetWidth(), m_listbook1ImageSize.GetHeight() )
		self.m_listbook1.AssignImageList( m_listbook1Images )
		self.ctx_simple = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.VERTICAL )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		
		gbSizer3.AddSpacer( ( 10, 10 ), wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.m_staticText16 = wx.StaticText( self.ctx_simple, wx.ID_ANY, _(u"Recipient:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gbSizer3.Add( self.m_staticText16, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.ctx_simple_recipient = wx.TextCtrl( self.ctx_simple, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.ctx_simple_recipient, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( self.ctx_simple, wx.ID_ANY, _(u"Amount (BTC):"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gbSizer3.Add( self.m_staticText17, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.ctx_simple_amount = wx.TextCtrl( self.ctx_simple, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.ctx_simple_amount, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer3.AddSpacer( ( 10, 10 ), wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.ctx_simple_send_btn = wx.Button( self.ctx_simple, wx.ID_ANY, _(u"Send"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.ctx_simple_send_btn, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 3 ), wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.ctx_simple_clear_btn = wx.Button( self.ctx_simple, wx.ID_ANY, _(u"Clear"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.ctx_simple_clear_btn, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 3 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer3.AddGrowableRow( 0 )
		gbSizer3.AddGrowableRow( 5 )
		
		self.ctx_simple.SetSizer( gbSizer3 )
		self.ctx_simple.Layout()
		gbSizer3.Fit( self.ctx_simple )
		self.m_listbook1.AddPage( self.ctx_simple, _(u"Simple"), True )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.ctx_multi = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.ctx_multi, _(u"Multi"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-split.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.ctx_deposit = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.ctx_deposit, _(u"Deposit"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-retweet.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.ctx_escrow = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.ctx_escrow, _(u"Escrow"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-skip.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.ctx_assurance = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.ctx_assurance, _(u"Assurance"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-join.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.ctx_micro = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.ctx_micro, _(u"Micro"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-000-small.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		self.ctx_custom = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText18 = wx.StaticText( self.ctx_custom, wx.ID_ANY, _(u"Inputs"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.m_staticText18, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.ctx_custom, wx.ID_ANY, _(u"Outputs"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.m_staticText19, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.ctx_custom_inputs = wx.ListCtrl( self.ctx_custom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		gbSizer4.Add( self.ctx_custom_inputs, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )
		
		self.ctx_custom_outputs = wx.ListCtrl( self.ctx_custom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		gbSizer4.Add( self.ctx_custom_outputs, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self.ctx_custom, wx.ID_ANY, _(u"Tx Hash"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gbSizer4.Add( self.m_staticText20, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.ctx_custom_input_hash = wx.TextCtrl( self.ctx_custom, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.ctx_custom_input_hash, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self.ctx_custom, wx.ID_ANY, _(u"Index"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gbSizer4.Add( self.m_staticText22, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.ctx_custom_input_index = wx.TextCtrl( self.ctx_custom, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.ctx_custom_input_index, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText27 = wx.StaticText( self.ctx_custom, wx.ID_ANY, _(u"Seq"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gbSizer4.Add( self.m_staticText27, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( self.ctx_custom, wx.ID_ANY, _(u"0xFFFFFFFF"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.m_textCtrl12, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.ctx_custom_input_script = wx.TextCtrl( self.ctx_custom, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		gbSizer4.Add( self.ctx_custom_input_script, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 4 ), wx.BOTTOM|wx.EXPAND, 5 )
		
		self.ctx_custom_output_script = wx.TextCtrl( self.ctx_custom, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		gbSizer4.Add( self.ctx_custom_output_script, wx.GBPosition( 4, 5 ), wx.GBSpan( 2, 2 ), wx.BOTTOM|wx.EXPAND, 5 )
		
		self.m_staticText24 = wx.StaticText( self.ctx_custom, wx.ID_ANY, _(u"scriptSig"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gbSizer4.Add( self.m_staticText24, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 4 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )
		
		self.m_staticText25 = wx.StaticText( self.ctx_custom, wx.ID_ANY, _(u"scriptPubKey"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		gbSizer4.Add( self.m_staticText25, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 2 ), wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )
		
		self.m_staticText23 = wx.StaticText( self.ctx_custom, wx.ID_ANY, _(u"Amount (BTC)"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gbSizer4.Add( self.m_staticText23, wx.GBPosition( 2, 5 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.ctx_custom_output_amount = wx.TextCtrl( self.ctx_custom, wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.ctx_custom_output_amount, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.ctx_custom_create = wx.Button( self.ctx_custom, wx.ID_ANY, _(u"Create"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ctx_custom_create.SetDefault() 
		self.ctx_custom_create.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.ctx_custom_create, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button13 = wx.Button( self.ctx_custom, wx.ID_ANY, _(u"Reference"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.m_button13, wx.GBPosition( 7, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.ctx_custom_reset = wx.Button( self.ctx_custom, wx.ID_ANY, _(u"Reset"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.ctx_custom_reset, wx.GBPosition( 7, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.ctx_custom_generated = wx.TextCtrl( self.ctx_custom, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		gbSizer4.Add( self.ctx_custom_generated, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText26 = wx.StaticText( self.ctx_custom, wx.ID_ANY, _(u"Lock Time"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		gbSizer4.Add( self.m_staticText26, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 0 )
		
		self.m_textCtrl11 = wx.TextCtrl( self.ctx_custom, wx.ID_ANY, _(u"0xFFFFFFFF"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.m_textCtrl11, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )
		
		self.m_staticline1 = wx.StaticLine( self.ctx_custom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		gbSizer4.Add( self.m_staticline1, wx.GBPosition( 0, 4 ), wx.GBSpan( 6, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer4.AddGrowableCol( 1 )
		gbSizer4.AddGrowableCol( 6 )
		gbSizer4.AddGrowableRow( 5 )
		gbSizer4.AddGrowableRow( 8 )
		
		self.ctx_custom.SetSizer( gbSizer4 )
		self.ctx_custom.Layout()
		gbSizer4.Fit( self.ctx_custom )
		self.m_listbook1.AddPage( self.ctx_custom, _(u"Custom"), False )
		m_listbook1Bitmap = wx.Bitmap( u"icons/arrow-transition.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook1Bitmap.Ok() ):
			m_listbook1Images.Add( m_listbook1Bitmap )
			self.m_listbook1.SetPageImage( m_listbook1Index, m_listbook1Index )
			m_listbook1Index += 1
		
		
		bSizer6.Add( self.m_listbook1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.ctx.SetSizer( bSizer6 )
		self.ctx.Layout()
		bSizer6.Fit( self.ctx )
		self.m_notebook1.AddPage( self.ctx, _(u"Create Tx"), False )
		m_notebook1Bitmap = wx.Bitmap( u"icons/mail-send.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		self.ltx = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.ltx, _(u"Load Tx"), False )
		m_notebook1Bitmap = wx.Bitmap( u"icons/mail-open-document-text.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		self.txhist = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl2 = wx.ListCtrl( self.txhist, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		bSizer8.Add( self.m_listCtrl2, 1, wx.EXPAND, 5 )
		
		
		self.txhist.SetSizer( bSizer8 )
		self.txhist.Layout()
		bSizer8.Fit( self.txhist )
		self.m_notebook1.AddPage( self.txhist, _(u"Tx History"), False )
		m_notebook1Bitmap = wx.Bitmap( u"icons/receipts-text.png", wx.BITMAP_TYPE_ANY )
		if ( m_notebook1Bitmap.Ok() ):
			m_notebook1Images.Add( m_notebook1Bitmap )
			self.m_notebook1.SetPageImage( m_notebook1Index, m_notebook1Index )
			m_notebook1Index += 1
		
		self.addrbook = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.addrbook, _(u"Address Book"), False )
		m_notebook1Bitmap = wx.Bitmap( u"icons/address-book.png", wx.BITMAP_TYPE_ANY )
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
		self.Bind( wx.EVT_MENU, self.menu_change_passphrase, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_options, id = self.m_menuItem6.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_about, id = self.m_menuItem7.GetId() )
		self.paddrs_refresh_btn.Bind( wx.EVT_BUTTON, self.paddrs_refresh )
		self.paddrs_create_btn.Bind( wx.EVT_BUTTON, self.paddrs_create )
		self.paddrs_newtx_btn.Bind( wx.EVT_BUTTON, self.paddrs_newtx )
		self.paddrs_copy_btn.Bind( wx.EVT_BUTTON, self.paddrs_copy )
		self.paddrs_list.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.paddrs_disable_btns )
		self.paddrs_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.paddrs_enable_btns )
		self.ctx_simple_send_btn.Bind( wx.EVT_BUTTON, self.ctx_simple_send )
		self.ctx_simple_clear_btn.Bind( wx.EVT_BUTTON, self.ctx_simple_clear )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def menu_backup( self, event ):
		pass
	
	def menu_exit( self, event ):
		pass
	
	def menu_encrypt( self, event ):
		pass
	
	def menu_change_passphrase( self, event ):
		pass
	
	def menu_options( self, event ):
		pass
	
	def menu_about( self, event ):
		pass
	
	def paddrs_refresh( self, event ):
		pass
	
	def paddrs_create( self, event ):
		pass
	
	def paddrs_newtx( self, event ):
		pass
	
	def paddrs_copy( self, event ):
		pass
	
	def paddrs_disable_btns( self, event ):
		pass
	
	def paddrs_enable_btns( self, event ):
		pass
	
	def ctx_simple_send( self, event ):
		pass
	
	def ctx_simple_clear( self, event ):
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
	

###########################################################################
## Class TxReference
###########################################################################

class TxReference ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Custom Transaction Reference"), pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

