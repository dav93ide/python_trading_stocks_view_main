import wx
import json
from Panels.Base.BasePanel import BasePanel
from Utils.KeyboardEventUtils import KeyboardEventUtils
from Classes.FilterClasses.FilterSearchCryptoPanel import FilterSearchCryptoPanel
from Resources.Strings import Strings
from Utils.WxUtils import WxUtils
from Resources.Constants import Icons
from wx.lib.pubsub import pub 


LISTEN_FILTER_CRYPTO_PANEL = "ListenFiltersCryptoPanel"

class SearchCryptoPanel(BasePanel):

    __mMainSizer = None

    __mstCryptoData = None

    __mtxMinPrice = None
    __mtxMaxPrice = None
    __mtxMinVolume = None
    __mtxMaxVolume = None

    __mcbMaxPriceMover = None
    __mcbMinPriceMover = None
    __mcbMaxVolumeMover = None
    __mcbMinVolumeMover = None

    __mtxMaxValueMover = None
    __mtxMinValueMover = None

    __mcbMoverAboveZero = None
    __mcbMoverAboveFifty = None
    __mcbMoverAboveHundred = None
    __mcbMoverBelowZero = None
    __mcbMoverBelowFifty = None
    __mcbMoverBelowHundred = None

    __mcbMoverAboveZeroToTen = None
    __mcbMoverAboveTenToTwenty = None
    __mcbMoverAboveTwentyThirty = None
    __mcbMoverAboveThirtyFourty = None

    __mcbMoverBelowZeroToTen = None
    __mcbMoverBelowTenToTwenty = None
    __mcbMoverBelowTwentyThirty = None
    __mcbMoverBelowThirtyFourty = None

    __mstFiftyWeeksData = None

    __mtxFiftyMaxValueMover = None
    __mtxFiftyMinValueMover = None

    __mcbMoverFiftyWeeksAboveZero = None
    __mcbMoverFiftyWeeksAboveFifty = None
    __mcbMoverFiftyWeeksAboveHundred = None
    __mcbMoverFiftyWeeksBelowZero = None
    __mcbMoverFiftyWeeksBelowFifty = None

    __mcbMoverFiftyWeeksAboveZeroToTen = None
    __mcbMoverFiftyWeeksAboveTenToTwenty = None
    __mcbMoverFiftyWeeksAboveTwentyThirty = None
    __mcbMoverFiftyWeeksAboveThirtyFourty = None

    __mcbMoverFiftyWeeksBelowZeroToTen = None
    __mcbMoverFiftyWeeksBelowTenToTwenty = None
    __mcbMoverFiftyWeeksBelowTwentyThirty = None
    __mcbMoverFiftyWeeksBelowThirtyFourty = None


    __mFilterSearchCryptoPanel = FilterSearchCryptoPanel()

    def __init__(self, parent, size, filterData):
        super().__init__(parent, size)
        self.__mFilterSearchCryptoPanel = filterData
        self.__init_layout()

