import wx, threading, uuid
import wx.lib.scrolledpanel
from pyglet.window import key
from Panels.Base.BasePanel import BasePanel
from Utils.NumberUtils import NumberUtils
from Utils.KeyboardEventUtils import KeyboardEventUtils
from Utils.RegexUtils import RegexUtils
from Utils.WxUtils import WxUtils
from Resources.Strings import Strings
from Resources.Constants import Constants, Sizes, Regex, Colors
from Dialogs.ConfirmDialog import ConfirmDialog
from Classes.TradingStrategy import TradingStrategy
from Environment import Environment

class NewTradingStrategyPanel(BasePanel):

    __mMainBox: wx.BoxSizer = None
    __mSecondBox: wx.BoxSizer = None
    __mVerticalBoxBotInfos: wx.BoxSizer = None

    __mMainSplitter = None

    __mLeftPanel: wx.lib.scrolledpanel = None
    __mRightPanel: wx.lib.scrolledpanel = None


    __mtxName: wx.TextCtrl = None

    __mtxMaxDayChange: wx.TextCtrl = None
    __mtxMinDayChange: wx.TextCtrl = None
    __mtxMaxMarketCap: wx.TextCtrl = None
    __mtxMinMarketCap: wx.TextCtrl = None
    __mtxMaxDayRange: wx.TextCtrl = None
    __mtxMinDayRange: wx.TextCtrl = None
    __mtxMaxWeekRange: wx.TextCtrl = None
    __mtxMinWeekRange: wx.TextCtrl = None
    __mtxMaxMonthRange: wx.TextCtrl = None
    __mtxMinMonthRange: wx.TextCtrl = None
    __mtxMaxYearRange: wx.TextCtrl = None
    __mtxMinYearRange: wx.TextCtrl = None
    __mtxMaxDayVolume: wx.TextCtrl = None
    __mtxMinDayVolume: wx.TextCtrl = None
    __mtxMaxCompanyValue: wx.TextCtrl = None
    __mtxMinCompanyValue: wx.TextCtrl = None
    __mtxMaxRatioCompanyValueMarketCap: wx.TextCtrl = None
    __mtxMinRatioCompanyValueMarketCap: wx.TextCtrl = None
    __mtxMaxBeta: wx.TextCtrl = None
    __mtxMinBeta: wx.TextCtrl = None
    __mtxMaxRatioPE: wx.TextCtrl = None
    __mtxMinRatioPE: wx.TextCtrl = None
    __mtxMaxEPS: wx.TextCtrl = None
    __mtxMinEPS: wx.TextCtrl = None
    __mtxMaxYearTarget: wx.TextCtrl = None
    __mtxMinYearTarget: wx.TextCtrl = None
    __mtxMaxTrailingPE: wx.TextCtrl = None
    __mtxMinTrailingPE: wx.TextCtrl = None
    __mtxMaxForwardPE: wx.TextCtrl = None
    __mtxMinForwardPE: wx.TextCtrl = None
    __mtxMaxPegRatio: wx.TextCtrl = None
    __mtxMinPegRatio: wx.TextCtrl = None
    __mtxMaxPriceSales: wx.TextCtrl = None
    __mtxMinPriceSales: wx.TextCtrl = None
    __mtxMaxPriceBook: wx.TextCtrl = None
    __mtxMinPriceBook: wx.TextCtrl = None
    __mtxMaxCompanyValueRevenue: wx.TextCtrl = None
    __mtxMinCompanyValueRevenue: wx.TextCtrl = None
    __mtxMaxCompanyValueEbitda: wx.TextCtrl = None
    __mtxMinCompanyValueEbitda: wx.TextCtrl = None

    def __init__(self, parent, size):
        super().__init__(parent, size)
        self.__init_layout()

#region - Private Methods
#region - Init Methods
    def __init_layout(self):      
        self.__mMainBox = wx.BoxSizer(wx.HORIZONTAL)         

        self.__mMainBox.AddSpacer(10)
        self.__mMainSplitter = wx.SplitterWindow(self)
        self.__init_left_panel()
        self.__init_right_panel()
        self.__mMainSplitter.SplitVertically(self.__mLeftPanel, self.__mRightPanel, round((wx.DisplaySize()[0] / 10 * 7)))
        
        self.__mMainBox.Add(self.__mMainSplitter, 1, wx.EXPAND)
        self.__mMainBox.AddSpacer(10)
        self.SetSizer(self.__mMainBox)        

#region - Panels Methods
    def __init_left_panel(self):
        self.__mLeftPanel = wx.lib.scrolledpanel.ScrolledPanel(self.__mMainSplitter, wx.ID_ANY)
        self.__mLeftPanel.SetSizer(self.__get_boxsizer_trading_strategy())
        self.__init_bind_listeners()
        self.__mLeftPanel.SetupScrolling()

    def __init_right_panel(self):
        self.__mRightPanel = wx.lib.scrolledpanel.ScrolledPanel(self.__mMainSplitter, wx.ID_ANY)
        self.__mRightPanel.SetBackgroundColour((66, 66, 66))
        self.__mRightPanel.SetupScrolling()

        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(15)
        
        vbs = wx.BoxSizer(wx.VERTICAL)
        vbs.AddSpacer(5)
        vbs.Add(wx.StaticText(self.__mRightPanel, label = Strings.STR_SPECIFICS_BOT, style = wx.ALIGN_CENTRE), 0, wx.EXPAND|wx.ALL)
        vbs.AddSpacer(5)
        self.__set_texts_bot_info()
        vbs.Add(self.__mVerticalBoxBotInfos)
        hbs.Add(vbs)
        vbs.AddSpacer(25)
        vbs.Add(self.__get_buttons())
        hbs.AddSpacer(25)

        hbs.Fit(self.__mRightPanel)
        self.__mRightPanel.SetSizer(hbs)
        self.__mRightPanel.Fit()
#endregion

