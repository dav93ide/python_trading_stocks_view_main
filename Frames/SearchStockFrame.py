import wx
from Panels.SearchStockPanel import SearchStockPanel
from Resources.Constants import Constants
from Classes.FilterClasses.FilterSearchStockPanel import FilterSearchStockPanel

class SearchStockFrame(wx.Frame):

    def __init__(self, title, filterData):
        wx.Frame.__init__(self, None, wx.ID_ANY, title, size=Constants.DISPLAY_SIZE_MAIN_FRAME)
        wx.Frame.CenterOnScreen(self)
        self.__init_main_panel(filterData)

    def __init_main_panel(self, filterData):
        self.__mMainPanel = SearchStockPanel(self, wx.DisplaySize(), filterData)
        self.__mMainPanel.Show()