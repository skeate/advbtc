from jsonrpc import ServiceProxy, JSONRPCException
from threading import Thread

class BitcoinThread(Thread):
  def __init__(self,rpcinfo,workQueue):
    super(BitcoinThread, self).__init__()
    self.q = workQueue
    url = "http://%s:%s@localhost:8332" % rpcinfo
    self.rpc = ServiceProxy(url)

  def run(self):
    while True:
      task = self.q.get()
      if task[0] == 'listaddressgroupings':
        ret = self.rpc.listaddressgroupings()
        ret = [item for sublist in ret for item in sublist]
      elif task[0] == 'getbalance':
        ret = self.rpc.getbalance()
      elif task[0] == 'getucbalance':
        ret = self.rpc.getbalance('*', 0)
      task[1](ret)
      self.q.task_done()
