import wx
import wx.lib.scrolledpanel
import wx.lib.agw.aui as aui
import wx.lib.mixins.inspection as wit
import time
import random
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure
from datetime import datetime
from threading import Thread
from Panels.Base.BasePanel import BasePanel
from Lists.StocksViewList import StocksViewList
from Classes.Stock import Stock
from Resources.Strings import Strings
from Resources.Constants import Sizes
from Resources.Constants import DataFilenames
from Resources.Constants import Icons
from Networking.DataSynchronization import DataSynchronization
from Utils.WxUtils import WxUtils
from Utils.TextUtils import TextUtils
from Utils.StoredDataUtils import StoredDataUtils
from Resources.Constants import Colors
from Utils.NumberUtils import NumberUtils
from Networking.APIConstants import APIConstants
from Frames.ChartFrame import ChartFrame
from Threads.StoppableThread import StoppableThread
from Frames.ViewStocksFrame import ViewStocksFrame

class ViewStocksPanel(BasePanel):

    __mbsMainBox: wx.BoxSizer = None
    __mbsRightListBox: wx.BoxSizer = None
    __mMainSplitter = None

    __mLeftPanel: wx.Panel = None
    __mRightPanel: wx.Panel = None
    __mDataPanel: wx.Panel = None

    __mBoxSizerData = None

    __mtxSearchList: wx.TextCtrl = None

    __mList: wx.ListCtrl = None

    __mGraphOneDayCanvas = None
    __mGraphAxValues = None
    __mGraphAxVolume = None

    __mGraphOneDayPlot = None

    __mstPrice = None
    __mstPrePostMarketPrice = None
    __mstMarketCap = None
    __mstDayMax = None
    __mstDayMin = None
    __mstAsk = None
    __mstBid = None
    __mstFiftyTwoWeeksHigh = None
    __mstFiftyTwoWeeksLow = None
    __mstFifityTwoWeeksPercChange = None
    __mstVolume = None
    __mstAvgVolumeTenDays = None
    __mstAvgVolumeThreeMonths = None

    __mThreadUpdateGraph: StoppableThread = None
    __mThreadUpdateList: StoppableThread = None
    __mThreadUpdateGraphPlotOneDay: StoppableThread = None

    __mTimerUpdateList = None
    __mTimerUpdateLeftPanel = None

    __mStockViewData = None

    __mGraphLastValue = None
    __mGraphLastColor = "b"

    __mIsShowingChart5d = False
    __mIsShowingChart1Mo = False
    __mIsShowingChart3Mo = False
    __mIsShowingChart6Mo = False
    __mIsShowingChart1Y = False
    __mIsShowingChart2Y = False
    __mIsShowingChart5Y = False
    __mIsShowingChart10Y = False
    __mIsShowingChartYTD = False
    __mIsShowingChartMax = False

    def __init__(self, parent, size, stock):
        super().__init__(parent, size)
        self.init_threads()
        self.Bind(wx.EVT_WINDOW_DESTROY, self.__on_destroy_self)
        self.__init_timers()
        self.__init_layout()
        
        if stock is not None:
            self.__on_click_item_list(stock)

