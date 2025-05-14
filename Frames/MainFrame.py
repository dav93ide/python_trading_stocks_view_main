import wx, os, uuid
from Environment import Environment
from Resources.Constants import *
from Panels.ViewStocksPanel import ViewStocksPanel
from Panels.ViewCryptosPanel import ViewCryptosPanel
from Resources.Strings import Strings
from Utils.RegexUtils import RegexUtils
from Networking.DataSynchronization import DataSynchronization

class MainFrame(wx.Frame):

    __mViewStocksPanel: ViewStocksPanel = None
    __mViewCryptosPanel : ViewCryptosPanel = None

    __mMenubar: wx.MenuBar = None

    __mProgressDialog: wx.ProgressDialog = None

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title=Strings.STR_TRADING_STOCKS_VIEW, size=Constants.DISPLAY_SIZE_MAIN_FRAME)
        wx.Frame.CenterOnScreen(self)
        self.Maximize(True)
        self.Show()
        self.__init_layout()

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

#region - Private Methods
    def __init_layout(self):
        self.__init_menubar()
        self.__init_view_stocks_panel()
        
#region - Init Menu Methods
    def __init_menubar(self):
        self.__mMenubar = wx.MenuBar()
        self.__init_menu_assets()
        self.SetMenuBar(self.__mMenubar)

    def __init_menu_assets(self):
        assetsMenu = wx.Menu()
        m11 = assetsMenu.Append(-1, Strings.STR_MENU_STOCKS)
        m12 = assetsMenu.Append(-1, Strings.STR_MENU_CRYPTO)
        self.__mMenubar.Append(assetsMenu, Strings.STR_MENU_ASSETS_VIEW)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_stocks_view, m11)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_cryptos_view, m12)
#endregion

#region - Init Panels Methods
    def __init_view_stocks_panel(self):
        self.__remove_all_panels()
        self.__mViewStocksPanel = ViewStocksPanel(self, wx.DisplaySize(), [], None)
        self.__mViewStocksPanel.Show()

    def __init_view_cryptos_panel(self):
        self.__remove_all_panels()
        self.__mViewCryptosPanel = ViewCryptosPanel(self, wx.DisplaySize(), [], None)
        self.__mViewCryptosPanel.Show()
#endregion

#region - Remove Panel Methods
    def __remove_all_panels(self):
        self.__remove_view_stocks_panel()
        self.__remove_view_cryptos_panel()

    def __remove_view_stocks_panel(self):
        if self.__mViewStocksPanel:
            self.__mViewStocksPanel.Destroy()

    def __remove_view_cryptos_panel(self):
        if self.__mViewCryptosPanel:
            self.__mViewCryptosPanel.Destroy()
#endregion

#region - On Click Methods
    def __on_click_menu_stocks_view(self, evt):
        self.__init_view_stocks_panel()

    def __on_click_menu_cryptos_view(self, evt):
        self.__init_view_cryptos_panel()
#endregion
#endregion