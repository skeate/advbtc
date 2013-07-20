"""Subclass of MainWindow, which is generated by wxFormBuilder."""

import wx
import BaseGui

# Implementing MainWindow
class MainWindowEx( BaseGui.MainWindow ):
	def __init__( self, parent ):
		BaseGui.MainWindow.__init__( self, parent )
        self.work_queue = queue

        # set up address events
        self.Bind(wx.EVT_LIST_ITEM_SELECTED,
                  self.enableAddrButtons, self.addrList)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED,
                  self.disableAddrButtons, self.addrList)

        # set up timer to check connection
        # and update balance
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer.Start(0)

	
	# Handlers for MainWindow events.
	def menu_backup( self, event ):
		# TODO: Implement menu_backup
		pass
	
	def menu_exit( self, event ):
		# TODO: Implement menu_exit
		pass
	
	def menu_encrypt( self, event ):
		# TODO: Implement menu_encrypt
		pass
	
	def menu_changePassphrase( self, event ):
		# TODO: Implement menu_changePassphrase
		pass
	
	def menu_settings( self, event ):
		# TODO: Implement menu_settings
		pass
	
	def menu_about( self, event ):
		# TODO: Implement menu_about
		pass
	
	def paddrs_refresh( self, event ):
		# TODO: Implement paddrs_refresh
		pass
	
	def paddrs_create( self, event ):
		# TODO: Implement paddrs_create
		pass
	
	def paddrs_newtx( self, event ):
		# TODO: Implement paddrs_newtx
		pass
	
	def paddrs_copy( self, event ):
		# TODO: Implement paddrs_copy
		pass
	
	def ctx_simple_send( self, event ):
		# TODO: Implement ctx_simple_send
		pass
	
	def ctx_simple_clear( self, event ):
		# TODO: Implement ctx_simple_clear
		pass
	
	