#region - Private Methods
#region - Init Methods
    def init_threads(self):
        self.__mThreadUpdateGraph = StoppableThread(None, self.__update_graph_thread)
        self.__mThreadUpdateList = StoppableThread(None, self.__update_list_thread)

    def __init_timers(self):
        self.__mTimerUpdateList = wx.Timer(self, -1)
        self.__mTimerUpdateList.Start(20000)

        self.__mTimerUpdateLeftPanel = wx.Timer(self, -1)
        self.__mTimerUpdateLeftPanel.Start(20000)

        self.Bind(wx.EVT_TIMER, self.__repopulate_list, self.__mTimerUpdateList)
        self.Bind(wx.EVT_TIMER, self.__update_left_panel_data, self.__mTimerUpdateLeftPanel)

    def __init_layout(self):
        self.__mbsMainBox = wx.BoxSizer(wx.HORIZONTAL)

        self.__mbsMainBox.AddSpacer(10)
        self.__mMainSplitter = wx.SplitterWindow(self)
        self.__init_left_panel()
        self.__init_right_panel()
        self.__mMainSplitter.SplitVertically(self.__mLeftPanel, self.__mRightPanel, round((wx.DisplaySize()[0] / 10 * 7.5)))

        self.__mbsMainBox.Add(self.__mMainSplitter, 1, wx.EXPAND)
        self.__mbsMainBox.AddSpacer(10)
        self.SetSizer(self.__mbsMainBox)
        self.__mMainSplitter.Layout()
        self.__mLeftPanel.Layout()
        self.__mRightPanel.Layout()

    def __init_right_panel(self):
        self.__mRightPanel = wx.Panel(self.__mMainSplitter, wx.ID_ANY)
        self.__mRightPanel.SetBackgroundColour((66, 66, 66))
        
        main = wx.BoxSizer(wx.VERTICAL)
        
        vbs = wx.BoxSizer(wx.VERTICAL)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(15)
        hbs.Add(wx.StaticText(self.__mRightPanel, label = Strings.STR_SEARCH, style = wx.ALIGN_CENTRE), 0)
        vbs.Add(hbs, 0)

        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(15)
        self.__mtxSearchList = wx.TextCtrl(self.__mRightPanel, wx.ID_ANY, pos = wx.DefaultPosition, value = "", size = (500, 25))
        self.__mtxSearchList.Bind(wx.EVT_TEXT, self.__on_change_search_list_value)
        hbs.Add(self.__mtxSearchList, 1, wx.EXPAND)

        searchButton = super()._get_icon_button(self, wx.Bitmap(Icons.ICON_SEARCH), self.__on_click_search)
        hbs.Add(searchButton, 0, wx.EXPAND)

        vbs.Add(hbs, 0)

        main.Add(vbs, 0)
        main.AddSpacer(15)
        self.__mList = StocksViewList(self.__mRightPanel, wx.ID_ANY, wx.EXPAND|wx.LC_REPORT|wx.SUNKEN_BORDER, self.GetSize()[0], self.__on_click_item_list)
        main.Add(self.__mList, 1, wx.EXPAND)
        self.__mList.init_layout()
        self.__mList.add_items_and_populate(Stock.get_stored_data())

        self.__mRightPanel.SetSizer(main)
        self.__mRightPanel.Fit()

        if not self.__mThreadUpdateList.is_alive():
            self.__mThreadUpdateList.start()

    def __init_left_panel(self):
        self.__mLeftPanel = wx.lib.scrolledpanel.ScrolledPanel(self.__mMainSplitter, wx.ID_ANY)
        self.__mLeftPanel.Fit()
        self.__mLeftPanel.SetupScrolling()
#endregion

