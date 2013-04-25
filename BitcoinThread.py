from jsonrpc import ServiceProxy, JSONRPCException
from threading import Thread
import shelve
from sys import platform as _platform
import os
import re

class BitcoinThread(Thread):
  def __init__(self, workQueue):
    super(BitcoinThread, self).__init__()
    self.q = workQueue
    self.username = ""
    self.password = ""
    self.address = ""
    self.secure = False
    self.getRPCInfo()
    url = "http%s://%s:%s@%s" % \
      ('s' if self.secure else '', self.username, self.password, self.address)
    self.rpc = ServiceProxy(url)

  def run(self):
    while True:
      task = self.q.get()
      try:
        if task[0] == 'beat':
          ret = {
              'connections': self.rpc.getconnectioncount(),
              'balance': self.rpc.getbalance(),
              'ubalance': self.rpc.getbalance('*', 0)
              }
        elif task[0] == 'get addresses':
          # listaddressgroupings can be used to find account balances
          used = self.rpc.listaddressgroupings()
          used = dict((x[0], x[1]) for sublist in used for x in sublist)
          # but if it hasn't been used, it won't be in the list
          # so merge it with a complete address listing
          every = self.rpc.listreceivedbyaddress(0, True)
          ret = [[x['address'],
                  used[x['address']] if used.has_key(x['address']) else 0,
                  x['account']] for x in every]
        elif task[0] == 'reconnect':
          self.getRPCInfo()
          url = "http://%s:%s@%s" % (self.username, self.password, self.address)
          self.rpc = ServiceProxy(url)
        elif task[0] == 'create address':
          ret = self.rpc.getnewaddress('default')
        else:
          print 'Unknown command.'
          ret = False
      except Exception as ex:
        if task[0] == 'beat':
          ret = False
        else:
          print ex
      finally:
        task[1](ret)
      self.q.task_done()

  def getRPCInfo(self):
    settings = shelve.open('settings')
    confName = 'bitcoin_conf_dir'
    addrName = 'bitcoin_rpc_address'
    if not settings.has_key(confName):
      if _platform.startswith('linux'):
        settings[confName] = os.environ['HOME'] + '/.bitcoin/bitcoin.conf'
      elif _platform == 'darwin':
        settings[confName] = os.environ['HOME'] + \
          '/Library/Application Support/Bitcoin/bitcoin.conf'
      elif _platform == 'win32':
        settings[confName] = os.environ['APPDATA'] + r'\Bitcoin\bitcoin.conf'
    bcc = open(settings[confName], 'r')
    for line in bcc:
      m = re.search(r'rpc(user|password)\s*=\s*([^# \n]+)', line)
      if m:
        if m.group(1) == 'user':
          self.username = m.group(2)
        else:
          self.password = m.group(2)
    if self.username == '' or self.password == '':
      raise Exception("Couldn't find username in given bitcoin.conf")
    if not settings.has_key(addrName):
      settings[addrName] = 'localhost:8332'
    self.address = settings[addrName]
    if not settings.has_key('use_ssl'):
      settings['use_ssl'] = False
    self.secure = settings['use_ssl']
    settings.close()