#region - Layout Methods
    def __get_boxsizer_trading_strategy(self):
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(self.__get_panel_data(), 0, wx.EXPAND)
        main.AddSpacer(10)
        main.Add(self.__get_panel_trading_strategy_label(), 0, wx.EXPAND)
        main.Add(
        self.__get_panel_trading_strategy_data(
            self.__get_boxsizer_day_change, 
            self.__get_boxsizer_market_cap, 
            self.__get_boxsizer_day_range,
            self.__get_boxsizer_week_range, 
        ), 1, wx.ALL | wx.EXPAND)
        
        main.AddSpacer(15)
        main.Add(
        self.__get_panel_trading_strategy_data(
            self.__get_boxsizer_month_range,
            self.__get_boxsizer_year_range,
            self.__get_boxsizer_day_volume,
            self.__get_boxsizer_company_value
        ), 1, wx.ALL | wx.EXPAND)
        
        main.AddSpacer(15)
        main.Add(
        self.__get_panel_trading_strategy_data(
            self.__get_boxsizer_ratio_company_value_market_cap,
            self.__get_boxsizer_beta,
            self.__get_boxsizer_ratio_pe,
            self.__get_boxsizer_eps
        ), 1, wx.ALL | wx.EXPAND)
        
        main.AddSpacer(15)
        main.Add(
        self.__get_panel_trading_strategy_data(
            self.__get_boxsizer_year_target,
            self.__get_boxsizer_trailing_pe,
            self.__get_boxsizer_forward_pe,
            self.__get_boxsizer_peg_ratio
        ), 1, wx.ALL | wx.EXPAND)
        
        main.AddSpacer(15)
        main.Add(
        self.__get_panel_trading_strategy_data(
            self.__get_boxsizer_price_sales,
            self.__get_boxsizer_price_book,
            self.__get_boxsizer_company_value_revenue,
            self.__get_boxsizer_company_value_ebitda
        ), 1, wx.ALL | wx.EXPAND)

        return main

    def __get_panel_data(self):
        panel = wx.Panel(self.__mLeftPanel)
        panel.SetBackgroundColour((77, 77, 77))
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(self.__get_boxsizer_name_trading_strategy(panel), 1, wx.EXPAND | wx.ALL)

        panel.SetSizer(main)
        return panel

    def __get_boxsizer_name_trading_strategy(self, panel):
        main = wx.BoxSizer(wx.HORIZONTAL)
        main.AddSpacer(50)
        vbs = wx.BoxSizer(wx.VERTICAL)
        static = wx.StaticText(panel, label = Strings.STR_NAME_TRADING_STRATEGY, style = wx.TE_CENTRE)
        WxUtils.set_font_size_and_bold(static, 15)
        vbs.Add(static, 0, wx.EXPAND)
        vbs.AddSpacer(10)
        self.__mtxName = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        vbs.Add(self.__mtxName, 0, wx.EXPAND)
        vbs.AddSpacer(10)
        main.Add(vbs, 1, wx.EXPAND)
        main.AddSpacer(50)
        return main

    def __get_panel_trading_strategy_label(self):
        panel = wx.Panel(self.__mLeftPanel)
        panel.SetBackgroundColour((66, 66, 66))
        hbs = wx.BoxSizer(wx.HORIZONTAL)

        static = wx.StaticText(panel, label = Strings.STR_TRADING_STRATEGY_DATA.upper(), style = wx.TE_CENTRE)
        WxUtils.set_font_size_and_bold(static, 15)
        hbs.Add(static, 1, wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_panel_trading_strategy_data(self, f1, f2, f3, f4):
        boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer.AddSpacer(15)
        panel = wx.Panel(self.__mLeftPanel)
        panel.SetBackgroundColour((88, 88, 88))
        boxSizer.Add(f1(panel))
        boxSizer.AddSpacer(50)
        boxSizer.Add(f2(panel))
        boxSizer.AddSpacer(50)
        boxSizer.Add(f3(panel))
        boxSizer.AddSpacer(50)
        boxSizer.Add(f4(panel))
        boxSizer.AddSpacer(50)
        boxSizer.Fit(panel)

        panel.SetSizer(boxSizer)
        panel.Update()    
        panel.Fit()
        panel.SetAutoLayout(True)
        return panel

    def __get_buttons(self):
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.Add(super()._get_button(self.__mRightPanel, Strings.STR_RESET_ALL, self.__on_click_button_reset_values))
        hbs.AddSpacer(50)
        hbs.Add(super()._get_button(self.__mRightPanel, Strings.STR_SAVE, self.__on_click_button_save))
        return hbs
#endregion

#region - Init Listeners Methods
    def __init_bind_listeners(self):
        self.__mtxMaxDayChange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinDayChange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxMarketCap.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinMarketCap.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxDayRange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinDayRange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxWeekRange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinWeekRange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxMonthRange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinMonthRange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxYearRange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinYearRange.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxDayVolume.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinDayVolume.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxCompanyValue.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinCompanyValue.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxRatioCompanyValueMarketCap.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinRatioCompanyValueMarketCap.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxBeta.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinBeta.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxRatioPE.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinRatioPE.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxEPS.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinEPS.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxYearTarget.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinYearTarget.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxTrailingPE.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinTrailingPE.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxForwardPE.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinForwardPE.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxPegRatio.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinPegRatio.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxPriceSales.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinPriceSales.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxPriceBook.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinPriceBook.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxCompanyValueRevenue.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinCompanyValueRevenue.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMaxCompanyValueEbitda.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        self.__mtxMinCompanyValueEbitda.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
#endregion
#endregion

#region - Event Handler Methods
    def __on_change_text_check_is_int_value(self, evt):
        if KeyboardEventUtils.on_change_text_check_is_int_value(self, evt):   
            children = self.__mVerticalBoxBotInfos.GetChildren()    

            match evt.GetEventObject():
                case self.__mtxMaxDayChange:
                    children[0].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[0].format("\t" + self.__mtxMaxDayChange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxDayChange.GetValue(), children[0])
                case self.__mtxMinDayChange:
                    children[1].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[1].format("\t" + self.__mtxMinDayChange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinDayChange.GetValue(), children[1])
                case self.__mtxMaxMarketCap:
                    children[2].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[2].format("\t" + self.__mtxMaxMarketCap.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxMarketCap.GetValue(), children[2])
                case self.__mtxMinMarketCap:
                    children[3].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[3].format("\t" + self.__mtxMinMarketCap.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinMarketCap.GetValue(), children[3])
                case self.__mtxMaxDayRange:
                    children[4].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[4].format("\t" + self.__mtxMaxDayRange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxDayRange.GetValue(), children[4])
                case self.__mtxMinDayRange:
                    children[5].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[5].format("\t" + self.__mtxMinDayRange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinDayRange.GetValue(), children[5])
                case self.__mtxMaxWeekRange:
                    children[6].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[6].format("\t" + self.__mtxMaxWeekRange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxWeekRange.GetValue(), children[6])
                case self.__mtxMinWeekRange:
                    children[7].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[7].format("\t" + self.__mtxMinWeekRange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinWeekRange.GetValue(), children[7])
                case self.__mtxMaxMonthRange:
                    children[8].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[8].format("\t" + self.__mtxMaxMonthRange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxMonthRange.GetValue(), children[8])
                case self.__mtxMinMonthRange:
                    children[9].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[9].format("\t" + self.__mtxMinMonthRange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinMonthRange.GetValue(), children[9])
                case self.__mtxMaxYearRange:
                    children[10].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[10].format("\t" + self.__mtxMaxYearRange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxYearRange.GetValue(), children[10])
                case self.__mtxMinYearRange:
                    children[11].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[11].format("\t" + self.__mtxMinYearRange.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinYearRange.GetValue(), children[11])
                case self.__mtxMaxDayVolume:
                    children[12].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[12].format("\t" + self.__mtxMaxDayVolume.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxDayVolume.GetValue(), children[12])
                case self.__mtxMinDayVolume:
                    children[13].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[13].format("\t" + self.__mtxMinDayVolume.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinDayVolume.GetValue(), children[13])
                case self.__mtxMaxCompanyValue:
                    children[14].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[14].format("\t" + self.__mtxMaxCompanyValue.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxCompanyValue.GetValue(), children[14])
                case self.__mtxMinCompanyValue:
                    children[15].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[15].format("\t" + self.__mtxMinCompanyValue.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinCompanyValue.GetValue(), children[15])
                case self.__mtxMaxRatioCompanyValueMarketCap:
                    children[16].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[16].format("\t" + self.__mtxMaxRatioCompanyValueMarketCap.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxRatioCompanyValueMarketCap.GetValue(), children[16])
                case self.__mtxMinRatioCompanyValueMarketCap:
                    children[17].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[17].format("\t" + self.__mtxMinRatioCompanyValueMarketCap.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinRatioCompanyValueMarketCap.GetValue(), children[17])
                case self.__mtxMaxBeta:
                    children[18].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[18].format("\t" + self.__mtxMaxBeta.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxBeta.GetValue(), children[18])
                case self.__mtxMinBeta:
                    children[19].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[19].format("\t" + self.__mtxMinBeta.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinBeta.GetValue(), children[19])
                case self.__mtxMaxRatioPE:
                    children[20].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[20].format("\t" + self.__mtxMaxRatioPE.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxRatioPE.GetValue(), children[20])
                case self.__mtxMinRatioPE:
                    children[21].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[21].format("\t" + self.__mtxMinRatioPE.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinRatioPE.GetValue(), children[21])
                case self.__mtxMaxEPS:
                    children[22].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[22].format("\t" + self.__mtxMaxEPS.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxEPS.GetValue(), children[22])
                case self.__mtxMinEPS:
                    children[23].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[23].format("\t" + self.__mtxMinEPS.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinEPS.GetValue(), children[23])
                case self.__mtxMaxYearTarget:
                    children[24].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[24].format("\t" + self.__mtxMaxYearTarget.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxYearTarget.GetValue(), children[24])
                case self.__mtxMinYearTarget:
                    children[25].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[25].format("\t" + self.__mtxMinYearTarget.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinYearTarget.GetValue(), children[25])
                case self.__mtxMaxTrailingPE:
                    children[26].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[26].format("\t" + self.__mtxMaxTrailingPE.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxTrailingPE.GetValue(), children[26])
                case self.__mtxMinTrailingPE:
                    children[27].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[27].format("\t" + self.__mtxMinTrailingPE.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinTrailingPE.GetValue(), children[27])
                case self.__mtxMaxForwardPE:
                    children[28].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[28].format("\t" + self.__mtxMaxForwardPE.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxForwardPE.GetValue(), children[28])
                case self.__mtxMinForwardPE:
                    children[29].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[29].format("\t" + self.__mtxMinForwardPE.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinForwardPE.GetValue(), children[29])
                case self.__mtxMaxPegRatio:
                    children[30].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[30].format("\t" + self.__mtxMaxPegRatio.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxPegRatio.GetValue(), children[30])
                case self.__mtxMinPegRatio:
                    children[31].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[31].format("\t" + self.__mtxMinPegRatio.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinPegRatio.GetValue(), children[31])
                case self.__mtxMaxPriceSales:
                    children[32].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[32].format("\t" + self.__mtxMaxPriceSales.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxPriceSales.GetValue(), children[32])
                case self.__mtxMinPriceSales:
                    children[33].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[33].format("\t" + self.__mtxMinPriceSales.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinPriceSales.GetValue(), children[33])
                case self.__mtxMaxPriceBook:
                    children[34].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[34].format("\t" + self.__mtxMaxPriceBook.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxPriceBook.GetValue(), children[34])
                case self.__mtxMinPriceBook:
                    children[35].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[35].format("\t" + self.__mtxMinPriceBook.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinPriceBook.GetValue(), children[35])
                case self.__mtxMaxCompanyValueRevenue:
                    children[36].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[36].format("\t" + self.__mtxMaxCompanyValueRevenue.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxCompanyValueRevenue.GetValue(), children[36])
                case self.__mtxMinCompanyValueRevenue:
                    children[37].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[37].format("\t" + self.__mtxMinCompanyValueRevenue.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinCompanyValueRevenue.GetValue(), children[37])
                case self.__mtxMaxCompanyValueEbitda:
                    children[38].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[38].format("\t" + self.__mtxMaxCompanyValueEbitda.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMaxCompanyValueEbitda.GetValue(), children[38])
                case self.__mtxMinCompanyValueEbitda:
                    children[39].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[39].format("\t" + self.__mtxMinCompanyValueEbitda.GetValue()))
                    self.__set_color_static_text_info_bot(self.__mtxMinCompanyValueEbitda.GetValue(), children[39])
        
    def __on_click_button_reset_values(self, evt):
        cDialog = ConfirmDialog(self, Strings.STR_DIALOG_TITLE_QUESTION_RESET_ALL_PARAMS, Strings.STR_MSG_QUESTION_RESET_ALL_PARAMS_ON_VIEW, self.__on_confirm_reset_values)
        cDialog.ShowModal()

    def __on_click_button_save(self, evt):
        if self.__check_insert_values():
            strategy = TradingStrategy(uuid.uuid4(), self.__mtxName.GetValue())     

            strategy.set_max_day_change(self.__mtxMaxDayChange.GetValue())
            strategy.set_min_day_change(self.__mtxMinDayChange.GetValue())
            strategy.set_max_market_cap(self.__mtxMaxMarketCap.GetValue())
            strategy.set_min_market_cap(self.__mtxMinMarketCap.GetValue())
            strategy.set_max_day_range(self.__mtxMaxDayRange.GetValue())
            strategy.set_min_day_range(self.__mtxMinDayRange.GetValue())
            strategy.set_max_week_range(self.__mtxMaxWeekRange.GetValue())
            strategy.set_min_week_range(self.__mtxMinWeekRange.GetValue())
            strategy.set_max_month_range(self.__mtxMaxMonthRange.GetValue())
            strategy.set_min_month_range(self.__mtxMinMonthRange.GetValue())
            strategy.set_max_year_range(self.__mtxMaxYearRange.GetValue())
            strategy.set_min_year_range(self.__mtxMinYearRange.GetValue())
            strategy.set_max_day_volume(self.__mtxMaxDayVolume.GetValue())
            strategy.set_min_day_volume(self.__mtxMinDayVolume.GetValue())
            strategy.set_max_company_value(self.__mtxMaxCompanyValue.GetValue())
            strategy.set_min_company_value(self.__mtxMinCompanyValue.GetValue())
            strategy.set_max_ratio_company_value_market_cap(self.__mtxMaxRatioCompanyValueMarketCap.GetValue())
            strategy.set_min_ratio_company_value_market_cap(self.__mtxMinRatioCompanyValueMarketCap.GetValue())
            strategy.set_max_beta(self.__mtxMaxBeta.GetValue())
            strategy.set_min_beta(self.__mtxMinBeta.GetValue())
            strategy.set_max_ratio_pe(self.__mtxMaxRatioPE.GetValue())
            strategy.set_min_ratio_pe(self.__mtxMinRatioPE.GetValue())
            strategy.set_max_eps(self.__mtxMaxEPS.GetValue())
            strategy.set_min_eps(self.__mtxMinEPS.GetValue())
            strategy.set_max_year_target(self.__mtxMaxYearTarget.GetValue())
            strategy.set_min_year_target(self.__mtxMinYearTarget.GetValue())
            strategy.set_max_trailing_pe(self.__mtxMaxTrailingPE.GetValue())
            strategy.set_min_trailing_pe(self.__mtxMinTrailingPE.GetValue())
            strategy.set_max_forward_pe(self.__mtxMaxForwardPE.GetValue())
            strategy.set_min_forward_pe(self.__mtxMinForwardPE.GetValue())
            strategy.set_max_peg_ratio(self.__mtxMaxPegRatio.GetValue())
            strategy.set_min_peg_ratio(self.__mtxMinPegRatio.GetValue())
            strategy.set_max_price_sales(self.__mtxMaxPriceSales.GetValue())
            strategy.set_min_price_sales(self.__mtxMinPriceSales.GetValue())
            strategy.set_max_price_book(self.__mtxMaxPriceBook.GetValue())
            strategy.set_min_price_book(self.__mtxMinPriceBook.GetValue())
            strategy.set_max_company_value_revenue(self.__mtxMaxCompanyValueRevenue.GetValue())
            strategy.set_min_company_value_revenue(self.__mtxMinCompanyValueRevenue.GetValue())
            strategy.set_max_company_value_ebitda(self.__mtxMaxCompanyValueEbitda.GetValue())
            strategy.set_min_company_value_ebitda(self.__mtxMinCompanyValueEbitda.GetValue())
        
            Environment().get_logger().info("] Storing TradingStrategy: \n\n%s\n\n" % strategy)

            strategy.add_to_stored_data_list()

            super()._show_message(Strings.STR_SUCCESS, Strings.STR_MSG_SUCCESS_INSERT_DATA)
            self.__mtxName.SetValue("")