#region - Event Handler Methods
    def __on_destroy_self(self, evt):
        self.__mTimerUpdateList.Stop()
        self.__mTimerUpdateLeftPanel.Stop()
        self.__mThreadUpdateGraph.stop()
        self.__mThreadUpdateList.stop()

    def __on_change_search_list_value(self, evt):
        self.__mList.filter_items(evt.GetString())

    def __on_click_item_list(self, item):
        self.__mStockViewData = DataSynchronization.sync_single_stock_full_data(item.get_id(), item.get_sign())
        self.__mIsShowingChart5d = False
        self.__mIsShowingChart1Mo = False
        self.__mIsShowingChart3Mo = False
        self.__mIsShowingChart6Mo = False
        self.__mIsShowingChart1Y = False
        self.__mIsShowingChart2Y = False
        self.__mIsShowingChart5Y = False
        self.__mIsShowingChart10Y = False
        self.__mIsShowingChartYTD = False
        self.__mIsShowingChartMax = False
        self.__update_left_panel()

    def __on_click_search(self, evt):
        print("SEARCH")

    def __on_click_five_day_chart(self, evt):
        if not self.__mIsShowingChart5d:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_5D, APIConstants.VALUE_1M)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_5D_VALUES, Strings.STR_5D_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart5d = True
        

    def __on_click_one_month_chart(self, evt):
        if not self.__mIsShowingChart1Mo:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_1MO, APIConstants.VALUE_5M)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_1MO_VALUES, Strings.STR_1MO_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart1Mo = True

    def __on_click_three_month_chart(self, evt):
        if not self.__mIsShowingChart3Mo:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_3MO, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_3MO_VALUES, Strings.STR_3MO_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart3Mo = True

    def __on_click_six_month_chart(self, evt):
        if not self.__mIsShowingChart6Mo:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_6MO, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_6MO_VALUES, Strings.STR_6MO_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart6Mo = True

    def __on_click_one_year_chart(self, evt):
        if not self.__mIsShowingChart1Y:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_1Y, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_1Y_VALUES, Strings.STR_1Y_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart1Y = True

    def __on_click_two_year_chart(self, evt):
        if not self.__mIsShowingChart2Y:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_2Y, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_2Y_VALUES, Strings.STR_2Y_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart2Y = True

    def __on_click_five_year_chart(self, evt):
        if not self.__mIsShowingChart5Y:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_5Y, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_5Y_VALUES, Strings.STR_5Y_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart5Y = True

    def __on_click_ten_year_chart(self, evt):
        if not self.__mIsShowingChart10Y:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_10Y, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_10Y_VALUES, Strings.STR_10Y_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart10Y = True

    def __on_click_ytd_chart(self, evt):
        if not self.__mIsShowingChartYTD:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_YTD, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_YTD_VALUES, Strings.STR_YTD_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChartYTD = True

    def __on_click_max_chart(self, evt):
        if not self.__mIsShowingChartMax:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_MAX, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_MAX_VALUES, Strings.STR_MAX_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChartMax = True

    def __on_click_open_one_day_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_1D, APIConstants.VALUE_1M)
        self.__mGraphOneDayPlot = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        self.__mGraphOneDayPlot.Show(True)
        self.__mGraphOneDayPlot.Bind(wx.EVT_WINDOW_DESTROY, self.__on_destroy_graph_one_day_plot)

    def __on_click_open_five_day_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_5D, APIConstants.VALUE_1M)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)
        
    def __on_click_open_one_month_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_1MO, APIConstants.VALUE_5M)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_three_month_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_3MO, APIConstants.VALUE_1H)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_six_month_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_6MO, APIConstants.VALUE_1H)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_one_year_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_1Y, APIConstants.VALUE_1H)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_two_year_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_2Y, APIConstants.VALUE_1H)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_five_year_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_5Y, APIConstants.VALUE_1D)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_ten_year_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_10Y, APIConstants.VALUE_1D)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_ytd_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_YTD, APIConstants.VALUE_1H)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_max_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_MAX, APIConstants.VALUE_1D)
        cf = ChartFrame(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_in_new_window(self, evt):
        frame = ViewStocksFrame(self.__mStockViewData.get_stock().get_name(), self.__mStockViewData.get_stock())
        frame.Show()

    def __repopulate_list(self, event):
        list_total = self.__mList.GetItemCount()
        list_top = self.__mList.GetTopItem()
        list_pp = self.__mList.GetCountPerPage()
        list_bottom = min(list_top + list_pp, list_total - 1)
        self.__mList.add_items_and_populate(Stock.get_stored_data())
        if list_bottom != 0:
            self.__mList.EnsureVisible((list_bottom - 1))
        filtered = self.__mList.get_filtered_items()
        for i in range(0, len(filtered)):
            if self.__mStockViewData.get_stock().get_id() == filtered[i].get_id():
                self.__mList.unbind_listener()
                self.__mList.Select(i)
                self.__mList.bind_listener()
                break 
        
    def __update_left_panel_data(self, event):
        if self.__mStockViewData is not None:
            self.__mstPrice.SetLabel("$" + str(self.__mStockViewData.get_stock().get_price()))
            if self.__mStockViewData.get_stock().get_pre_market_price() is not None:
                self.__mstPrePostMarketPrice.SetLabel(Strings.STR_FIELD_PRE_MARKET + str(self.__mStockViewData.get_stock().get_pre_market_price()))
            else:
                if self.__mStockViewData.get_stock().get_post_market_price() is not None:
                    self.__mstPrePostMarketPrice.SetLabel(Strings.STR_FIELD_POST_MARKET + str(self.__mStockViewData.get_stock().get_pre_market_price()))
                else:
                    self.__mstPrePostMarketPrice.SetLabel("")
            self.__mstMarketCap.SetLabel(TextUtils.convert_number_to_millions_form(self.__mStockViewData.get_stock().get_market_cap()))
            self.__mstDayMax.SetLabel(str(self.__mStockViewData.get_stock().get_day_max()))
            self.__mstDayMin.SetLabel(str(self.__mStockViewData.get_stock().get_day_min()))
            self.__mstAsk.SetLabel(str(self.__mStockViewData.get_stock().get_ask()) + " x " + str(self.__mStockViewData.get_stock().get_ask_size() * 100))
            self.__mstBid.SetLabel(str(self.__mStockViewData.get_stock().get_bid()) + " x " + str(self.__mStockViewData.get_stock().get_bid_size() * 100))
            self.__mstFiftyTwoWeeksHigh.SetLabel(str(self.__mStockViewData.get_stock().get_fifty_two_weeks_high()))
            self.__mstFiftyTwoWeeksLow.SetLabel(str(self.__mStockViewData.get_stock().get_fifty_two_weeks_low()))
            self.__mstFifityTwoWeeksPercChange.SetLabel(str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_fifty_two_weeks_perc_change(), 2)))
            self.__mstVolume.SetLabel(str(self.__mStockViewData.get_stock().get_volume()))
            self.__mstAvgVolumeTenDays.SetLabel(str(self.__mStockViewData.get_stock().get_avg_volume_ten_days()))
            self.__mstAvgVolumeThreeMonths.SetLabel(str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_avg_volume_three_months(), 2)))

    def __on_destroy_graph_one_day_plot(self, event):
        self.__mGraphOneDayPlot = None
