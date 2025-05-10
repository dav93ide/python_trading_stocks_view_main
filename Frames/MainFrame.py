import wx, os, uuid
from Environment import Environment
from Resources.Constants import *
from Panels.MainPanel import MainPanel
from Panels.PlatformDataPanel import PlatformDataPanel
from Panels.NewTradingStrategyPanel import NewTradingStrategyPanel
from Panels.NewBotPanel import NewBotPanel
from Panels.ViewStocksPanel import ViewStocksPanel
from Panels.AddStockApplicationData import AddStockApplicationData
from Resources.Strings import Strings
from Utils.RegexUtils import RegexUtils
from Classes.ConfigurationData import ConfigurationData
from Networking.DataSynchronization import DataSynchronization

class MainFrame(wx.Frame):

    __mMainPanel: MainPanel = None
    __mPlatformDataPanel: PlatformDataPanel = None
    __mNewTradingStrategyPanel: NewTradingStrategyPanel = None
    __mNewBotPanel: NewBotPanel = None
    __mViewStocksPanel: ViewStocksPanel = None
    __mAddStocksApplicationPanel: AddStockApplicationData = None

    __mMenubar: wx.MenuBar = None

    __mProgressDialog: wx.ProgressDialog = None

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title=Strings.STR_TRADING_BOT, size=Constants.DISPLAY_SIZE_MAIN_FRAME)
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
        self.__init_menu_main_menu()
        self.__init_menu_settings()
        self.__init_menu_views()
        self.__init_menu_new_trading_strategy()
        self.__init_menu_bot()
        self.__init_menu_stocks()
        self.SetMenuBar(self.__mMenubar)

    def __init_menu_main_menu(self):
        mainMenu = wx.Menu()
        m00 = mainMenu.Append(-1, Strings.STR_MAIN_MENU)
        self.__mMenubar.Append(mainMenu, Strings.STR_MAIN_MENU)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_main_menu, m00)

    def __init_menu_settings(self):
        settingsMenu = wx.Menu()
        m11 = settingsMenu.Append(-1, Strings.STR_MENU_SETTINGS_PLATFORM_DATA)
        m12 = settingsMenu.Append(-1, Strings.STR_MENU_SETTINGS_BOTS)
        m13 = settingsMenu.Append(-1, Strings.STR_MENU_SETTINGS_SIMULATIONS)
        self.__mMenubar.Append(settingsMenu, Strings.STR_MENU_SETTINGS)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_settings_platform_data, m11)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_settings_bots, m12)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_settings_simulations, m13)

    def __init_menu_views(self):
        viewMenu = wx.Menu()
        m21 = viewMenu.Append(-1, Strings.STR_MENU_VIEW_ASSETS)
        m22 = viewMenu.Append(-1, Strings.STR_MENU_VIEW_BOTS)
        m23 = viewMenu.Append(-1, Strings.STR_MENU_VIEW_SIMULATIONS)
        m24 = viewMenu.Append(-1, Strings.STR_MENU_VIEW_CHARTS)
        self.__mMenubar.Append(viewMenu, Strings.STR_MENU_VIEW)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_view_assets, m21)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_view_bots, m22)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_view_simulations, m23)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_view_charts, m24)

    def __init_menu_new_trading_strategy(self):
        newTradingStrategyMenu = wx.Menu()
        m31 = newTradingStrategyMenu.Append(-1, Strings.STR_MENU_TRADING_STRATEGY_NEW_TRADING_STRATEGY)
        m32 = newTradingStrategyMenu.Append(-1, Strings.STR_MENU_TRADING_STRATEGY_NEW_DIVIDEND_STRATEGY)
        m33 = newTradingStrategyMenu.Append(-1, Strings.STR_MENU_TRADING_STRATEGY_NEW_COPY_TRADER_STRATEGY)
        self.__mMenubar.Append(newTradingStrategyMenu, Strings.STR_MENU_TRADING_STRATEGY)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_new_trading_strategy, m31)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_new_dividend_strategy, m32)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_new_copy_trader_strategy, m33)

    def __init_menu_bot(self):
        botMenu = wx.Menu()
        m41 = botMenu.Append(-1, Strings.STR_MENU_BOT_NEW_BOT)
        self.__mMenubar.Append(botMenu, Strings.STR_MENU_BOT)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_bot_new_bot, m41)

    def __init_menu_stocks(self):
        botMenu = wx.Menu()
        m51 = botMenu.Append(-1, Strings.STR_MENU_STOCKS_VIEW)
        m52 = botMenu.Append(-1, Strings.STR_MENU_ADD_STOCK_APPLICATION)
        self.__mMenubar.Append(botMenu, Strings.STR_MENU_STOCKS)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_stocks_view, m51)
        self.Bind(wx.EVT_MENU, self.__on_click_menu_stocks_add_stock_application, m52)
