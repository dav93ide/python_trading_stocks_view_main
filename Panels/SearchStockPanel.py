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

        main.Add(vbs, 1, wx.ALL|wx.EXPAND)
        main.AddSpacer(25)
        self.SetSizer(main)

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

#region - Event Handler Methods
    def __on_change_text_check_is_int_value(self, evt):
        KeyboardEventUtils.on_change_text_check_is_int_value(self, evt)
#endregion