#endregion

#region - Thread Methods
    def __update_graph_thread(self):
        while not self.__mThreadUpdateGraph.stopped():
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_stock().get_sign(), APIConstants.VALUE_1D, APIConstants.VALUE_1M)
            opens = np.array(stockView.get_opens(), dtype=float)

            if self.__mGraphAxValues is not None and stockView.get_timestamps() is not None and len(stockView.get_timestamps()) > 0x0:
                self.__mGraphAxValues.clear()

                if self.__mGraphLastValue != opens[len(opens) - 1]:
                    if self.__mGraphLastValue <= opens[len(opens) - 1]:
                        self.__mGraphAxValues.plot(stockView.get_timestamps(), opens, "g")
                        self.__mGraphLastColor = "g"
                    else:
                        self.__mGraphAxValues.plot(stockView.get_timestamps(), opens, "r")
                        self.__mGraphLastColor = "r"
                else:
                    self.__mGraphAxValues.plot(stockView.get_timestamps(), opens, self.__mGraphLastColor)

                self.__mGraphAxValues.fill_between(stockView.get_timestamps(), min(opens), opens, alpha=0.5)
                self.__mGraphLastValue = opens[len(opens) - 1]

                self.__mGraphAxVolume.clear()
                self.__mGraphAxVolume.stem(stockView.get_timestamps(), stockView.get_volumes())

                self.__mGraphOneDayCanvas.draw()
                self.__mGraphOneDayCanvas.flush_events()
                
                if self.__mGraphOneDayPlot is not None:
                    self.__mGraphOneDayPlot.update_values_with_color(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float), self.__mGraphLastColor)

            time.sleep(30)

    def __update_list_thread(self):
        while not self.__mThreadUpdateList.stopped():
            DataSynchronization.sync_update_all_stocks()
            if self.__mStockViewData is not None:
                stock = StoredDataUtils.get_obj_from_id(self.__mStockViewData.get_stock().get_id(), Stock, DataFilenames.FILENAME_STOCK_DATA)
                self.__mStockViewData.set_stock(stock)
            time.sleep(30)
