#!/usr/bin/env python
#
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.6.6 (standalone edition) on Thu Apr 04 23:06:43 2013
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
import re
import os
from sys import platform as _platform
from AdvFrame import AdvFrame
from BitcoinThread import BitcoinThread
import glbls

def getRPCInfo():
  if _platform.startswith('linux'):
    bcc = open(os.environ['HOME'] + '/.bitcoin/bitcoin.conf', 'r')
  elif _platform == 'darwin':
    bcc = open(os.environ['HOME'] +
        '/Library/Application Support/Bitcoin/bitcoin.conf', 'r')
  elif _platform == 'win32':
    bcc = open(os.environ['APPDATA'] + r'\Bitcoin\bitcoin.conf', 'r')
  username = ""
  password = ""
  for line in bcc:
    m = re.search(r'rpc(user|password)\s*=\s*([^# \n]+)', line)
    if m:
      if m.group(1) == 'user':
        username = m.group(2)
      else:
        password = m.group(2)
  if username == '' or password == '':
    return False
  return (username, password)


if __name__ == "__main__":
  gettext.install("advbtc") # replace with the appropriate catalog name

  rpcinfo = getRPCInfo()
  if not rpcinfo:
    print "Could not load RPC info from bitcoin.conf"
    exit(1)

  btc = BitcoinThread(rpcinfo, glbls.workQueue)
  btc.setDaemon(True)
  btc.start()

  app = wx.PySimpleApp(0)
  wx.InitAllImageHandlers()
  frame_1 = AdvFrame()
  app.SetTopWindow(frame_1)
  frame_1.Show()
  app.MainLoop()