#endregion

#region - Init Panels Methods
    def __init_main_panel(self):
        self.__remove_all_panels()
        self.__mMainPanel = MainPanel(self, wx.DisplaySize())
        self.__mMainPanel.Show()

    def __init_platform_data_panel(self):
        self.__remove_all_panels()
        self.__mPlatformDataPanel = PlatformDataPanel(self, wx.DisplaySize())
        self.__mPlatformDataPanel.Show()

    def __init_new_trading_strategy_panel(self):
        self.__remove_all_panels()
        self.__mNewTradingStrategyPanel = NewTradingStrategyPanel(self, wx.DisplaySize())
        self.__mNewTradingStrategyPanel.Show()

    def __init_new_bot_panel(self):
        self.__remove_all_panels()
        self.__mNewBotPanel = NewBotPanel(self, wx.DisplaySize())
        self.__mNewBotPanel.Show()

    def __init_view_stocks_panel(self):
        self.__remove_all_panels()
        self.__mViewStocksPanel = ViewStocksPanel(self, wx.DisplaySize(), None)
        self.__mViewStocksPanel.Show()

    def __init_add_stocks_application_panel(self):
        self.__remove_all_panels()
        self.__mAddStocksApplicationPanel = AddStockApplicationData(self, wx.DisplaySize())
        self.__mAddStocksApplicationPanel.Show()

#endregion

#region - Remove Panel Methods
    def __remove_all_panels(self):
        self.__remove_main_panel()
        self.__remove_platform_data_panel()
        self.__remove_new_trading_bot_panel()
        self.__remove_new_bot_panel()
        self.__remove_view_stocks_panel()
        self.__remove_add_stocks_application_panel()

    def __remove_main_panel(self):
        if self.__mMainPanel:
            self.__mMainPanel.Destroy()

    def __remove_platform_data_panel(self):
        if self.__mPlatformDataPanel:
            self.__mPlatformDataPanel.Destroy()

    def __remove_new_trading_bot_panel(self):
        if self.__mNewTradingStrategyPanel:
            self.__mNewTradingStrategyPanel.Destroy()

    def __remove_new_bot_panel(self):
        if self.__mNewBotPanel:
            self.__mNewBotPanel.Destroy()

    def __remove_view_stocks_panel(self):
        if self.__mViewStocksPanel:
            self.__mViewStocksPanel.Destroy()

    def __remove_add_stocks_application_panel(self):
        if self.__mAddStocksApplicationPanel:
            self.__mAddStocksApplicationPanel.Destroy()
#endregion

#region - On Click Methods
    def __on_click_menu_main_menu(self, evt):
        self.__init_main_panel()

    def __on_click_menu_settings_platform_data(self, evt):
        self.__init_platform_data_panel()

    def __on_click_menu_settings_bots(self, evt):
        logging.info("__on_click_menu_settings_bots")

    def __on_click_menu_settings_simulations(self, evt):
        logging.info("__on_click_menu_settings_simulations")

    def __on_click_menu_view_assets(self, evt):
        logging.info("__on_click_menu_view_assets")

    def __on_click_menu_view_bots(self, evt):
        logging.info("__on_click_menu_view_bots")

    def __on_click_menu_view_simulations(self, evt):
        logging.info("__on_click_menu_view_simulations")

    def __on_click_menu_view_charts(self, evt):
        logging.info("__on_click_menu_view_charts")

    def __on_click_menu_new_trading_strategy(self, evt):
        self.__init_new_trading_strategy_panel()

    def __on_click_menu_new_dividend_strategy(self, evt):
        logging.info("__on_click_menu_bon_click_menu_new_dividend_strategyot_new_dividend_bot")

    def __on_click_menu_new_copy_trader_strategy(self, evt):
        logging.info("__on_click_menu_new_copy_trader_strategy")

    def __on_click_menu_bot_new_bot(self, evt):
        self.__init_new_bot_panel()

    def __on_click_menu_stocks_view(self, evt):
        self.__init_view_stocks_panel()

    def __on_click_menu_stocks_add_stock_application(self, evt):
        self.__init_add_stocks_application_panel()
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