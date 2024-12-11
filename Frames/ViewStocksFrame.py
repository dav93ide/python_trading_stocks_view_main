import wx
from Panels import ViewStocksPanel
from Resources.Constants import Constants

class ViewStocksFrame(wx.Frame):

    def __init__(self, title, stock):
        wx.Frame.__init__(self, None, wx.ID_ANY, title, size=Constants.DISPLAY_SIZE_MAIN_FRAME)
        wx.Frame.CenterOnScreen(self)
        self.__init_main_panel(stock)

    def __init_main_panel(self, stock):
        self.__mMainPanel = ViewStocksPanel.ViewStocksPanel(self, wx.DisplaySize(), stock)
        self.__mMainPanel.Show()