#endregion

#region - Get Layout Components
    def __update_left_panel(self):
        if self.__mBoxSizerData is not None:
            for child in self.__mBoxSizerData.GetChildren():
                if child is not None and child.Window is not None:
                    self.__mBoxSizerData.Hide(child.GetWindow())
                    self.__mBoxSizerData.Layout()
        self.__mBoxSizerData = wx.BoxSizer(wx.VERTICAL)
        self.__mBoxSizerData.Add(self.__get_layout_nome_azienda(), 0, wx.EXPAND)
        self.__mBoxSizerData.Add(self.__get_layout_data_one(), 1, wx.EXPAND|wx.ALL)
        self.__mLeftPanel.SetSizer(self.__mBoxSizerData)

        if self.__mIsShowingChart5d:
            self.__mIsShowingChart5d = False
            self.__on_click_five_day_chart(None)

        if self.__mIsShowingChart1Mo:
            self.__mIsShowingChart1Mo = False
            self.__on_click_one_month_chart(None)

        if self.__mIsShowingChart3Mo:
            self.__mIsShowingChart3Mo = False
            self.__on_click_three_month_chart(None)

        if self.__mIsShowingChart6Mo:
            self.__mIsShowingChart6Mo = False
            self.__on_click_six_month_chart(None)
        
        if self.__mIsShowingChart1Y:
            self.__mIsShowingChart1Y = False
            self.__on_click_one_year_chart(None)
        
        if self.__mIsShowingChart2Y:
            self.__mIsShowingChart2Y = False
            self.__on_click_two_year_chart(None)
        
        if self.__mIsShowingChart5Y:
            self.__mIsShowingChart5Y = False
            self.__on_click_five_year_chart(None)
        
        if self.__mIsShowingChart10Y:
            self.__mIsShowingChart10Y = False
            self.__on_click_ten_year_chart(None)
        
        if self.__mIsShowingChartYTD:
            self.__mIsShowingChartYTD = False
            self.__on_click_ytd_chart(None)
        
        if self.__mIsShowingChartMax:
            self.__mIsShowingChartMax = False
            self.__on_click_max_chart(None)

        if not self.__mThreadUpdateGraph.is_alive():
            self.__mThreadUpdateGraph.start()

    def __get_layout_nome_azienda(self):
        panel = wx.Panel(self.__mLeftPanel)
        panel.SetBackgroundColour((33, 33, 33))

        vbs = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(panel, label = self.__mStockViewData.get_stock().get_company().get_short_name(), style = wx.ALIGN_LEFT)
        WxUtils.set_font_size_and_bold_and_roman(st, 30)
        vbs.Add(st, 0, wx.EXPAND)

        hbs = wx.BoxSizer(wx.HORIZONTAL)
        self.__mstPrice = wx.StaticText(panel, label = "$" + str(self.__mStockViewData.get_stock().get_price()))
        WxUtils.set_font_size_and_bold_and_roman(self.__mstPrice, 20)
        hbs.Add(self.__mstPrice, 1, wx.EXPAND)
        
        if self.__mStockViewData.get_stock().get_pre_market_price() is not None:
            self.__mstPrePostMarketPrice = wx.StaticText(panel, label = Strings.STR_FIELD_PRE_MARKET + str(self.__mStockViewData.get_stock().get_pre_market_price()))
        else:
            if self.__mStockViewData.get_stock().get_post_market_price() is not None:
                self.__mstPrePostMarketPrice = wx.StaticText(panel, label = Strings.STR_FIELD_POST_MARKET + str(self.__mStockViewData.get_stock().get_pre_market_price()))
            else:
                self.__mstPrePostMarketPrice = wx.StaticText(panel, label = "")
        
        WxUtils.set_font_size_and_bold_and_roman(self.__mstPrePostMarketPrice, 20)
        hbs.Add(self.__mstPrePostMarketPrice, 0)
        vbs.Add(hbs, 0, wx.EXPAND)
        
        panel.SetSizer(vbs)
        return panel

    def __get_layout_data_one(self):
        self.__mDataPanel = wx.Panel(self.__mLeftPanel)
        self.__mDataPanel.SetBackgroundColour((66, 66, 66))
        vbs = wx.BoxSizer(wx.VERTICAL)
        vbs.AddSpacer(10)
        self.__mGraphsSizer = wx.BoxSizer(wx.VERTICAL)
        self.__mGraphsSizer.Add(self.__get_chart_row_thread_managed(self.__mDataPanel, Strings.STR_1D_VALUES, Strings.STR_1D_VOLUME, self.__mStockViewData.get_timestamps(), self.__mStockViewData.get_opens(), self.__mStockViewData.get_closes(), self.__mStockViewData.get_volumes()), 0, wx.EXPAND)
        vbs.Add(self.__mGraphsSizer, 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_zero_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_first_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_second_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_third_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_fourth_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_fifth_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_sixth_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_seventh_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_eigth_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_nineth_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_ten_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_eleven_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_twelve_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_thirteen_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_fourteen_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_fiveteen_row_info(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)


        self.__mDataPanel.SetSizer(vbs)
        return self.__mDataPanel

    def __get_chart_row_thread_managed(self, parent, label1, label2, timestamps, opens, closes, volumes):
        panel = wx.Panel(parent)
        self.fig = Figure(figsize=(2, 4))
        self.__mGraphOneDayCanvas = FigureCanvas(panel, -1, self.fig)
        toolbar = NavigationToolbar(self.__mGraphOneDayCanvas)
        toolbar.Realize()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.__mGraphOneDayCanvas, 1, wx.EXPAND)
        sizer.Add(toolbar, 0, wx.LEFT | wx.EXPAND)
        panel.SetSizer(sizer)

        timestamps = np.array(timestamps, dtype=str)
        opens = np.array(opens, dtype=float)
        volumes = np.array(volumes, dtype=float)

        (self.__mGraphAxValues, self.__mGraphAxVolume) = self.fig.subplots(1, 2)
        
        self.__mGraphAxValues.set_title(label1)
        if timestamps is not None and len(timestamps) > 0x0:
            self.__mGraphAxValues.plot(timestamps, opens)
            self.__mGraphAxValues.fill_between(timestamps, min(opens), opens, alpha=0.5)
            self.__mGraphLastValue = opens[len(opens) - 1]

        if timestamps is not None and len(timestamps) > 0x0:
            self.__mGraphAxVolume.set_title(label2)
            self.__mGraphAxVolume.stem(timestamps, volumes)

        return panel

    def __get_chart_row(self, parent, label1, label2, timestamps, opens, closes, volumes):
        panel = wx.Panel(parent)
        fig = Figure(figsize=(2, 4))
        canvas = FigureCanvas(panel, -1, fig)
        toolbar = NavigationToolbar(canvas)
        toolbar.Realize()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(canvas, 1, wx.EXPAND)
        sizer.Add(toolbar, 0, wx.LEFT | wx.EXPAND)
        panel.SetSizer(sizer)

        opens = np.array(opens, dtype=float)

        (ax1, ax2) = fig.subplots(1, 2)
        ax1.set_title(label1)
        ax1.plot(timestamps, opens)
        ax1.fill_between(timestamps, min(opens), opens, alpha=0.5)

        ax2.set_title(label2)
        ax2.stem(timestamps, volumes)

        return panel

    def __get_zero_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)
        
        st = wx.StaticText(panel, label = Strings.STR_FIELD_MARKET_CAP, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstMarketCap = wx.StaticText(panel, label = TextUtils.convert_number_to_millions_form(self.__mStockViewData.get_stock().get_market_cap()), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstMarketCap, 15)
        hbs.Add(self.__mstMarketCap, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_ENTERPRISE_VALUE, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = TextUtils.convert_number_to_millions_form(self.__mStockViewData.get_stock().get_enterprise_value()), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel


    def __get_first_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_DAY_MAX, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstDayMax = wx.StaticText(panel, label = str(self.__mStockViewData.get_stock().get_day_max()), style = wx.ALIGN_RIGHT)
        self.__mstDayMax.SetForegroundColour(Colors.GREEN)
        WxUtils.set_font_size(self.__mstDayMax, 15)
        hbs.Add(self.__mstDayMax, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_DAY_MIN, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstDayMin = wx.StaticText(panel, label = str(self.__mStockViewData.get_stock().get_day_min()), style = wx.ALIGN_RIGHT)
        self.__mstDayMin.SetForegroundColour(Colors.RED)
        WxUtils.set_font_size(self.__mstDayMin, 15)
        hbs.Add(self.__mstDayMin, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel
        
    def __get_second_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_ASK, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstAsk = wx.StaticText(panel, label = str(self.__mStockViewData.get_stock().get_ask()) + " x " + str(self.__mStockViewData.get_stock().get_ask_size() * 100), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstAsk, 15)
        hbs.Add(self.__mstAsk, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_BID, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstBid = wx.StaticText(panel, label = str(self.__mStockViewData.get_stock().get_bid()) + " x " + str(self.__mStockViewData.get_stock().get_bid_size() * 100), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstBid, 15)
        hbs.Add(self.__mstBid, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_SHARES_OUTSTANDING, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(self.__mStockViewData.get_stock().get_shares_outstanding()), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_third_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_52_WEEKS_MAX, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstFiftyTwoWeeksHigh = wx.StaticText(panel, label = str(self.__mStockViewData.get_stock().get_fifty_two_weeks_high()), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstFiftyTwoWeeksHigh, 15)
        self.__mstFiftyTwoWeeksHigh.SetForegroundColour(Colors.GREEN)
        hbs.Add(self.__mstFiftyTwoWeeksHigh, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_52_WEEKS_MIN, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstFiftyTwoWeeksLow = wx.StaticText(panel, label = str(self.__mStockViewData.get_stock().get_fifty_two_weeks_low()), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstFiftyTwoWeeksLow, 15)
        self.__mstFiftyTwoWeeksLow.SetForegroundColour(Colors.RED)
        hbs.Add(self.__mstFiftyTwoWeeksLow, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_52_WEEKS_PERC_CHANGE, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstFifityTwoWeeksPercChange = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_fifty_two_weeks_perc_change(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstFifityTwoWeeksPercChange, 15)
        if self.__mStockViewData.get_stock().get_fifty_two_weeks_perc_change() > 0:
            self.__mstFifityTwoWeeksPercChange.SetForegroundColour(Colors.GREEN)
        else:
            self.__mstFifityTwoWeeksPercChange.SetForegroundColour(Colors.RED)
        hbs.Add(self.__mstFifityTwoWeeksPercChange, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_fourth_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_VOLUME, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstVolume = wx.StaticText(panel, label = str(self.__mStockViewData.get_stock().get_volume()), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstVolume, 15)
        hbs.Add(self.__mstVolume, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_VOLUME_10_DAYS, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstAvgVolumeTenDays = wx.StaticText(panel, label = str(self.__mStockViewData.get_stock().get_avg_volume_ten_days()), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstAvgVolumeTenDays, 15)
        hbs.Add(self.__mstAvgVolumeTenDays, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_VOLUME_3_MONTHS, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstAvgVolumeThreeMonths = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_avg_volume_three_months(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstAvgVolumeThreeMonths, 15)
        hbs.Add(self.__mstAvgVolumeThreeMonths, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_fifth_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_TRAILING_PRICE_EARNINGS, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_trailing_price_earnings(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_FORWARD_PRICE_EARNINGS, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_forward_price_earnings(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_sixth_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_PE_RATIO, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_pe_ratio(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_PEG_RATIO, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_peg_ratio(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_PB_RATIO, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_pb_ratio(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_seventh_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_PRICE_TO_BOOK, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_price_to_book(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_BOOK_VALUE_PER_SHARE, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_book_value_per_share(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_eigth_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_DIVIDEND_DATE, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        if self.__mStockViewData.get_stock().get_dividend_date() is not None:
            st = wx.StaticText(panel, label = datetime.utcfromtimestamp(self.__mStockViewData.get_stock().get_dividend_date()).strftime('%d/%m/%Y'), style = wx.ALIGN_RIGHT)
            WxUtils.set_font_size(st, 15)
            hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_ANNUAL_DIVIDEND_RATE, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_trailing_annual_dividend_rate(), 3)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_ANNUAL_DIVIDEND_YELD, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_trailing_annual_dividend_yeld(), 5)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_nineth_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_RATIO_ENTERPRISE_VALUE_REVENUE, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_enterprises_value_revenue_ratio(), 3)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        hbs.AddSpacer(50)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_RATIO_ENTERPRISE_VALUE_EBITDA, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        st = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_stock().get_enterprises_value_ebitda_ratio(), 3)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_ten_row_info(self, parent):
        p = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open in New Window", self.__on_click_open_in_new_window), 1, wx.EXPAND)
        hbs.AddSpacer(10)

        p.SetSizer(hbs)
        return p

    def __get_eleven_row_info(self, parent):
        p = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "5D Chart", self.__on_click_five_day_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "1M Chart", self.__on_click_one_month_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "3M Chart", self.__on_click_three_month_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "6M Chart", self.__on_click_six_month_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "1y Chart", self.__on_click_one_year_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)

        p.SetSizer(hbs)
        return p

    def __get_twelve_row_info(self, parent):
        p = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)

        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "2y Chart", self.__on_click_two_year_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "5y Chart", self.__on_click_five_year_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "10y Chart", self.__on_click_ten_year_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "YTD Chart", self.__on_click_ytd_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Max Chart", self.__on_click_max_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)

        p.SetSizer(hbs)
        return p

    def __get_thirteen_row_info(self, parent):
        p = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open 1D Chart", self.__on_click_open_one_day_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open 5D Chart", self.__on_click_open_five_day_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open 1M Chart", self.__on_click_open_one_month_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open 3M Chart", self.__on_click_open_three_month_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)

        p.SetSizer(hbs)
        return p

    def __get_fourteen_row_info(self, parent):
        p = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open 6M Chart", self.__on_click_open_six_month_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open 1Y Chart", self.__on_click_open_one_year_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open 2Y Chart", self.__on_click_open_two_year_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open 5Y Chart", self.__on_click_open_five_year_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)

        p.SetSizer(hbs)
        return p

    def __get_fiveteen_row_info(self, parent):
        p = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open 10Y Chart", self.__on_click_open_ten_year_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open YTD Chart", self.__on_click_open_ytd_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open Max Chart", self.__on_click_open_max_chart), 1, wx.EXPAND)
        hbs.AddSpacer(10)

        p.SetSizer(hbs)
        return p

#endregion
#endregion