import wx
from enum import IntEnum
from Panels.Base.BasePanel import BasePanel
from Resources.Strings import Strings
from Utils.WxUtils import WxUtils
from Resources.Constants import TradingStrategyType, Sizes
from Classes.TradingStrategy import TradingStrategy


class SelectionCodes(IntEnum):
    SELECTION_TRADING_STRATEGY = 0
    SELECTION_DIVIDEND_STRATEGY = 1
    SELECTION_COPY_TRADER_STRATEGY = 2

class NewBotPanel(BasePanel):
    
    __mtxName: wx.TextCtrl = None
    __mcTradingStrategyType: wx.Choice = None
    __mcTradingStrategy: wx.Choice = None

    __mTradingStrategies = []

    def __init__(self, parent, size):
        super().__init__(parent, size)
        self.__get_all_trading_strategies()
        self.__init_layout()

#region - Private Methods
#region - Init Methods
    def __init_layout(self):
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(self.__get_top_panel(), 0, wx.EXPAND)
        main.AddSpacer(15)
        main.Add(self.__get_select_trading_strategies_panel(), 0, wx.EXPAND)

        self.SetSizer(main)
        self.Fit()
        self.Update()


    def __get_top_panel(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour((66, 66, 66))

        main = wx.BoxSizer(wx.HORIZONTAL)
        main.AddSpacer(100)

        hbs = wx.BoxSizer(wx.VERTICAL)
        static = wx.StaticText(panel, label = Strings.STR_NAME_NEW_BOT, style = wx.TE_CENTRE)
        WxUtils.set_font_size_and_bold(static, 15)
        hbs.Add(static, 0, wx.EXPAND)
        hbs.AddSpacer(10)
        self.__mtxName = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        hbs.Add(self.__mtxName, 0, wx.EXPAND)
        hbs.AddSpacer(10)

        main.Add(hbs, 1, wx.EXPAND)
        main.AddSpacer(100)

        panel.SetSizer(main)
        panel.Fit()
        panel.Update()

        return panel

    def __get_select_trading_strategies_panel(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour((66, 66, 66))

        main = wx.BoxSizer(wx.VERTICAL)
        main.AddSpacer(10)
        splitter = wx.SplitterWindow(panel)
        splitter.SplitVertically(
            self.__get_select_strategy_type_panel(splitter), 
            self.__get_select_trading_strategy_panel(splitter), 
            -round((wx.DisplaySize()[0] / 10 * 7))
        )
        main.Add(splitter, 1, wx.EXPAND)
        main.AddSpacer(10)
        
        panel.SetSizer(main)
        panel.Fit()
        panel.Update()

        return panel

    def __get_select_strategy_type_panel(self, splitter):
        panel = wx.Panel(splitter)
        main = wx.BoxSizer(wx.HORIZONTAL)
        main.AddSpacer(15)

        vbs = wx.BoxSizer(wx.VERTICAL)
        static = wx.StaticText(panel, label = Strings.STR_TRADING_STRATEGY_TYPE, style = wx.TE_CENTRE)
        WxUtils.set_font_size_and_bold(static, 15)
        vbs.Add(static, 0, wx.EXPAND)
        vbs.AddSpacer(10)
        self.__mcTradingStrategyType = wx.Choice(panel, wx.ID_ANY, size = Sizes.SELECTION_SIZE_TRADING_STRATEGY_TYPE_NEW_BOT, style = wx.ALIGN_CENTRE)
        self.__mcTradingStrategyType.SetItems(TradingStrategyType.get_all_names())
        self.__mcTradingStrategyType.Bind(wx.EVT_CHOICE, self.__on_trading_strategy_type_selected)
        vbs.Add(self.__mcTradingStrategyType, 0, wx.EXPAND)
        
        main.Add(vbs, 1, wx.EXPAND)
        main.AddSpacer(15)
        panel.SetSizer(main)
        panel.Fit()
        panel.Update()

        return panel

    def __get_select_trading_strategy_panel(self, splitter):
        panel = wx.Panel(splitter)
        main = wx.BoxSizer(wx.HORIZONTAL)
        main.AddSpacer(15)

        vbs = wx.BoxSizer(wx.VERTICAL)
        static = wx.StaticText(panel, label = Strings.STR_TRADING_STRATEGY, style = wx.TE_CENTRE)
        WxUtils.set_font_size_and_bold(static, 15)
        vbs.Add(static, 0, wx.EXPAND)
        vbs.AddSpacer(10)
        self.__mcTradingStrategy = wx.Choice(panel, wx.ID_ANY, size = Sizes.SELECTION_SIZE_TRADING_STRATEGY_NEW_BOT, style = wx.ALIGN_CENTRE)
        vbs.Add(self.__mcTradingStrategy, 0, wx.EXPAND)

        main.Add(vbs, 1, wx.EXPAND)
        main.AddSpacer(15)
        panel.SetSizer(main)
        panel.Fit()
        panel.Update()

        return panel
#endregion

#region - Trading Strategy Choice Listener Methods
    def __on_trading_strategy_type_selected(self, evt):
        choice = evt.GetEventObject()
        selection = choice.GetSelection()
        match selection:
            case SelectionCodes.SELECTION_TRADING_STRATEGY:
                self.__mcTradingStrategy.SetItems(self.__get_trading_strategies_names())
            case SelectionCodes.SELECTION_DIVIDEND_STRATEGY:
                self.__mcTradingStrategy.SetItems(["Dividend"])
            case SelectionCodes.SELECTION_COPY_TRADER_STRATEGY:
                self.__mcTradingStrategy.SetItems(["Copy Trader"])
            case _:
                self.__mcTradingStrategy.SetItems([])        
#endregion

#region - Get Data Methods
    def __get_all_trading_strategies(self):
        self.__mTradingStrategies = TradingStrategy.get_stored_data()

    def __get_trading_strategies_names(self):
        names = []
        if self.__mTradingStrategies is not None and len(self.__mTradingStrategies) > 0:
            for t in self.__mTradingStrategies:
                names.append(t.get_name())
        return names
#endregion
#endregion

