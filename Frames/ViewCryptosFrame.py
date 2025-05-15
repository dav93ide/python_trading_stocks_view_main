import wx
from Panels import ViewCryptosPanel
from Resources.Constants import Constants

class ViewCryptosFrame(wx.Frame):

    def __init__(self, title, crypto):
        wx.Frame.__init__(self, None, wx.ID_ANY, title, size=Constants.DISPLAY_SIZE_MAIN_FRAME)
        wx.Frame.CenterOnScreen(self)
        self.__init_main_panel(crypto)

    def __init_main_panel(self, crypto):
        self.__mMainPanel = ViewCryptosPanel.ViewCryptosPanel(self, wx.DisplaySize(), stock)
        self.__mMainPanel.Show()