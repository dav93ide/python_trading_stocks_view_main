import wx, os, uuid
from Environment import Environment
from Resources.Constants import *
from Panels.MainPanel import MainPanel
from Panels.ViewStocksPanel import ViewStocksPanel
from Resources.Strings import Strings
from Utils.RegexUtils import RegexUtils
from Classes.ConfigurationData import ConfigurationData
from Networking.DataSynchronization import DataSynchronization

class MainFrame(wx.Frame):

    __mMainPanel: MainPanel = None
    __mViewStocksPanel: ViewStocksPanel = None

    __mMenubar: wx.MenuBar = None

    __mProgressDialog: wx.ProgressDialog = None

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title=Strings.STR_TRADING_STOCKS_VIEW, size=Constants.DISPLAY_SIZE_MAIN_FRAME)
        wx.Frame.CenterOnScreen(self)
        self.Maximize(True)
        self.Show()
        self.__check_configuration()

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

#region - Private Methods
    def __init_layout(self):
        self.__init_menubar()
        self.__init_main_panel()
        
#region - Init Menu Methods
    def __init_menubar(self):
        self.__mMenubar = wx.MenuBar()
        self.__init_menu_stocks()
        self.SetMenuBar(self.__mMenubar)

    def __init_menu_stocks(self):
        botMenu = wx.Menu()
        m11 = botMenu.Append(-1, Strings.STR_MENU_STOCKS_VIEW)
        self.__mMenubar.Append(botMenu, Strings.STR_MENU_STOCKS)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_stocks_view, m11)
#endregion

#region - Init Panels Methods
    def __init_main_panel(self):
        self.__remove_all_panels()
        self.__mMainPanel = MainPanel(self, wx.DisplaySize())
        self.__mMainPanel.Show()

    def __init_view_stocks_panel(self):
        self.__remove_all_panels()
        self.__mViewStocksPanel = ViewStocksPanel(self, wx.DisplaySize(), None)
        self.__mViewStocksPanel.Show()
#endregion

#region - Remove Panel Methods
    def __remove_all_panels(self):
        self.__remove_main_panel()
        self.__remove_view_stocks_panel()

    def __remove_main_panel(self):
        if self.__mMainPanel:
            self.__mMainPanel.Destroy()

    def __remove_view_stocks_panel(self):
        if self.__mViewStocksPanel:
            self.__mViewStocksPanel.Destroy()
#endregion

#region - On Click Methods
    def __on_click_menu_main_menu(self, evt):
        self.__init_main_panel()

    def __on_click_menu_stocks_view(self, evt):
        self.__init_view_stocks_panel()
#endregion

#region - Check Configuration Methods
    def __check_configuration(self):
        configuration = Environment().get_configuration()
        if not configuration:
            configuration = ConfigurationData(uuid.uuid4())
        if not configuration.get_is_initialized():
            self.__mProgressDialog = wx.ProgressDialog(Strings.STR_INITIAL_SYNCHRONIZATION, "", maximum=100, parent=None, style=wx.PD_APP_MODAL|wx.PD_AUTO_HIDE|wx.PD_ELAPSED_TIME)
            if DataSynchronization.sync_initial_all_stocks_and_symbols(self.__mProgressDialog):
                configuration.set_is_initialized(True)
                configuration.store_data()
        self.__init_layout()
#endregion
#endregion