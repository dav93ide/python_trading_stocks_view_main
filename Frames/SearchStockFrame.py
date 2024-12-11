import wx
from Panels.SearchStockPanel import SearchStockPanel
from Resources.Constants import Constants

class SearchStockFrame(wx.Frame):

    def __init__(self, title):
        wx.Frame.__init__(self, None, wx.ID_ANY, title, size=Constants.DISPLAY_SIZE_MAIN_FRAME)
        wx.Frame.CenterOnScreen(self)
        self.__init_main_panel()

    def __init_main_panel(self):
        self.__mMainPanel = SearchStockPanel(self, wx.DisplaySize())
        self.__mMainPanel.Show()