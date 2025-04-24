import wx
from Panels.Base.BasePanel import BasePanel
from Utils.KeyboardEventUtils import KeyboardEventUtils
from Classes.FilterClasses.FilterSearchStockPanel import FilterSearchStockPanel
from Resources.Constants import Icons

class SearchStockPanel(BasePanel):

    __mtxMinPrice = None
    __mtxMaxPrice = None
    __mtxMinVolume = None
    __mtxMaxVolume = None

    __mcbMaxPriceMover = None
    __mcbMinPriceMover = None
    __mcbMaxVolumeMover = None
    __mcbMinVolumeMover = None

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

    __mFilterSearchStockPanel = FilterSearchStockPanel()

    def __init__(self, parent, size):
        super().__init__(parent, size)
        self.__init_layout()

#region - Private Methods
    def __init_layout(self):
        main = wx.BoxSizer(wx.HORIZONTAL)
        main.AddSpacer(25)
        
        vbs = wx.BoxSizer(wx.VERTICAL)
        vbs.Add(self.__get_panels_min_max_price(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_min_max_volume(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_max_min_movers_volumes(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_one_percentage_movers(), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panels_two_percentage_movers(), 0, wx.EXPAND)
        vbs.AddSpacer(100)
        vbs.Add(self.__get_panel_buttons(), 0, wx.EXPAND)

        main.Add(vbs, 1, wx.ALL|wx.EXPAND)
        main.AddSpacer(25)
        self.SetSizer(main)

#region - Min Max Price Methods
    def __get_panels_min_max_price(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)
        main.Add(self.__get_panel_min_price(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_max_price(panel), 1, wx.EXPAND)
        panel.SetSizer(main)
        return panel

    def __get_panel_min_price(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)
        main.Add(wx.StaticText(panel, label = "Min Price", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMinPrice = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMinPrice.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMinPrice, 0, wx.EXPAND)
        panel.SetSizer(main)
        return panel

    def __get_panel_max_price(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)
        main.Add(wx.StaticText(panel, label = "Max Price", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMaxPrice = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMaxPrice.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMaxPrice, 0, wx.EXPAND)
        panel.SetSizer(main)
        return panel
#endregion

#region - Min Max Volume Methods
    def __get_panels_min_max_volume(self):
        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)
        main.Add(self.__get_panel_min_volume(panel), 1, wx.EXPAND)
        main.AddSpacer(25)
        main.Add(self.__get_panel_max_volume(panel), 1, wx.EXPAND)
        panel.SetSizer(main)
        return panel

    def __get_panel_min_volume(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)
        main.Add(wx.StaticText(panel, label = "Min Volume", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMinVolume = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMinVolume.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMinVolume, 0, wx.EXPAND)
        panel.SetSizer(main)
        return panel

    def __get_panel_max_volume(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.VERTICAL)
        main.Add(wx.StaticText(panel, label = "Max Volume", style = wx.ALIGN_CENTRE), 0, wx.EXPAND)
        self.__mtxMaxVolume = wx.TextCtrl(panel, wx.ID_ANY, value = "", style = wx.TE_CENTRE)
        self.__mtxMaxVolume.Bind(wx.EVT_CHAR, self.__on_change_text_check_is_int_value)
        main.Add(self.__mtxMaxVolume, 0, wx.EXPAND)
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

        self.__mcbMinPriceMover = wx.CheckBox(panel, wx.ID_ANY, label = "Min Mover")
        self.__mcbMinPriceMover.Bind(wx.EVT_CHECKBOX, self.__on_check_min_mover)
        main.Add(self.__mcbMinPriceMover, 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_min_max_volumes(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)
        self.__mcbMaxVolumeMover = wx.CheckBox(panel, wx.ID_ANY, label = "Max Volume")
        self.__mcbMaxVolumeMover.Bind(wx.EVT_CHECKBOX, self.__on_check_max_volume)
        main.Add(self.__mcbMaxVolumeMover, 1, wx.EXPAND)

        self.__mcbMinVolumeMover = wx.CheckBox(panel, wx.ID_ANY, label = "Min Volume")
        self.__mcbMinVolumeMover.Bind(wx.EVT_CHECKBOX, self.__on_check_min_volume)
        main.Add(self.__mcbMinVolumeMover, 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel
#endregion


#region - Percentage Above Below Movers Methods
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
        self.__mcbMoverAboveZero.Bind(wx.EVT_CHECKBOX, self.__on_check_above_fifty)
        main.Add(self.__mcbMoverAboveZero, 1, wx.EXPAND)

        self.__mcbMoverAboveFifty = wx.CheckBox(panel, wx.ID_ANY, label = "> 50% Movers")
        self.__mcbMoverAboveFifty.Bind(wx.EVT_CHECKBOX, self.__on_check_above_fifty)
        main.Add(self.__mcbMoverAboveFifty, 1, wx.EXPAND)

        self.__mcbMoverAboveHundred = wx.CheckBox(panel, wx.ID_ANY, label = ">100% Movers")
        self.__mcbMoverAboveHundred.Bind(wx.EVT_CHECKBOX, self.__on_check_above_hundred)
        main.Add(self.__mcbMoverAboveHundred, 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_one_percentage_below_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)
        self.__mcbMoverBelowZero = wx.CheckBox(panel, wx.ID_ANY, label = "< 0% Movers")
        self.__mcbMoverBelowZero.Bind(wx.EVT_CHECKBOX, self.__on_check_below_fifty)
        main.Add(self.__mcbMoverBelowZero, 1, wx.EXPAND)

        self.__mcbMoverBelowFifty = wx.CheckBox(panel, wx.ID_ANY, label = "< -50% Movers")
        self.__mcbMoverBelowFifty.Bind(wx.EVT_CHECKBOX, self.__on_check_below_fifty)
        main.Add(self.__mcbMoverBelowFifty, 1, wx.EXPAND)

        self.__mcbMoverBelowHundred = wx.CheckBox(panel, wx.ID_ANY, label = "< -100% Movers")
        self.__mcbMoverBelowHundred.Bind(wx.EVT_CHECKBOX, self.__on_check_below_hundred)
        main.Add(self.__mcbMoverBelowHundred, 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel
#endregion

#region - Percentage Above Below Movers Methods
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

        self.__mcbMoverAboveTenToTwenty = wx.CheckBox(panel, wx.ID_ANY, label = "+10% - 20%")
        self.__mcbMoverAboveTenToTwenty.Bind(wx.EVT_CHECKBOX, self.__on_check_above_ten_to_twenty)
        main.Add(self.__mcbMoverAboveTenToTwenty, 1, wx.EXPAND)

        self.__mcbMoverAboveTwentyThirty = wx.CheckBox(panel, wx.ID_ANY, label = "+20% - 30%")
        self.__mcbMoverAboveTwentyThirty.Bind(wx.EVT_CHECKBOX, self.__on_check_above_twenty_to_thirty)
        main.Add(self.__mcbMoverAboveTwentyThirty, 1, wx.EXPAND)

        self.__mcbMoverAboveThirtyFourty = wx.CheckBox(panel, wx.ID_ANY, label = "+30% - 40%")
        self.__mcbMoverAboveThirtyFourty.Bind(wx.EVT_CHECKBOX, self.__on_click_above_thirty_to_fourty)
        main.Add(self.__mcbMoverAboveThirtyFourty, 1, wx.EXPAND)
        panel.SetSizer(main)
        return panel

    def __get_panel_two_percentage_below_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)
        self.__mcbMoverBelowZeroToTen = wx.CheckBox(panel, wx.ID_ANY, label = "0% - -10%")
        self.__mcbMoverBelowZeroToTen.Bind(wx.EVT_CHECKBOX, self.__on_check_below_zero_to_ten)
        main.Add(self.__mcbMoverBelowZeroToTen, 1, wx.EXPAND)

        self.__mcbMoverBelowTenToTwenty = wx.CheckBox(panel, wx.ID_ANY, label = "-10% - -20%")
        self.__mcbMoverBelowTenToTwenty.Bind(wx.EVT_CHECKBOX, self.__on_check_below_ten_to_twenty)
        main.Add(self.__mcbMoverBelowTenToTwenty, 1, wx.EXPAND)

        self.__mcbMoverBelowTwentyThirty = wx.CheckBox(panel, wx.ID_ANY, label = "-20% - -30%")
        self.__mcbMoverBelowTwentyThirty.Bind(wx.EVT_CHECKBOX, self.__on_check_below_twenty_to_thirty)
        main.Add(self.__mcbMoverBelowTwentyThirty, 1, wx.EXPAND)

        self.__mcbMoverBelowThirtyFourty = wx.CheckBox(panel, wx.ID_ANY, label = "-30% - -40%")
        self.__mcbMoverBelowThirtyFourty.Bind(wx.EVT_CHECKBOX, self.__on_check_below_thirty_to_fourty)
        main.Add(self.__mcbMoverBelowThirtyFourty, 1, wx.EXPAND)
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
        searchButton.Bind(wx.EVT_BUTTON, self.__on_click_search)
        return panel
#endregion

#region - Event Handler Methods
    def __on_change_text_check_is_int_value(self, evt):
        KeyboardEventUtils.on_change_text_check_is_int_value(self, evt)

    def __on_check_max_mover(self, evt):
        __mFilterSearchStockPanel.set_min_price(evt.IsChecked)

    def __on_check_min_mover(self, evt):
        __mFilterSearchStockPanel.set_min_price_mover(evt.IsChecked)

    def __on_check_max_volume(self, evt):
        __mFilterSearchStockPanel.set_max_volume(evt.IsChecked)

    def __on_check_min_volume(self, evt):
        __mFilterSearchStockPanel.set_min_volume(evt.IsChecked)

    def __on_check_above_zero(self, evt):
        __mFilterSearchStockPanel.set_mover_above_zero(evt.IsChecked)

    def __on_check_above_fifty(self, evt):
        __mFilterSearchStockPanel.set_mover_above_fifty(evt.IsChecked)

    def __on_check_above_hundred(self, evt):
        __mFilterSearchStockPanel.set_mover_above_hundred(evt.IsChecked)

    def __on_check_below_zero(self, evt):
        __mFilterSearchStockPanel.set_mover_below_zero(evt.IsChecked)

    def __on_check_below_fifty(self, evt):
        __mFilterSearchStockPanel.set_mover_below_fifty(evt.IsChecked)

    def __on_check_below_hundred(self, evt):
        __mFilterSearchStockPanel.set_mover_below_hundred(evt.IsChecked)

    def __on_check_above_zero_to_ten(self, evt):
        __mFilterSearchStockPanel.set_mover_above_zero_to_ten(evt.IsChecked)

    def __on_check_above_ten_to_twenty(self, evt):
        __mFilterSearchStockPanel.set_mover_above_ten_to_twenty(evt.IsChecked)

    def __on_check_above_twenty_to_thirty(self, evt):
        __mFilterSearchStockPanel.set_mover_above_twenty_to_thirty(evt.IsChecked)

    def __on_click_above_thirty_to_fourty(self, evt):
        _+mFilterSearchStockPanel.set_mover_above_thirty_to_fourty(evt.IsChecked)

    def __on_check_below_zero_to_ten(self, evt):
        _mFilterSearchStockPanel.set_mover_below_zero_to_ten(evt.IsChecked)

    def __on_check_below_ten_to_twenty(self, evt):
        _mFilterSearchStockPanel.set_mover_below_ten_to_twenty(evt.IsChecked)

    def __on_check_below_twenty_to_thirty(self, evt):
        _mFilterSearchStockPanel.set_mover_below_twenty_to_thirty(evt.IsChecked)

    def __on_check_below_thirty_to_fourty(self, evt):
        _mFilterSearchStockPanel.set_mover_below_thirty_to_fourty(evt.IsChecked)

    def __on_click_search(self, evt):
        
#endregion