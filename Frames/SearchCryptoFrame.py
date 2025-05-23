import wx
from Panels.SearchCryptoPanel import SearchCryptoPanel
from Resources.Constants import Constants
from Classes.FilterClasses.FilterSearchCryptoPanel import FilterSearchCryptoPanel

class SearchCryptoFrame(wx.Frame):

    def __init__(self, title, filterData):
        wx.Frame.__init__(self, None, wx.ID_ANY, title, size = Constants.DISPLAY_SIZE_SEARCH_STOCKS_FRAME)
        wx.Frame.CenterOnScreen(self)
        self.__init_main_panel(filterData)

    def __init_main_panel(self, filterData):
        self.__mMainPanel = SearchCryptoPanel(self, wx.DisplaySize(), filterData)
        self.__mMainPanel.Show()