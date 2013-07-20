import wx
import wx.lib.mixins.listctrl as listmix

class AddressListControl(
    wx.ListCtrl,
    listmix.ListCtrlAutoWidthMixin,
    listmix.ColumnSorterMixin):
  def __init__(self, parent, ID, pos=wx.DefaultPosition,
      size=wx.DefaultSize, style=0):
    wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
    self.itemDataMap = None
    self.itemIndexMap = None
    listmix.ListCtrlAutoWidthMixin.__init__(self)
    listmix.ColumnSorterMixin.__init__(self, 3)
    self.setResizeColumn(0)
    self.InsertColumn(0, 'Address')
    self.InsertColumn(1, 'Balance', width=100)
    self.InsertColumn(2, 'Label', width=100)

  def GetListCtrl(self):
    return self

  def setData(self, data):
    self.itemDataMap = data
    self.itemIndexMap = range(len(data))
