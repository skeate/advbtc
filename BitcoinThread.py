"""
BitcoinThread.py

Handles connection/communication to bitcoin API
"""

from jsonrpc import ServiceProxy, JSONRPCException
from threading import Thread
import shelve
from sys import platform as _platform
import os
import re


class BitcoinThread(Thread):
    """Main class"""
    def __init__(self, work_queue):
        super(BitcoinThread, self).__init__()
        self.queue = work_queue
        self.username = ""
        self.password = ""
        self.address = ""
        self.secure = False
        self.get_rpc_info()
        url = "http%s://%s:%s@%s" % \
            ('s' if self.secure else '',
             self.username,
             self.password,
             self.address)
        self.rpc = ServiceProxy(url)

    def run(self):
        while True:
            task = self.queue.get()
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
                    used = dict((x[0], x[1]) for sub in used for x in sub)
                    # but if it hasn't been used, it won't be in the list
                    # so merge it with a complete address listing
                    every = self.rpc.listreceivedbyaddress(0, True)
                    ret = [[x['address'],
                           used[x['address']] if x['address'] in used else 0,
                           x['account']] for x in every]
                elif task[0] == 'reconnect':
                    self.get_rpc_info()
                    url = "http://%s:%s@%s" % \
                        (self.username, self.password, self.address)
                    self.rpc = ServiceProxy(url)
                elif task[0] == 'create address':
                    ret = self.rpc.getnewaddress('default')
                elif task[0] == 'send to address':
                    ret = self.rpc.sendtoaddress(*task[2:])
                else:
                    print 'Unknown command.'
                    ret = False
            except JSONRPCException as ex:
                print repr(ex.error)
            except Exception as ex:
                if task[0] == 'beat':
                    ret = False
                else:
                    print "Exception: ",
                    print ex
            finally:
                task[1](ret)
                self.queue.task_done()

    def get_rpc_info(self):
        """Fetch RPC connection information from bitcoin.conf"""
        settings = shelve.open('settings')
        conf_name = 'bitcoin_conf_dir'
        addr_name = 'bitcoin_rpc_address'
        if not conf_name in settings:
            if _platform.startswith('linux'):
                settings[conf_name] = os.environ['HOME'] + \
                    '/.bitcoin/bitcoin.conf'
            elif _platform == 'darwin':
                settings[conf_name] = os.environ['HOME'] + \
                    '/Library/Application Support/Bitcoin/bitcoin.conf'
            elif _platform == 'win32':
                settings[conf_name] = os.environ['APPDATA'] + \
                    r'\Bitcoin\bitcoin.conf'
        bcc = open(settings[conf_name], 'r')
        for line in bcc:
            match = re.search(r'rpc(user|password)\s*=\s*([^# \n]+)', line)
            if match:
                if match.group(1) == 'user':
                    self.username = match.group(2)
                else:
                    self.password = match.group(2)
        if self.username == '' or self.password == '':
            raise Exception("Couldn't find username in given bitcoin.conf")
        if not addr_name in settings:
            settings[addr_name] = 'localhost:8332'
        self.address = settings[addr_name]
        if not 'use_ssl' in settings:
            settings['use_ssl'] = False
        self.secure = settings['use_ssl']
        settings.close()