#endregion

#region - Bot Info Methods
    def __set_texts_bot_info(self):
        self.__mVerticalBoxBotInfos = wx.BoxSizer(wx.VERTICAL)
        for s in Strings.STR_DATA_MAKING_BOT:
            txt = wx.StaticText(self.__mRightPanel, label = s.format(""), style = wx.ALIGN_LEFT)
            WxUtils.set_font_bold(txt)
            self.__mVerticalBoxBotInfos.Add(txt)

    def __set_color_static_text_info_bot(self, txt, child):
        if len(txt) > 0 and float(txt) > 0:
            child.GetWindow().SetForegroundColour(Colors.GREEN)
        elif len(txt) == 0 or float(txt) == 0:
            child.GetWindow().SetForegroundColour(Colors.WHITE)
        else:
            child.GetWindow().SetForegroundColour(Colors.RED)
#endregion

#region - Reset Values Methods
    def __on_confirm_reset_values(self):
        self.__mtxMaxDayChange.SetValue("")
        self.__mtxMinDayChange.SetValue("")
        self.__mtxMaxMarketCap.SetValue("")
        self.__mtxMinMarketCap.SetValue("")
        self.__mtxMaxDayRange.SetValue("")
        self.__mtxMinDayRange.SetValue("")
        self.__mtxMaxWeekRange.SetValue("")
        self.__mtxMinWeekRange.SetValue("")
        self.__mtxMaxMonthRange.SetValue("")
        self.__mtxMinMonthRange.SetValue("")
        self.__mtxMaxYearRange.SetValue("")
        self.__mtxMinYearRange.SetValue("")
        self.__mtxMaxDayVolume.SetValue("")
        self.__mtxMinDayVolume.SetValue("")
        self.__mtxMaxCompanyValue.SetValue("")
        self.__mtxMinCompanyValue.SetValue("")
        self.__mtxMaxRatioCompanyValueMarketCap.SetValue("")
        self.__mtxMinRatioCompanyValueMarketCap.SetValue("")
        self.__mtxMaxBeta.SetValue("")
        self.__mtxMinBeta.SetValue("")
        self.__mtxMaxRatioPE.SetValue("")
        self.__mtxMinRatioPE.SetValue("")
        self.__mtxMaxEPS.SetValue("")
        self.__mtxMinEPS.SetValue("")
        self.__mtxMaxYearTarget.SetValue("")
        self.__mtxMinYearTarget.SetValue("")
        self.__mtxMaxTrailingPE.SetValue("")
        self.__mtxMinTrailingPE.SetValue("")
        self.__mtxMaxForwardPE.SetValue("")
        self.__mtxMinForwardPE.SetValue("")
        self.__mtxMaxPegRatio.SetValue("")
        self.__mtxMinPegRatio.SetValue("")
        self.__mtxMaxPriceSales.SetValue("")
        self.__mtxMinPriceSales.SetValue("")
        self.__mtxMaxPriceBook.SetValue("")
        self.__mtxMinPriceBook.SetValue("")
        self.__mtxMaxCompanyValueRevenue.SetValue("")
        self.__mtxMinCompanyValueRevenue.SetValue("")
        self.__mtxMaxCompanyValueEbitda.SetValue("")
        self.__mtxMinCompanyValueEbitda.SetValue("")

        self.__reset_info_bots_values()


    def __reset_info_bots_values(self):
        children = self.__mVerticalBoxBotInfos.GetChildren()
        for i in range(0, len(children)):
            children[i].GetWindow().SetLabel(Strings.STR_DATA_MAKING_BOT[i].format(""))
            children[i].GetWindow().SetForegroundColour(Colors.WHITE)
