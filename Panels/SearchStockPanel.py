import wx
from Panels.Base.BasePanel import BasePanel
from Utils.KeyboardEventUtils import KeyboardEventUtils

class SearchStockPanel(BasePanel):

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

#region - Min Max Volume
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

#region - Min Max Movers / Volumes
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
        self.__mcbMaxMover = wx.CheckBox(panel, wx.ID_ANY, label = "Max Mover", style = wx.TE_CENTRE)
        self.__mcbMaxMover.Bind(wx. wxEVT_CHECKBOX, self.__on_check_max_mover)
        main.Add(self.__mcbMaxMover, 1, wx.EXPAND)

        self.__mcbMinMover = wx.CheckBox(panel, wx.ID_ANY, label = "Min Mover", style = wx.TE_CENTRE)
        self.__mcbMinMover.Bind(wx. wxEVT_CHECKBOX, self.__on_check_min_mover)
        main.Add(self.__mcbMinMover, 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel

    def __get_panel_min_max_volumes(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)
        self.__mcbMaxVolume = wx.CheckBox(panel, wx.ID_ANY, label = "Max Volume", style = wx.TE_CENTRE)
        self.__mcbMaxVolume.Bind(wx. wxEVT_CHECKBOX, self.__on_check_max_volume)
        main.Add(self.__mcbMaxVolume, 1, wx.EXPAND)

        self.__mcbMinVolume = wx.CheckBox(panel, wx.ID_ANY, label = "Min Volume", style = wx.TE_CENTRE)
        self.__mcbMinVolume.Bind(wx. wxEVT_CHECKBOX, self.__on_check_min_volume)
        main.Add(self.__mcbMinVolume, 1, wx.EXPAND)

        panel.SetSizer(main)
        return panel
#endregion

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
        self.__mcbMoverAboveZeroToTen = wx.CheckBox(panel, wx.ID_ANY, label = "+0% - 10%", style = wx.TE_CENTRE)
        self.__mcbMoverAboveZeroToTen.Bind(wx. wxEVT_CHECKBOX, self.__on_change_text_check_is_int_value)
        main.Add(self.__mcbMoverAboveZeroToTen, 1, wx.EXPAND)

        self.__mcbMoverAboveTenToTwenty = wx.CheckBox(panel, wx.ID_ANY, label = "+10% - 20%", style = wx.TE_CENTRE)
        self.__mcbMoverAboveTenToTwenty.Bind(wx. wxEVT_CHECKBOX, self.__on_change_text_check_is_int_value)
        main.Add(self.__mcbMoverAboveTenToTwenty, 1, wx.EXPAND)

        self.__mcbMoverAboveTwentyThirty = wx.CheckBox(panel, wx.ID_ANY, label = "+20% - 30%", style = wx.TE_CENTRE)
        self.__mcbMoverAboveTwentyThirty.Bind(wx. wxEVT_CHECKBOX, self.__on_change_text_check_is_int_value)
        main.Add(self.__mcbMoverAboveTwentyThirty, 1, wx.EXPAND)

        self.__mcbMoverAboveThirtyFourty = wx.CheckBox(panel, wx.ID_ANY, label = "+30% - 40%", style = wx.TE_CENTRE)
        self.__mcbMoverAboveThirtyFourty.Bind(wx. wxEVT_CHECKBOX, self.__on_change_text_check_is_int_value)
        main.Add(self.__mcbMoverAboveThirtyFourty, 1, wx.EXPAND)
        panel.SetSizer(main)
        return panel

    def __get_panel_one_percentage_below_movers(self, parent):
        panel = wx.Panel(parent)
        main = wx.BoxSizer(wx.HORIZONTAL)
        self.__mcbMoverBelowZeroToTen = wx.CheckBox(panel, wx.ID_ANY, label = "0% - -10%", style = wx.TE_CENTRE)
        self.__mcbMoverBelowZeroToTen.Bind(wx. wxEVT_CHECKBOX, self.__on_check_below_zero_to_ten)
        main.Add(self.__mcbMoverBelowZeroToTen, 1, wx.EXPAND)

        self.__mcbMoverBelowTenToTwenty = wx.CheckBox(panel, wx.ID_ANY, label = "-10% - -20%", style = wx.TE_CENTRE)
        self.__mcbMoverBelowTenToTwenty.Bind(wx. wxEVT_CHECKBOX, self.__on_check_below_ten_to_twenty)
        main.Add(self.__mcbMoverBelowTenToTwenty, 1, wx.EXPAND)

        self.__mcbMoverBelowTwentyThirty = wx.CheckBox(panel, wx.ID_ANY, label = "-20% - -30%", style = wx.TE_CENTRE)
        self.__mcbMoverBelowTwentyThirty.Bind(wx. wxEVT_CHECKBOX, self.__on_check_below_twenty_to_thirty)
        main.Add(self.__mcbMoverBelowTwentyThirty, 1, wx.EXPAND)

        self.__mcbMoverBelowThirtyFourty = wx.CheckBox(panel, wx.ID_ANY, label = "-30% - -40%", style = wx.TE_CENTRE)
        self.__mcbMoverBelowThirtyFourty.Bind(wx. wxEVT_CHECKBOX, self.__on_check_below_thirty_to_fourty)
        main.Add(self.__mcbMoverBelowThirtyFourty, 1, wx.EXPAND)
        panel.SetSizer(main)
        return panel
#endregion

#region - Event Handler Methods
    def __on_change_text_check_is_int_value(self, evt):
        KeyboardEventUtils.on_change_text_check_is_int_value(self, evt)

    def __on_check_max_mover(self, evt):
        print("Max Mover")

    def __on_check_min_mover(self, evt):
        print("Min Mover")

    def __on_check_max_volume(self, evt):
        print("Max Volume")

    def __on_check_min_volume(self, evt):
        print("Min Volume")

    def __on_check_above_zero_to_ten(self, evt):
        print("Above Zero to Ten")

    def __on_check_above_ten_to_twenty(self, evt):
        print("Above Ten To Twenty")

    def __on_check_above_twenty_to_thirty(self, evt):
        print("Above Twenty to Thirty")

    def __on_click_above_thirty_to_fourty(self, evt):
        print("Above Thirty to Fourty")

    def __on_check_below_zero_to_ten(self, evt):
        print("Below Zero to Ten")

    def __on_check_below_ten_to_twenty(self, evt):
        print("Below Ten to Twenty")

    def __on_check_below_twenty_to_thirty(self, evt):
        print("Below Twenty to Thirty")

    def __on_check_below_thirty_to_fourty(self, evt):
        print("Below Thirty to Fourty")
#endregion