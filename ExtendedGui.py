#!/usr/bin/env python
"""ExtendedGui.py

Extends the GUI classes generated with wxFormBuilder.
"""

import sys
import wx
import shelve
import pyperclip
from BaseGui import MainWindow, AboutWindow, SettingsWindow

class SettingsWindowEx(SettingsWindow):
    def __init__(self, parent, queue):
        SettingsWindow.__init__(self, parent)
        self.queue = queue
    def open(self, event):
        settings = shelve.open('settings')
        self.bccloc.SetPath(settings['bitcoin_conf_dir'])
        self.bcdaddr.SetValue(settings['bitcoin_rpc_address'])
        self.useSSL.SetValue(settings['use_ssl'])
        settings.close()
    def save_settings(self, event):
        settings = shelve.open('settings')
        settings['bitcoin_conf_dir'] = self.bccloc.GetPath()
        settings['bitcoin_rpc_address'] = self.bcdaddr.GetValue()
        settings['use_ssl'] = self.useSSL.GetValue()
        settings.close()
        self.queue.put(('reconnect', self.close))
    def close(self, event):
        self.Close()

class MainWindowEx(MainWindow):
    """Set up main window and define all event handlers."""
    def __init__(self, queue):
        MainWindow.__init__(self, None)
        self.work_queue = queue

        # set up timer to check connection
        # and update balance
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._update, self.timer)
        self.timer.Start(0)

    # Timer event
    def _update(self, event):
        """Called on timeout; updates balances and connection info."""
        self.work_queue.put(('beat', self._update_cb))
        self.timer.Start(1000)
        event.Skip()
    def _update_cb(self, data):
        """Callback for timeout event."""
        if data is False:
            self.status_bar.SetStatusText('Connection error.')
            self.overview_cbalance.SetLabel('connection error')
            self.overview_ucbalance.SetLabel('connection error')
        else:
            self.status_bar.SetStatusText(
                    'Connected to server (%d connections to network)'
                    % data['connections'])
            self.overview_cbalance.SetLabel('%.8f' % data['balance'])
            self.overview_ucbalance.SetLabel(
                    '%.8f' % ( data['ubalance'] - data['balance'] ))

    # Menubar events
    def menu_exit(self, event):
        sys.exit()

    def menu_about(self, event):
        AboutWindow(wx.GetApp().TopWindow).Show()

    def menu_options(self, event):
        SettingsWindowEx(wx.GetApp().TopWindow, self.work_queue).Show()

    # Address Panel events
    def paddrs_enable_btns(self, event):
        self.paddrs_newtx_btn.Enable(True)
        self.paddrs_copy_btn.Enable(True)
        event.Skip()

    def paddrs_disable_btns(self, event):
        self.paddrs_newtx_btn.Enable(False)
        self.paddrs_copy_btn.Enable(False)
        event.Skip()

    def paddrs_copy(self, event):
        address_row = self.paddrs_list.GetFirstSelected()
        address = self.paddrs_list.GetItem(address_row, 0).GetText()
        pyperclip.copy(address)

    def paddrs_create(self, event):
        self.work_queue.put(('create address', self.paddrs_create_cb))
        event.Skip()
    def paddrs_create_cb(self, data):
        print data

    def paddrs_refresh(self, event):
        self.work_queue.put(('get addresses', self.paddrs_refresh_cb))
        self.paddrs_refresh_btn.SetLabel('loading...')
        self.paddrs_refresh_btn.Enable(False)
        event.Skip()
    def paddrs_refresh_cb(self, data):
        zero_count = 0
        self.paddrs_list.DeleteAllItems()
        dict_form = dict(zip(range(len(data)), data))
        self.paddrs_list.setData(dict_form)
        index = 0
        for key, data in dict_form.items():
            if not self.paddrs_showall.IsChecked() and data[1] == 0:
                if not self.paddrs_showlabeled.IsChecked() or data[2] == '':
                    continue
            zero_count += 1
            # some addresses do not have labels,
            # so set label field to empty string
            if len(data) == 2:
                data.append("")
            self.paddrs_list.InsertStringItem(index, data[0])
            self.paddrs_list.SetStringItem(index, 1, '%.8f' % data[1])
            self.paddrs_list.SetStringItem(index, 2, data[2])
            self.paddrs_list.SetItemData(index, key)
        self.paddrs_list.SortListItems(1, 0)
        self.paddrs_count.SetLabel('%d / %d' % (zero_count, len(dict_form)))
        self.paddrs_refresh_btn.SetLabel('Show Addresses')
        self.paddrs_refresh_btn.Enable(True)

    # simple tx events
    def ctx_simple_send(self, event):
        self.work_queue.put(('send to address',
                             self.ctx_simple_send_cb,
                             self.ctx_simple_recipient.Value,
                             self.ctx_simple_amount.Value))
        self.ctx_simple_clear(self, None)
    def ctx_simple_send_cb(self, data):
        print "hello"

    def ctx_simple_clear(self, event):
        self.ctx_simple_recipient.Clear()
        self.ctx_simple_amount.Clear()