#endregion

#region - Save Methods
    def __check_insert_values(self):
        check = True

        if self.__mtxName.IsEmpty():
            check = False
            super()._show_error_message(Strings.STR_ERROR, Strings.STR_MSG_ERROR_NO_NAME_INSERTED)
        else:
            data = TradingStrategy.get_stored_data()
            if data is not None and len(data) > 0:
                for d in data:
                    if d.get_name() == self.__mtxName.GetValue():
                        check = False
                        super()._show_error_message(Strings.STR_ERROR, Strings.STR_MSG_ERROR_NAME_ALREADY_PRESENT)
                        break
        
        return check

#endregion

#region - BoxSizer Day Change Methods
    def __get_boxsizer_day_change(self, panel):
        bsDayChange = wx.BoxSizer(wx.VERTICAL)
        bsDayChange.Add(self.__get_boxsizer_max_day_change(panel))
        bsDayChange.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsDayChange.Add(self.__get_boxsizer_min_day_change(panel))
        return bsDayChange

    def __get_boxsizer_max_day_change(self, panel):
        self.__mtxMaxDayChange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxDayChange = wx.BoxSizer(wx.VERTICAL)
        bsMaxDayChange.Add(wx.StaticText(panel, label = Strings.STR_MAX_DAY_CHANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxDayChange.Add(self.__mtxMaxDayChange, 0, wx.EXPAND)
        return bsMaxDayChange

    def __get_boxsizer_min_day_change(self, panel):
        self.__mtxMinDayChange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinDayChange = wx.BoxSizer(wx.VERTICAL)
        bsMinDayChange.Add(wx.StaticText(panel, label = Strings.STR_MIN_DAY_CHANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinDayChange.Add(self.__mtxMinDayChange, 0, wx.EXPAND)
        return bsMinDayChange
#endregion

#region - BoxSizer Market Cap Methods
    def __get_boxsizer_market_cap(self, panel):
        bsMarketCap = wx.BoxSizer(wx.VERTICAL)
        bsMarketCap.Add(self.__get_boxsizer_max_market_cap(panel))
        bsMarketCap.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsMarketCap.Add(self.__get_boxsizer_min_market_cap(panel))
        return bsMarketCap

    def __get_boxsizer_max_market_cap(self, panel):
        self.__mtxMaxMarketCap = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxMarketCap = wx.BoxSizer(wx.VERTICAL)
        bsMaxMarketCap.Add(wx.StaticText(panel, label = Strings.STR_MAX_MARKET_CAP, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxMarketCap.Add(self.__mtxMaxMarketCap, 0, wx.EXPAND)
        return bsMaxMarketCap

    def __get_boxsizer_min_market_cap(self, panel):
        self.__mtxMinMarketCap = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinMarketCap = wx.BoxSizer(wx.VERTICAL)
        bsMinMarketCap.Add(wx.StaticText(panel, label = Strings.STR_MIN_MARKET_CAP, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinMarketCap.Add(self.__mtxMinMarketCap, 0, wx.EXPAND)
        return bsMinMarketCap
#endregion

#region - BoxSizer Day Range Methods
    def __get_boxsizer_day_range(self, panel):
        bsDayRange = wx.BoxSizer(wx.VERTICAL)
        bsDayRange.Add(self.__get_boxsizer_max_day_range(panel))
        bsDayRange.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsDayRange.Add(self.__get_boxsizer_min_day_range(panel))
        return bsDayRange

    def __get_boxsizer_max_day_range(self, panel):
        self.__mtxMaxDayRange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxDayRange = wx.BoxSizer(wx.VERTICAL)
        bsMaxDayRange.Add(wx.StaticText(panel, label = Strings.STR_MAX_DAY_RANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxDayRange.Add(self.__mtxMaxDayRange, 0, wx.EXPAND)
        return bsMaxDayRange

    def __get_boxsizer_min_day_range(self, panel):
        self.__mtxMinDayRange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinDayRange = wx.BoxSizer(wx.VERTICAL)
        bsMinDayRange.Add(wx.StaticText(panel, label = Strings.STR_MIN_DAY_RANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinDayRange.Add(self.__mtxMinDayRange, 0, wx.EXPAND)
        return bsMinDayRange
#endregion

#region - BoxSizer Week Range Methods
    def __get_boxsizer_week_range(self, panel):
        bsWeekRange = wx.BoxSizer(wx.VERTICAL)
        bsWeekRange.Add(self.__get_boxsizer_max_week_range(panel))
        bsWeekRange.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsWeekRange.Add(self.__get_boxsizer_min_week_range(panel))
        return bsWeekRange

    def __get_boxsizer_max_week_range(self, panel):
        self.__mtxMaxWeekRange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxWeekRange = wx.BoxSizer(wx.VERTICAL)
        bsMaxWeekRange.Add(wx.StaticText(panel, label = Strings.STR_MAX_WEEK_RANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxWeekRange.Add(self.__mtxMaxWeekRange, 0, wx.EXPAND)
        return bsMaxWeekRange

    def __get_boxsizer_min_week_range(self, panel):
        self.__mtxMinWeekRange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinWeekRange = wx.BoxSizer(wx.VERTICAL)
        bsMinWeekRange.Add(wx.StaticText(panel, label = Strings.STR_MIN_WEEK_RANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinWeekRange.Add(self.__mtxMinWeekRange, 0, wx.EXPAND)
        return bsMinWeekRange
#endregion

#region - BoxSizer Month Range Methods
    def __get_boxsizer_month_range(self, panel):
        bsMonthRange = wx.BoxSizer(wx.VERTICAL)
        bsMonthRange.Add(self.__get_boxsizer_max_month_range(panel))
        bsMonthRange.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsMonthRange.Add(self.__get_boxsizer_min_month_range(panel))
        return bsMonthRange

    def __get_boxsizer_max_month_range(self, panel):
        self.__mtxMaxMonthRange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxMonthRange = wx.BoxSizer(wx.VERTICAL)
        bsMaxMonthRange.Add(wx.StaticText(panel, label = Strings.STR_MAX_MONTH_RANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxMonthRange.Add(self.__mtxMaxMonthRange, 0, wx.EXPAND)
        return bsMaxMonthRange

    def __get_boxsizer_min_month_range(self, panel):
        self.__mtxMinMonthRange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinMonthRange = wx.BoxSizer(wx.VERTICAL)
        bsMinMonthRange.Add(wx.StaticText(panel, label = Strings.STR_MIN_MONTH_RANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinMonthRange.Add(self.__mtxMinMonthRange, 0, wx.EXPAND)
        return bsMinMonthRange
#endregion

#region - BoxSizer Year Range Methods
    def __get_boxsizer_year_range(self, panel):
        bsYearRange = wx.BoxSizer(wx.VERTICAL)
        bsYearRange.Add(self.__get_boxsizer_max_year_range(panel))
        bsYearRange.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsYearRange.Add(self.__get_boxsizer_min_year_range(panel))
        return bsYearRange

    def __get_boxsizer_max_year_range(self, panel):
        self.__mtxMaxYearRange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxYearRange = wx.BoxSizer(wx.VERTICAL)
        bsMaxYearRange.Add(wx.StaticText(panel, label = Strings.STR_MAX_YEAR_RANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxYearRange.Add(self.__mtxMaxYearRange, 0, wx.EXPAND)
        return bsMaxYearRange

    def __get_boxsizer_min_year_range(self, panel):
        self.__mtxMinYearRange = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinYearRange = wx.BoxSizer(wx.VERTICAL)
        bsMinYearRange.Add(wx.StaticText(panel, label = Strings.STR_MIN_YEAR_RANGE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinYearRange.Add(self.__mtxMinYearRange, 0, wx.EXPAND)
        return bsMinYearRange
#endregion

#region - BoxSizer Day Volume Methods
    def __get_boxsizer_day_volume(self, panel):
        bsDayVolume = wx.BoxSizer(wx.VERTICAL)
        bsDayVolume.Add(self.__get_boxsizer_max_day_volume(panel))
        bsDayVolume.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsDayVolume.Add(self.__get_boxsizer_min_day_volume(panel))
        return bsDayVolume

    def __get_boxsizer_max_day_volume(self, panel):
        self.__mtxMaxDayVolume = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxDayVolume = wx.BoxSizer(wx.VERTICAL)
        bsMaxDayVolume.Add(wx.StaticText(panel, label = Strings.STR_MAX_DAY_VOLUME, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxDayVolume.Add(self.__mtxMaxDayVolume, 0, wx.EXPAND)
        return bsMaxDayVolume

    def __get_boxsizer_min_day_volume(self, panel):
        self.__mtxMinDayVolume = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinDayVolume = wx.BoxSizer(wx.VERTICAL)
        bsMinDayVolume.Add(wx.StaticText(panel, label = Strings.STR_MIN_DAY_VOLUME, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinDayVolume.Add(self.__mtxMinDayVolume, 0, wx.EXPAND)
        return bsMinDayVolume
#endregion

#region - BoxSizer Company Value Methods
    def __get_boxsizer_company_value(self, panel):
        bsCompanyValue = wx.BoxSizer(wx.VERTICAL)
        bsCompanyValue.Add(self.__get_boxsizer_max_company_value(panel))
        bsCompanyValue.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsCompanyValue.Add(self.__get_boxsizer_min_company_value(panel))
        return bsCompanyValue

    def __get_boxsizer_max_company_value(self, panel):
        self.__mtxMaxCompanyValue = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxCompanyValue = wx.BoxSizer(wx.VERTICAL)
        bsMaxCompanyValue.Add(wx.StaticText(panel, label = Strings.STR_MAX_COMPANY_VALUE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxCompanyValue.Add(self.__mtxMaxCompanyValue, 0, wx.EXPAND)
        return bsMaxCompanyValue

    def __get_boxsizer_min_company_value(self, panel):
        self.__mtxMinCompanyValue = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinCompanyValue = wx.BoxSizer(wx.VERTICAL)
        bsMinCompanyValue.Add(wx.StaticText(panel, label = Strings.STR_MIN_COMPANY_VALUE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinCompanyValue.Add(self.__mtxMinCompanyValue, 0, wx.EXPAND)
        return bsMinCompanyValue
#endregion

#region - BoxSizer Ratio Company Value Market Cap Methods
    def __get_boxsizer_ratio_company_value_market_cap(self, panel):
        bsRatioCompanyValueMarketCap = wx.BoxSizer(wx.VERTICAL)
        bsRatioCompanyValueMarketCap.Add(self.__get_boxsizer_max_ratio_company_value_market_cap(panel))
        bsRatioCompanyValueMarketCap.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsRatioCompanyValueMarketCap.Add(self.__get_boxsizer_min_ratio_company_value_market_cap(panel))
        return bsRatioCompanyValueMarketCap

    def __get_boxsizer_max_ratio_company_value_market_cap(self, panel):
        self.__mtxMaxRatioCompanyValueMarketCap = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxRatioCompanyValueMarketCap = wx.BoxSizer(wx.VERTICAL)
        bsMaxRatioCompanyValueMarketCap.Add(wx.StaticText(panel, label = Strings.STR_MAX_RATIO_COMPANY_VALUE_MARKET_CAP, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxRatioCompanyValueMarketCap.Add(self.__mtxMaxRatioCompanyValueMarketCap, 0, wx.EXPAND)
        return bsMaxRatioCompanyValueMarketCap

    def __get_boxsizer_min_ratio_company_value_market_cap(self, panel):
        self.__mtxMinRatioCompanyValueMarketCap = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinRatioCompanyValueMarketCap = wx.BoxSizer(wx.VERTICAL)
        bsMinRatioCompanyValueMarketCap.Add(wx.StaticText(panel, label = Strings.STR_MIN_RATIO_COMPANY_VALUE_MARKET_CAP, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinRatioCompanyValueMarketCap.Add(self.__mtxMinRatioCompanyValueMarketCap, 0, wx.EXPAND)
        return bsMinRatioCompanyValueMarketCap
#endregion

#region - BoxSizer BETA Methods
    def __get_boxsizer_beta(self, panel):
        bsBeta = wx.BoxSizer(wx.VERTICAL)
        bsBeta.Add(self.__get_boxsizer_max_beta(panel))
        bsBeta.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsBeta.Add(self.__get_boxsizer_min_beta(panel))
        return bsBeta

    def __get_boxsizer_max_beta(self, panel):
        self.__mtxMaxBeta = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxBeta = wx.BoxSizer(wx.VERTICAL)
        bsMaxBeta.Add(wx.StaticText(panel, label = Strings.STR_MAX_BETA, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxBeta.Add(self.__mtxMaxBeta, 0, wx.EXPAND)
        return bsMaxBeta

    def __get_boxsizer_min_beta(self, panel):
        self.__mtxMinBeta = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinBeta = wx.BoxSizer(wx.VERTICAL)
        bsMinBeta.Add(wx.StaticText(panel, label = Strings.STR_MIN_BETA, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinBeta.Add(self.__mtxMinBeta, 0, wx.EXPAND)
        return bsMinBeta
#endregion

#region - BoxSizer Ratio PE Methods
    def __get_boxsizer_ratio_pe(self, panel):
        bsRatioPE = wx.BoxSizer(wx.VERTICAL)
        bsRatioPE.Add(self.__get_boxsizer_max_ratio_pe(panel))
        bsRatioPE.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsRatioPE.Add(self.__get_boxsizer_min_ratio_pe(panel))
        return bsRatioPE

    def __get_boxsizer_max_ratio_pe(self, panel):
        self.__mtxMaxRatioPE = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxRatioPE = wx.BoxSizer(wx.VERTICAL)
        bsMaxRatioPE.Add(wx.StaticText(panel, label = Strings.STR_MAX_RATIO_PE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxRatioPE.Add(self.__mtxMaxRatioPE, 0, wx.EXPAND)
        return bsMaxRatioPE

    def __get_boxsizer_min_ratio_pe(self, panel):
        self.__mtxMinRatioPE = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinRatioPE = wx.BoxSizer(wx.VERTICAL)
        bsMinRatioPE.Add(wx.StaticText(panel, label = Strings.STR_MIN_RATIO_PE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinRatioPE.Add(self.__mtxMinRatioPE, 0, wx.EXPAND)
        return bsMinRatioPE
#endregion

#region - BoxSizer EPS Methods
    def __get_boxsizer_eps(self, panel):
        bsEPS = wx.BoxSizer(wx.VERTICAL)
        bsEPS.Add(self.__get_boxsizer_max_eps(panel))
        bsEPS.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsEPS.Add(self.__get_boxsizer_min_eps(panel))
        return bsEPS

    def __get_boxsizer_max_eps(self, panel):
        self.__mtxMaxEPS = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxEPS = wx.BoxSizer(wx.VERTICAL)
        bsMaxEPS.Add(wx.StaticText(panel, label = Strings.STR_MAX_EPS, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxEPS.Add(self.__mtxMaxEPS, 0, wx.EXPAND)
        return bsMaxEPS

    def __get_boxsizer_min_eps(self, panel):
        self.__mtxMinEPS = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinEPS = wx.BoxSizer(wx.VERTICAL)
        bsMinEPS.Add(wx.StaticText(panel, label = Strings.STR_MIN_EPS, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinEPS.Add(self.__mtxMinEPS, 0, wx.EXPAND)
        return bsMinEPS
#endregion

#region - BoxSizer Year Target Methods
    def __get_boxsizer_year_target(self, panel):
        bsYearTarget = wx.BoxSizer(wx.VERTICAL)
        bsYearTarget.Add(self.__get_boxsizer_max_year_target(panel))
        bsYearTarget.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsYearTarget.Add(self.__get_boxsizer_min_year_target(panel))
        return bsYearTarget

    def __get_boxsizer_max_year_target(self, panel):
        self.__mtxMaxYearTarget = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxYearTarget = wx.BoxSizer(wx.VERTICAL)
        bsMaxYearTarget.Add(wx.StaticText(panel, label = Strings.STR_MAX_YEAR_TARGET, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxYearTarget.Add(self.__mtxMaxYearTarget, 0, wx.EXPAND)
        return bsMaxYearTarget

    def __get_boxsizer_min_year_target(self, panel):
        self.__mtxMinYearTarget = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinYearTarget = wx.BoxSizer(wx.VERTICAL)
        bsMinYearTarget.Add(wx.StaticText(panel, label = Strings.STR_MIN_YEAR_TARGET, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinYearTarget.Add(self.__mtxMinYearTarget, 0, wx.EXPAND)
        return bsMinYearTarget
#endregion

#region - BoxSizer Trailing PE Methods
    def __get_boxsizer_trailing_pe(self, panel):
        bsTrailingPE = wx.BoxSizer(wx.VERTICAL)
        bsTrailingPE.Add(self.__get_boxsizer_max_trailing_pe(panel))
        bsTrailingPE.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsTrailingPE.Add(self.__get_boxsizer_min_trailing_pe(panel))
        return bsTrailingPE

    def __get_boxsizer_max_trailing_pe(self, panel):
        self.__mtxMaxTrailingPE = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxTrailingPE = wx.BoxSizer(wx.VERTICAL)
        bsMaxTrailingPE.Add(wx.StaticText(panel, label = Strings.STR_MAX_TRAILING_PE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxTrailingPE.Add(self.__mtxMaxTrailingPE, 0, wx.EXPAND)
        return bsMaxTrailingPE

    def __get_boxsizer_min_trailing_pe(self, panel):
        self.__mtxMinTrailingPE = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinTrailingPE = wx.BoxSizer(wx.VERTICAL)
        bsMinTrailingPE.Add(wx.StaticText(panel, label = Strings.STR_MIN_TRAILING_PE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinTrailingPE.Add(self.__mtxMinTrailingPE, 0, wx.EXPAND)
        return bsMinTrailingPE
#endregion

#region - BoxSizer Forward PE Methods
    def __get_boxsizer_forward_pe(self, panel):
        bsForwardPE = wx.BoxSizer(wx.VERTICAL)
        bsForwardPE.Add(self.__get_boxsizer_max_forward_pe(panel))
        bsForwardPE.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsForwardPE.Add(self.__get_boxsizer_min_forward_pe(panel))
        return bsForwardPE

    def __get_boxsizer_max_forward_pe(self, panel):
        self.__mtxMaxForwardPE = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxForwardPE = wx.BoxSizer(wx.VERTICAL)
        bsMaxForwardPE.Add(wx.StaticText(panel, label = Strings.STR_MAX_FORWARD_PE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxForwardPE.Add(self.__mtxMaxForwardPE, 0, wx.EXPAND)
        return bsMaxForwardPE

    def __get_boxsizer_min_forward_pe(self, panel):
        self.__mtxMinForwardPE = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinForwardPE = wx.BoxSizer(wx.VERTICAL)
        bsMinForwardPE.Add(wx.StaticText(panel, label = Strings.STR_MIN_FORWARD_PE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinForwardPE.Add(self.__mtxMinForwardPE, 0, wx.EXPAND)
        return bsMinForwardPE
#endregion

#region - BoxSizer Peg Ratio Methods
    def __get_boxsizer_peg_ratio(self, panel):
        bsPegRatio = wx.BoxSizer(wx.VERTICAL)
        bsPegRatio.Add(self.__get_boxsizer_max_peg_ratio(panel))
        bsPegRatio.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsPegRatio.Add(self.__get_boxsizer_min_peg_ratio(panel))
        return bsPegRatio

    def __get_boxsizer_max_peg_ratio(self, panel):
        self.__mtxMaxPegRatio = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxPegRatio = wx.BoxSizer(wx.VERTICAL)
        bsMaxPegRatio.Add(wx.StaticText(panel, label = Strings.STR_MAX_PEG_RATIO, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxPegRatio.Add(self.__mtxMaxPegRatio, 0, wx.EXPAND)
        return bsMaxPegRatio

    def __get_boxsizer_min_peg_ratio(self, panel):
        self.__mtxMinPegRatio = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinPegRatio = wx.BoxSizer(wx.VERTICAL)
        bsMinPegRatio.Add(wx.StaticText(panel, label = Strings.STR_MIN_PEG_RATIO, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinPegRatio.Add(self.__mtxMinPegRatio, 0, wx.EXPAND)
        return bsMinPegRatio
#endregion

#region - BoxSizer Price Sales Methods
    def __get_boxsizer_price_sales(self, panel):
        bsPriceSales = wx.BoxSizer(wx.VERTICAL)
        bsPriceSales.Add(self.__get_boxsizer_max_price_sales(panel))
        bsPriceSales.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsPriceSales.Add(self.__get_boxsizer_min_price_sales(panel))
        return bsPriceSales

    def __get_boxsizer_max_price_sales(self, panel):
        self.__mtxMaxPriceSales = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxPriceSales = wx.BoxSizer(wx.VERTICAL)
        bsMaxPriceSales.Add(wx.StaticText(panel, label = Strings.STR_MAX_PRICE_SALES, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxPriceSales.Add(self.__mtxMaxPriceSales, 0, wx.EXPAND)
        return bsMaxPriceSales

    def __get_boxsizer_min_price_sales(self, panel):
        self.__mtxMinPriceSales = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinPriceSales = wx.BoxSizer(wx.VERTICAL)
        bsMinPriceSales.Add(wx.StaticText(panel, label = Strings.STR_MIN_PRICE_SALES, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinPriceSales.Add(self.__mtxMinPriceSales, 0, wx.EXPAND)
        return bsMinPriceSales
#endregion

#region - BoxSizer Price Book Methods
    def __get_boxsizer_price_book(self, panel):
        bsPriceBook = wx.BoxSizer(wx.VERTICAL)
        bsPriceBook.Add(self.__get_boxsizer_max_price_book(panel))
        bsPriceBook.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsPriceBook.Add(self.__get_boxsizer_min_price_book(panel))
        return bsPriceBook

    def __get_boxsizer_max_price_book(self, panel):
        self.__mtxMaxPriceBook = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxPriceBook = wx.BoxSizer(wx.VERTICAL)
        bsMaxPriceBook.Add(wx.StaticText(panel, label = Strings.STR_MAX_PRICE_BOOK, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxPriceBook.Add(self.__mtxMaxPriceBook, 0, wx.EXPAND)
        return bsMaxPriceBook

    def __get_boxsizer_min_price_book(self, panel):
        self.__mtxMinPriceBook = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinPriceBook = wx.BoxSizer(wx.VERTICAL)
        bsMinPriceBook.Add(wx.StaticText(panel, label = Strings.STR_MIN_PRICE_BOOK, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinPriceBook.Add(self.__mtxMinPriceBook, 0, wx.EXPAND)
        return bsMinPriceBook
#endregion

#region - BoxSizer Company Value Revenue Methods
    def __get_boxsizer_company_value_revenue(self, panel):
        bsCompanyValueRevenue = wx.BoxSizer(wx.VERTICAL)
        bsCompanyValueRevenue.Add(self.__get_boxsizer_max_company_value_revenue(panel))
        bsCompanyValueRevenue.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsCompanyValueRevenue.Add(self.__get_boxsizer_min_company_value_revenue(panel))
        return bsCompanyValueRevenue

    def __get_boxsizer_max_company_value_revenue(self, panel):
        self.__mtxMaxCompanyValueRevenue = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxCompanyValueRevenue = wx.BoxSizer(wx.VERTICAL)
        bsMaxCompanyValueRevenue.Add(wx.StaticText(panel, label = Strings.STR_MAX_COMPANY_VALUE_REVENUE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxCompanyValueRevenue.Add(self.__mtxMaxCompanyValueRevenue, 0, wx.EXPAND)
        return bsMaxCompanyValueRevenue

    def __get_boxsizer_min_company_value_revenue(self, panel):
        self.__mtxMinCompanyValueRevenue = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinCompanyValueRevenue = wx.BoxSizer(wx.VERTICAL)
        bsMinCompanyValueRevenue.Add(wx.StaticText(panel, label = Strings.STR_MIN_COMPANY_VALUE_REVENUE, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinCompanyValueRevenue.Add(self.__mtxMinCompanyValueRevenue, 0, wx.EXPAND)
        return bsMinCompanyValueRevenue
#endregion

#region - BoxSizer Company Value EBITDA Methods
    def __get_boxsizer_company_value_ebitda(self, panel):
        bsCompanyValueEbitda = wx.BoxSizer(wx.VERTICAL)
        bsCompanyValueEbitda.Add(self.__get_boxsizer_max_company_value_ebitda(panel))
        bsCompanyValueEbitda.AddSpacer(Sizes.SPACER_TRADING_BOT_PANEL_GRID)
        bsCompanyValueEbitda.Add(self.__get_boxsizer_min_company_value_ebitda(panel))
        return bsCompanyValueEbitda

    def __get_boxsizer_max_company_value_ebitda(self, panel):
        self.__mtxMaxCompanyValueEbitda = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMaxCompanyValueEbitda = wx.BoxSizer(wx.VERTICAL)
        bsMaxCompanyValueEbitda.Add(wx.StaticText(panel, label = Strings.STR_MAX_COMPANY_VALUE_EBITDA, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMaxCompanyValueEbitda.Add(self.__mtxMaxCompanyValueEbitda, 0, wx.EXPAND)
        return bsMaxCompanyValueEbitda

    def __get_boxsizer_min_company_value_ebitda(self, panel):
        self.__mtxMinCompanyValueEbitda = wx.TextCtrl(panel, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL, style = wx.TE_CENTRE)
        bsMinCompanyValueEbitda = wx.BoxSizer(wx.VERTICAL)
        bsMinCompanyValueEbitda.Add(wx.StaticText(panel, label = Strings.STR_MIN_COMPANY_VALUE_EBITDA, style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        bsMinCompanyValueEbitda.Add(self.__mtxMinCompanyValueEbitda, 0, wx.EXPAND)
        return bsMinCompanyValueEbitda
#endregion
#endregion