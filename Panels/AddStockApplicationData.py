import wx
from Panels.Base.BasePanel import BasePanel
from Resources.Strings import Strings
from Utils.WxUtils import WxUtils

class AddStockApplicationData(BasePanel):

    __mLeftPanel = None

    __mChoPlatformData: wx.Choice = None

    def __init__(self, parent, size):
        super().__init__(parent, size)
        self.__init_layout()

#region - Private Methods
    def __init_layout(self):
        main = wx.BoxSizer(wx.VERTICAL)
        splitter = wx.SplitterWindow(self)
        vbs.Add(static, 0, wx.EXPAND)
        self.SetSizer(vbs)
#endregion