#region - Private Methods
    def __init_layout(self):
        self.__mMainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.__mMainSizer.AddSpacer(25)
        
        vbs = wx.BoxSizer(wx.VERTICAL)
        vbs.Add(self.__get_panel_text_crypto_data(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_min_max_price(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_min_max_volume(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_max_min_movers_volumes(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_values_max_min_mover(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_one_percentage_movers(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_two_percentage_movers(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panel_text_fifty_weeks_data(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_fifty_weeks_values_max_min_mover(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_two_fifty_weeks_percentage_movers(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_three_percentage_fifty_weeks_movers(), 0, wx.EXPAND)
        vbs.AddSpacer(100)
        vbs.Add(self.__get_panel_buttons(), 0, wx.EXPAND)

        self.__mMainSizer.Add(vbs, 1, wx.ALL|wx.EXPAND)
        self.__mMainSizer.AddSpacer(25)
        self.SetSizer(self.__mMainSizer)

#region - Header Crypto Data
    def __get_panel_text_crypto_data(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        self.__mstCryptoData = wx.StaticText(panel, label = Strings.STR_CRYPTO_DATA, style = wx.ALIGN_CENTRE_HORIZONTAL)
        WxUtils.set_font_size_and_bold_and_roman(self.__mstCryptoData, 15)
        main.Add(self.__mstCryptoData, 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel
#endregion

#region - Min Max Price Methods
    def __get_panels_min_max_price(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        main.Add(self.__get_panel_max_price(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_min_price(panel), 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_max_price(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(wx.StaticText(panel, label = "Max Price", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMaxPrice = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMaxPrice.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMaxPrice, 0, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_max_price():
            self.__mtxMaxPrice.SetValue(self.__mFilterSearchCryptoPanel.get_max_price())

        panel.SetSizer(main)
        return panel

    def __get_panel_min_price(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(wx.StaticText(panel, label = "Min Price", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMinPrice = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMinPrice.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMinPrice, 0, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_min_price():
            self.__mtxMinPrice.SetValue(self.__mFilterSearchCryptoPanel.get_min_price())

        panel.SetSizer(main)
        return panel
#endregion

#region - Min Max Volume Methods
    def __get_panels_min_max_volume(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        main.Add(self.__get_panel_max_volume(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_min_volume(panel), 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_max_volume(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(wx.StaticText(panel, label = "Max Volume", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMaxVolume = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMaxVolume.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMaxVolume, 0, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_max_volume():
            self.__mtxMaxVolume.SetValue(self.__mFilterSearchCryptoPanel.get_max_volume())

        panel.SetSizer(main)
        return panel

    def __get_panel_min_volume(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(wx.StaticText(panel, label = "Min Volume", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMinVolume = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMinVolume.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMinVolume, 0, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_min_volume():
            self.__mtxMinVolume.SetValue(self.__mFilterSearchCryptoPanel.get_min_volume())

        panel.SetSizer(main)
        return panel

#endregion

#region - Min Max Movers / Volumes Methods
    def __get_panels_max_min_movers_volumes(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        main.Add(self.__get_panel_min_max_movers(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_min_max_volumes(panel), 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_min_max_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)

        self.__mcbMaxPriceMover = wx.CheckBox(panel, wx.ID_ANY, label = "Max Mover")
        self.__mcbMaxPriceMover.Bind(wx.EVT_CHECKBOX, self.__on_check_max_mover)
        main.Add(self.__mcbMaxPriceMover, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_max_price_mover():
            self.__mcbMaxPriceMover.SetValue(True)

        self.__mcbMinPriceMover = wx.CheckBox(panel, wx.ID_ANY, label = "Min Mover")
        self.__mcbMinPriceMover.Bind(wx.EVT_CHECKBOX, self.__on_check_min_mover)
        main.Add(self.__mcbMinPriceMover, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_min_price_mover():
            self.__mcbMinPriceMover.SetValue(True)

        panel.SetSizer(main)
        return panel

    def __get_panel_min_max_volumes(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)

        self.__mcbMaxVolumeMover = wx.CheckBox(panel, wx.ID_ANY, label = "Max Volume")
        self.__mcbMaxVolumeMover.Bind(wx.EVT_CHECKBOX, self.__on_check_max_volume)
        main.Add(self.__mcbMaxVolumeMover, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_max_volume_mover():
            self.__mcbMaxVolumeMover.SetValue(True)

        self.__mcbMinVolumeMover = wx.CheckBox(panel, wx.ID_ANY, label = "Min Volume")
        self.__mcbMinVolumeMover.Bind(wx.EVT_CHECKBOX, self.__on_check_min_volume)
        main.Add(self.__mcbMinVolumeMover, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_min_volume_mover():
            self.__mcbMinVolumeMover.SetValue(True)

        panel.SetSizer(main)
        return panel
#endregion


#region - Percentage Above Below Movers Methods
    def __get_panels_values_max_min_mover(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        main.Add(self.__get_panel_value_max_mover(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_value_min_mover(panel), 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_value_max_mover(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(wx.StaticText(panel, label = "Max Value %", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMaxValueMover = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMaxValueMover.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMaxValueMover, 0, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_value_max_mover():
            self.__mtxMaxValueMover.SetValue(self.__mFilterSearchCryptoPanel.get_value_max_mover())

        panel.SetSizer(main)
        return panel

    def __get_panel_value_min_mover(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(wx.StaticText(panel, label = "Min Value %", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMinValueMover = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMinValueMover.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMinValueMover, 0, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_value_min_mover():
            self.__mtxMinValueMover.SetValue(self.__mFilterSearchCryptoPanel.get_value_min_mover())

        panel.SetSizer(main)
        return panel

    def __get_panels_one_percentage_movers(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        main.Add(self.__get_panel_one_percentage_above_movers(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_one_percentage_below_movers(panel), 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_one_percentage_above_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)
        self.__mcbMoverAboveZero = wx.CheckBox(panel, wx.ID_ANY, label = "> 0% Movers")
        self.__mcbMoverAboveZero.Bind(wx.EVT_CHECKBOX, self.__on_check_above_zero)
        main.Add(self.__mcbMoverAboveZero, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_above_zero():
            self.__mcbMoverAboveZero.SetValue(True)

        self.__mcbMoverAboveFifty = wx.CheckBox(panel, wx.ID_ANY, label = "> 50% Movers")
        self.__mcbMoverAboveFifty.Bind(wx.EVT_CHECKBOX, self.__on_check_above_fifty)
        main.Add(self.__mcbMoverAboveFifty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_above_fifty():
            self.__mcbMoverAboveFifty.SetValue(True)

        self.__mcbMoverAboveHundred = wx.CheckBox(panel, wx.ID_ANY, label = ">100% Movers")
        self.__mcbMoverAboveHundred.Bind(wx.EVT_CHECKBOX, self.__on_check_above_hundred)
        main.Add(self.__mcbMoverAboveHundred, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_above_hundred():
            self.__mcbMoverAboveHundred.SetValue(True)

        panel.SetSizer(main)
        return panel

    def __get_panel_one_percentage_below_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)
        self.__mcbMoverBelowZero = wx.CheckBox(panel, wx.ID_ANY, label = "< 0% Movers")
        self.__mcbMoverBelowZero.Bind(wx.EVT_CHECKBOX, self.__on_check_below_zero)
        main.Add(self.__mcbMoverBelowZero, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_below_zero():
            self.__mcbMoverBelowZero.SetValue(True)

        self.__mcbMoverBelowFifty = wx.CheckBox(panel, wx.ID_ANY, label = "< -50% Movers")
        self.__mcbMoverBelowFifty.Bind(wx.EVT_CHECKBOX, self.__on_check_below_fifty)
        main.Add(self.__mcbMoverBelowFifty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_below_fifty():
            self.__mcbMoverBelowFifty.SetValue(True)

        panel.SetSizer(main)
        return panel
#endregion

#region - Specific Percentage Above Below Movers Methods
    def __get_panels_two_percentage_movers(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        main.Add(self.__get_panel_two_percentage_above_movers(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_two_percentage_below_movers(panel), 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_two_percentage_above_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)

        self.__mcbMoverAboveZeroToTen = wx.CheckBox(panel, wx.ID_ANY, label = "+0% - 10%")
        self.__mcbMoverAboveZeroToTen.Bind(wx.EVT_CHECKBOX, self.__on_check_above_zero_to_ten)
        main.Add(self.__mcbMoverAboveZeroToTen, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_above_zero_to_ten():
            self.__mcbMoverAboveZeroToTen.SetValue(True)

        self.__mcbMoverAboveTenToTwenty = wx.CheckBox(panel, wx.ID_ANY, label = "+10% - 20%")
        self.__mcbMoverAboveTenToTwenty.Bind(wx.EVT_CHECKBOX, self.__on_check_above_ten_to_twenty)
        main.Add(self.__mcbMoverAboveTenToTwenty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_above_ten_to_twenty():
            self.__mcbMoverAboveTenToTwenty.SetValue(True)

        self.__mcbMoverAboveTwentyThirty = wx.CheckBox(panel, wx.ID_ANY, label = "+20% - 30%")
        self.__mcbMoverAboveTwentyThirty.Bind(wx.EVT_CHECKBOX, self.__on_check_above_twenty_to_thirty)
        main.Add(self.__mcbMoverAboveTwentyThirty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_above_twenty_to_thirty():
            self.__mcbMoverAboveTwentyThirty.SetValue(True)

        self.__mcbMoverAboveThirtyFourty = wx.CheckBox(panel, wx.ID_ANY, label = "+30% - 40%")
        self.__mcbMoverAboveThirtyFourty.Bind(wx.EVT_CHECKBOX, self.__on_check_above_thirty_to_fourty)
        main.Add(self.__mcbMoverAboveThirtyFourty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_above_thirty_to_fourty():
            self.__mcbMoverAboveThirtyFourty.SetValue(True)

        panel.SetSizer(main)
        return panel

    def __get_panel_two_percentage_below_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)
        self.__mcbMoverBelowZeroToTen = wx.CheckBox(panel, wx.ID_ANY, label = "0% - -10%")
        self.__mcbMoverBelowZeroToTen.Bind(wx.EVT_CHECKBOX, self.__on_check_below_zero_to_ten)
        main.Add(self.__mcbMoverBelowZeroToTen, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_below_zero_to_ten():
            self.__mcbMoverBelowZeroToTen.SetValue(True)

        self.__mcbMoverBelowTenToTwenty = wx.CheckBox(panel, wx.ID_ANY, label = "-10% - -20%")
        self.__mcbMoverBelowTenToTwenty.Bind(wx.EVT_CHECKBOX, self.__on_check_below_ten_to_twenty)
        main.Add(self.__mcbMoverBelowTenToTwenty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_below_ten_to_twenty():
            self.__mcbMoverBelowTenToTwenty.SetValue(True)

        self.__mcbMoverBelowTwentyThirty = wx.CheckBox(panel, wx.ID_ANY, label = "-20% - -30%")
        self.__mcbMoverBelowTwentyThirty.Bind(wx.EVT_CHECKBOX, self.__on_check_below_twenty_to_thirty)
        main.Add(self.__mcbMoverBelowTwentyThirty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_below_twenty_to_thirty():
            self.__mcbMoverBelowTwentyThirty.SetValue(True)

        self.__mcbMoverBelowThirtyFourty = wx.CheckBox(panel, wx.ID_ANY, label = "-30% - -40%")
        self.__mcbMoverBelowThirtyFourty.Bind(wx.EVT_CHECKBOX, self.__on_check_below_thirty_to_fourty)
        main.Add(self.__mcbMoverBelowThirtyFourty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_below_thirty_to_fourty():
            self.__mcbMoverBelowThirtyFourty.SetValue(True)

        panel.SetSizer(main)
        return panel
#endregion

#region - Percentage Above Below Movers Methods
    def __get_panel_text_fifty_weeks_data(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        self.__mstFiftyWeeksData = wx.StaticText(panel, label = Strings.STR_FIFTY_WEEKS_STOCK_DATA, style = wx.ALIGN_CENTRE_HORIZONTAL)
        WxUtils.set_font_size_and_bold_and_roman(self.__mstFiftyWeeksData, 15)
        main.Add(self.__mstFiftyWeeksData, 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panels_fifty_weeks_values_max_min_mover(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        main.Add(self.__get_panel_fifty_weeks_value_max_mover(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_fifty_weeks_value_min_mover(panel), 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_fifty_weeks_value_max_mover(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(wx.StaticText(panel, label = "52-Week Max Value %", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxFiftyMaxValueMover = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxFiftyMaxValueMover.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxFiftyMaxValueMover, 0, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_fifty_value_max_mover():
            self.__mtxFiftyMaxValueMover.SetValue(self.__mFilterSearchCryptoPanel.get_fifty_value_max_mover())

        panel.SetSizer(main)
        return panel

    def __get_panel_fifty_weeks_value_min_mover(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)

        main.Add(wx.StaticText(panel, label = "52-Week Min Value %", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxFiftyMinValueMover = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxFiftyMinValueMover.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxFiftyMinValueMover, 0, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_fifty_value_min_mover():
            self.__mtxFiftyMinValueMover.SetValue(self.__mFilterSearchCryptoPanel.get_fifty_value_min_mover())

        panel.SetSizer(main)
        return panel

#endregion

#region - Specific Percentage Above Below Movers Fifty Weeks Methods

    def __get_panels_two_fifty_weeks_percentage_movers(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        main.Add(self.__get_panel_two_fifty_weeks_percentage_above_movers(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_two_fifty_weeks_percentage_below_movers(panel), 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_two_fifty_weeks_percentage_above_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)

        self.__mcbMoverFiftyWeeksAboveZero = wx.CheckBox(panel, wx.ID_ANY, label = "> 0% Movers")
        self.__mcbMoverFiftyWeeksAboveZero.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_above_zero)
        main.Add(self.__mcbMoverFiftyWeeksAboveZero, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_above_zero():
            self.__mcbMoverFiftyWeeksAboveZero.SetValue(True)

        self.__mcbMoverFiftyWeeksAboveFifty = wx.CheckBox(panel, wx.ID_ANY, label = "> 50% Movers")
        self.__mcbMoverFiftyWeeksAboveFifty.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_above_fifty)
        main.Add(self.__mcbMoverFiftyWeeksAboveFifty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_above_fifty():
            self.__mcbMoverFiftyWeeksAboveFifty.SetValue(True)

        self.__mcbMoverFiftyWeeksAboveHundred = wx.CheckBox(panel, wx.ID_ANY, label = ">100% Movers")
        self.__mcbMoverFiftyWeeksAboveHundred.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_above_hundred)
        main.Add(self.__mcbMoverFiftyWeeksAboveHundred, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_above_hundred():
            self.__mcbMoverFiftyWeeksAboveHundred.SetValue(True)

        panel.SetSizer(main)
        return panel

    def __get_panel_two_fifty_weeks_percentage_below_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)

        self.__mcbMoverFiftyWeeksBelowZero = wx.CheckBox(panel, wx.ID_ANY, label = "< 0% Movers")
        self.__mcbMoverFiftyWeeksBelowZero.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_below_zero)
        main.Add(self.__mcbMoverFiftyWeeksBelowZero, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_below_zero():
            self.__mcbMoverFiftyWeeksBelowZero.SetValue(True)

        self.__mcbMoverFiftyWeeksBelowFifty = wx.CheckBox(panel, wx.ID_ANY, label = "< -50% Movers")
        self.__mcbMoverFiftyWeeksBelowFifty.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_below_fifty)
        main.Add(self.__mcbMoverFiftyWeeksBelowFifty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_below_fifty():
            self.__mcbMoverFiftyWeeksBelowFifty.SetValue(True)

        panel.SetSizer(main)
        return panel

    def __get_panels_three_percentage_fifty_weeks_movers(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        main.Add(self.__get_panels_three_percentage_fifty_weeks_above_movers(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panels_three_percentage_fifty_weeks_below_movers(panel), 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panels_three_percentage_fifty_weeks_above_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)

        self.__mcbMoverFiftyWeeksAboveZeroToTen = wx.CheckBox(panel, wx.ID_ANY, label = "+0% - 10%")
        self.__mcbMoverFiftyWeeksAboveZeroToTen.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_above_zero_to_ten)
        main.Add(self.__mcbMoverFiftyWeeksAboveZeroToTen, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_above_zero_to_ten():
            self.__mcbMoverFiftyWeeksAboveZeroToTen.SetValue(True)

        self.__mcbMoverFiftyWeeksAboveTenToTwenty = wx.CheckBox(panel, wx.ID_ANY, label = "+10% - 20%")
        self.__mcbMoverFiftyWeeksAboveTenToTwenty.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_above_ten_to_twenty)
        main.Add(self.__mcbMoverFiftyWeeksAboveTenToTwenty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_above_ten_to_twenty():
            self.__mcbMoverFiftyWeeksAboveTenToTwenty.SetValue(True)

        self.__mcbMoverFiftyWeeksAboveTwentyThirty = wx.CheckBox(panel, wx.ID_ANY, label = "+20% - 30%")
        self.__mcbMoverFiftyWeeksAboveTwentyThirty.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_above_twenty_to_thirty)
        main.Add(self.__mcbMoverFiftyWeeksAboveTwentyThirty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_above_twenty_to_thirty():
            self.__mcbMoverFiftyWeeksAboveTwentyThirty.SetValue(True)

        self.__mcbMoverFiftyWeeksAboveThirtyFourty = wx.CheckBox(panel, wx.ID_ANY, label = "+30% - 40%")
        self.__mcbMoverFiftyWeeksAboveThirtyFourty.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_above_thirty_to_fourty)
        main.Add(self.__mcbMoverFiftyWeeksAboveThirtyFourty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_above_thirty_to_fourty():
            self.__mcbMoverFiftyWeeksAboveThirtyFourty.SetValue(True)

        panel.SetSizer(main)
        return panel

    def __get_panels_three_percentage_fifty_weeks_below_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)

        self.__mcbMoverFiftyWeeksBelowZeroToTen = wx.CheckBox(panel, wx.ID_ANY, label = "0% - -10%")
        self.__mcbMoverFiftyWeeksBelowZeroToTen.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_below_zero_to_ten)
        main.Add(self.__mcbMoverFiftyWeeksBelowZeroToTen, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_below_zero_to_ten():
            self.__mcbMoverFiftyWeeksBelowZeroToTen.SetValue(True)

        self.__mcbMoverFiftyWeeksBelowTenToTwenty = wx.CheckBox(panel, wx.ID_ANY, label = "-10% - -20%")
        self.__mcbMoverFiftyWeeksBelowTenToTwenty.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_below_ten_to_twenty)
        main.Add(self.__mcbMoverFiftyWeeksBelowTenToTwenty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_below_ten_to_twenty():
            self.__mcbMoverFiftyWeeksBelowTenToTwenty.SetValue(True)

        self.__mcbMoverFiftyWeeksBelowTwentyThirty = wx.CheckBox(panel, wx.ID_ANY, label = "-20% - -30%")
        self.__mcbMoverFiftyWeeksBelowTwentyThirty.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_below_twenty_to_thirty)
        main.Add(self.__mcbMoverFiftyWeeksBelowTwentyThirty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_below_twenty_to_thirty():
            self.__mcbMoverFiftyWeeksBelowTwentyThirty.SetValue(True)

        self.__mcbMoverFiftyWeeksBelowThirtyFourty = wx.CheckBox(panel, wx.ID_ANY, label = "-30% - -40%")
        self.__mcbMoverFiftyWeeksBelowThirtyFourty.Bind(wx.EVT_CHECKBOX, self.__on_check_fifty_weeks_below_thirty_to_fourty)
        main.Add(self.__mcbMoverFiftyWeeksBelowThirtyFourty, 1, wx.EXPAND)
        if self.__mFilterSearchCryptoPanel.get_mover_fifty_weeks_below_thirty_to_fourty():
            self.__mcbMoverFiftyWeeksBelowThirtyFourty.SetValue(True)

        panel.SetSizer(main)
        return panel
#endregion

#region - Get Panel Filter
    def __get_panel_buttons(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        searchButton = super()._get_icon_button(panel, wx.Bitmap(Icons.ICON_SEARCH), self.__on_click_search)
        main.Add(searchButton, 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel
#endregion

#region - Event Handler Methods
    def __on_click_search(self, evt):
        self.__send_data()
        self.GetParent().Destroy()
        self.Layout()

    def __on_change_text_check_is_int_value(self, evt):
        if(KeyboardEventUtils.on_change_text_check_is_int_value(self, evt)):
            match evt.GetEventObject():
                case self.__mtxMinPrice:
                    self.__mFilterSearchCryptoPanel.set_min_price(self.__mtxMinPrice.GetValue())
                case self.__mtxMaxPrice:
                    self.__mFilterSearchCryptoPanel.set_max_price(self.__mtxMaxPrice.GetValue())
                case self.__mtxMinVolume:
                    self.__mFilterSearchCryptoPanel.set_min_volume(self.__mtxMinVolume.GetValue())
                case self.__mtxMaxVolume:
                    self.__mFilterSearchCryptoPanel.set_max_volume(self.__mtxMaxVolume.GetValue())
                case self.__mtxMaxValueMover:
                    self.__mFilterSearchCryptoPanel.set_value_max_mover(self.__mtxMaxValueMover.GetValue())
                case self.__mtxMinValueMover:
                    self.__mFilterSearchCryptoPanel.set_value_min_mover(self.__mtxMinValueMover.GetValue())
                case self.__mtxFiftyMaxValueMover:
                    self.__mFilterSearchCryptoPanel.set_fifty_value_max_mover(self.__mtxFiftyMaxValueMover.GetValue())
                case self.__mtxFiftyMinValueMover:
                    self.__mFilterSearchCryptoPanel.set_fifty_value_min_mover(self.__mtxFiftyMinValueMover.GetValue())

    def __on_check_max_mover(self, evt):
        self.__mFilterSearchCryptoPanel.set_max_price_mover(evt.IsChecked())
        self.__mFilterSearchCryptoPanel.set_min_price_mover(False)
        self.__mcbMinPriceMover.SetValue(False)
        self.__mcbMinVolumeMover.SetValue(False)
        self.__mcbMaxVolumeMover.SetValue(False)

    def __on_check_min_mover(self, evt):
        self.__mFilterSearchCryptoPanel.set_max_price_mover(False)
        self.__mFilterSearchCryptoPanel.set_min_price_mover(evt.IsChecked())
        self.__mcbMaxPriceMover.SetValue(False)
        self.__mcbMinVolumeMover.SetValue(False)
        self.__mcbMaxVolumeMover.SetValue(False)

    def __on_check_max_volume(self, evt):
        self.__mFilterSearchCryptoPanel.set_max_volume_mover(evt.IsChecked())
        self.__mFilterSearchCryptoPanel.set_min_volume_mover(False)
        self.__mcbMinVolumeMover.SetValue(False)
        self.__mcbMaxPriceMover.SetValue(False)
        self.__mcbMinPriceMover.SetValue(False)

    def __on_check_min_volume(self, evt):
        self.__mFilterSearchCryptoPanel.set_max_volume_mover(False)
        self.__mFilterSearchCryptoPanel.set_min_volume_mover(evt.IsChecked())
        self.__mcbMaxVolumeMover.SetValue(False)
        self.__mcbMaxPriceMover.SetValue(False)
        self.__mcbMinPriceMover.SetValue(False)

    def __on_check_above_zero(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_above_zero(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverAboveZero)

    def __on_check_above_fifty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_above_fifty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverAboveFifty)

    def __on_check_above_hundred(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_above_hundred(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverAboveHundred)

    def __on_check_below_zero(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_below_zero(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverBelowZero)

    def __on_check_below_fifty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_below_fifty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverBelowFifty)

    def __on_check_above_zero_to_ten(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_above_zero_to_ten(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverAboveZeroToTen)

    def __on_check_above_ten_to_twenty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_above_ten_to_twenty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverAboveTenToTwenty)

    def __on_check_above_twenty_to_thirty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_above_twenty_to_thirty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverAboveTwentyThirty)

    def __on_check_above_thirty_to_fourty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_above_thirty_to_fourty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverAboveThirtyFourty)

    def __on_check_below_zero_to_ten(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_below_zero_to_ten(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverBelowZeroToTen)

    def __on_check_below_ten_to_twenty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_below_ten_to_twenty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverBelowTenToTwenty)

    def __on_check_below_twenty_to_thirty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_below_twenty_to_thirty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverBelowTwentyThirty)

    def __on_check_below_thirty_to_fourty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_below_thirty_to_fourty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverBelowThirtyFourty)

    def __on_check_fifty_weeks_above_zero(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_above_zero(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksAboveZero)

    def __on_check_fifty_weeks_above_fifty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_above_fifty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksAboveFifty)

    def __on_check_fifty_weeks_above_hundred(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_above_hundred(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksAboveHundred)

    def __on_check_fifty_weeks_below_zero(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_below_zero(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksBelowZero)

    def __on_check_fifty_weeks_below_fifty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_below_fifty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksBelowFifty)

    def __on_check_fifty_weeks_above_zero_to_ten(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_above_zero_to_ten(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksAboveZeroToTen)

    def __on_check_fifty_weeks_above_ten_to_twenty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_above_ten_to_twenty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksAboveTenToTwenty)

    def __on_check_fifty_weeks_above_twenty_to_thirty(self, evt):   
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_above_twenty_to_thirty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksAboveTwentyThirty)

    def __on_check_fifty_weeks_above_thirty_to_fourty(self, evt):   
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_above_thirty_to_fourty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksAboveThirtyFourty)

    def __on_check_fifty_weeks_below_zero_to_ten(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_below_zero_to_ten(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksBelowZeroToTen)

    def __on_check_fifty_weeks_below_ten_to_twenty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_below_ten_to_twenty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksBelowTenToTwenty)

    def __on_check_fifty_weeks_below_twenty_to_thirty(self, evt):   
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_below_twenty_to_thirty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksBelowTwentyThirty)

    def __on_check_fifty_weeks_below_thirty_to_fourty(self, evt):
        self.__mFilterSearchCryptoPanel.set_all_to_false()
        self.__mFilterSearchCryptoPanel.set_mover_fifty_weeks_below_thirty_to_fourty(evt.IsChecked())
        self.__clear_checks(self.__mcbMoverFiftyWeeksBelowThirtyFourty)
#endregion

    def __clear_checks(self, obj):
        arr = [self.__mcbMoverAboveZero, self.__mcbMoverAboveFifty, self.__mcbMoverAboveHundred, self.__mcbMoverBelowZero,
            self.__mcbMoverBelowFifty, self.__mcbMoverAboveZeroToTen, self.__mcbMoverAboveTenToTwenty, self.__mcbMoverAboveTwentyThirty,
            self.__mcbMoverAboveThirtyFourty, self.__mcbMoverBelowZeroToTen, self.__mcbMoverBelowTenToTwenty, self.__mcbMoverBelowTwentyThirty,
            self.__mcbMoverBelowThirtyFourty, self.__mcbMoverFiftyWeeksAboveZero, self.__mcbMoverFiftyWeeksAboveFifty, self.__mcbMoverFiftyWeeksAboveHundred,
            self.__mcbMoverFiftyWeeksBelowZero, self.__mcbMoverFiftyWeeksBelowFifty, self.__mcbMoverFiftyWeeksAboveZeroToTen, self.__mcbMoverFiftyWeeksAboveTenToTwenty,
            self.__mcbMoverFiftyWeeksAboveTwentyThirty, self.__mcbMoverFiftyWeeksAboveThirtyFourty, self.__mcbMoverFiftyWeeksBelowZeroToTen, self.__mcbMoverFiftyWeeksBelowTenToTwenty,
            self.__mcbMoverFiftyWeeksBelowTwentyThirty, self.__mcbMoverFiftyWeeksBelowThirtyFourty]
        for a in arr:
            if a != obj:
                a.SetValue(False)

    def __send_data(self):
        j = json.dumps(self.__mFilterSearchCryptoPanel.to_dict())
        pub.sendMessage(LISTEN_FILTER_CRYPTO_PANEL, message = json.loads(j))
        self.GetParent().Destroy()