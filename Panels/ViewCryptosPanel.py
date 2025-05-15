import wx
import io
import requests
import time
from Panels.Base.BasePanel import BasePanel
from Resources.Strings import Strings
from Resources.Constants import Icons
from Lists.CryptosViewList import CryptosViewList
from Networking.DataSynchronization import DataSynchronization
from Utils.WxUtils import WxUtils
from Utils.TextUtils import TextUtils
from Utils.NumberUtils import NumberUtils
from Resources.Constants import Colors
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure
from Threads.StoppableThread import StoppableThread
from Networking.APIConstants import APIConstants
from Frames.ViewCryptosFrame import ViewCryptosFrame
from Environment import Environment
from Frames.ChartFrame import ChartFrame

class ViewCryptosPanel(BasePanel):

    __mThreadUpdateGraph: StoppableThread = None
    __mThreadUpdateList: StoppableThread = None

    __mTimerUpdateList = None
    __mTimerUpdateLeftPanel = None

    __mbsMainBox = None
    __mMainSplitter = None
    __mLeftPanel = None
    __mRightPanel = None

    __mtxSearchList = None
    __mList = None

    __mDataPanel = None
    __mBoxSizerData = None
    __msbCryptoImage = None
    __mGraphsSizer = None
    __mstMarketPercentage = None
    __mstMarketCap = None
    __mstDayMax = None
    __mstDayMin = None
    __mstFiftyTwoWeeksHigh = None
    __mstFiftyTwoWeeksLow = None
    __mstFifityTwoWeeksPercChange = None
    __mstVolume = None
    __mstVolumeTwentyFourHours = None
    __mstVolumeAllCurrencies = None

    __mGraphOneDayPlot = None
    __mGraphOneDayCanvas = None
    __mGraphLastColor = None
    __mGraphAxValues = None
    __mGraphAxVolume = None
    __mGraphLastValue = None

    __mIsShowingChart5d = None
    __mIsShowingChart1Mo = None
    __mIsShowingChart3Mo = None
    __mIsShowingChart6Mo = None
    __mIsShowingChart1Y = None
    __mIsShowingChart2Y = None
    __mIsShowingChart5Y = None
    __mIsShowingChart10Y = None
    __mIsShowingChartYTD = None
    __mIsShowingChartMax = None

    __mCryptos = None
    __mStockViewData = None

    def __init__(self, parent, size, cryptos, crypto):
        super().__init__(parent, size)
        self.__mCryptos = cryptos
        self.__init_threads()
        self.__init_timers()
        self.Bind(wx.EVT_WINDOW_DESTROY, self.__on_destroy_self)
        self.__init_layout()

        # if crypto is not None:
        #     self.__on_click_item_list(crypto)

    def __init_threads(self):
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

        searchButton = super()._get_icon_button(self.__mRightPanel, wx.Bitmap(Icons.ICON_SEARCH), self.__on_click_search)
        hbs.Add(searchButton, 0, wx.EXPAND)

        vbs.Add(hbs, 0)
        main.Add(vbs, 0)
        main.AddSpacer(15)
        self.__mList = CryptosViewList(self.__mRightPanel, wx.ID_ANY, wx.EXPAND|wx.LC_REPORT|wx.SUNKEN_BORDER, self.GetSize()[0], self.__on_click_item_list)
        main.Add(self.__mList, 1, wx.EXPAND)
        self.__mList.init_layout()

        if self.__mCryptos is None or len(self.__mCryptos) == 0x0:
            self.__mCryptos = DataSynchronization.sync_all_crypto()

        self.__mList.add_items_and_populate(self.__mCryptos)

        self.__mRightPanel.SetSizer(main)
        self.__mRightPanel.Fit()

        if not self.__mThreadUpdateList.is_alive():
            self.__mThreadUpdateList.start()

    def __init_left_panel(self):
        self.__mLeftPanel = wx.lib.scrolledpanel.ScrolledPanel(self.__mMainSplitter, wx.ID_ANY)
        self.__mLeftPanel.Fit()
        self.__mLeftPanel.SetupScrolling()
        self.__mLeftPanel.Layout()

#region - Event Handler Methods
    def __on_destroy_self(self, evt):
        self.__mTimerUpdateList.Stop()
        self.__mTimerUpdateLeftPanel.Stop()
        self.__mThreadUpdateGraph.stop()
        self.__mThreadUpdateList.stop()

    def __on_change_search_list_value(self, evt):
        self.__mList.filter_items_by_name(evt.GetString())

    def __on_click_search(self, evt):
        print("Search")

    def __on_click_item_list(self, item):
        self.__mStockViewData = DataSynchronization.sync_single_crypto_full_data(item)
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

    def __on_click_five_day_chart(self, evt):
        if not self.__mIsShowingChart5d:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_5D, APIConstants.VALUE_1M)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_5D_VALUES, Strings.STR_5D_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart5d = True        

    def __on_click_one_month_chart(self, evt):
        if not self.__mIsShowingChart1Mo:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_1MO, APIConstants.VALUE_5M)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_1MO_VALUES, Strings.STR_1MO_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart1Mo = True

    def __on_click_three_month_chart(self, evt):
        if not self.__mIsShowingChart3Mo:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_3MO, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_3MO_VALUES, Strings.STR_3MO_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart3Mo = True

    def __on_click_six_month_chart(self, evt):
        if not self.__mIsShowingChart6Mo:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_6MO, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_6MO_VALUES, Strings.STR_6MO_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart6Mo = True

    def __on_click_one_year_chart(self, evt):
        if not self.__mIsShowingChart1Y:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_1Y, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_1Y_VALUES, Strings.STR_1Y_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart1Y = True

    def __on_click_two_year_chart(self, evt):
        if not self.__mIsShowingChart2Y:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_2Y, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_2Y_VALUES, Strings.STR_2Y_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart2Y = True

    def __on_click_five_year_chart(self, evt):
        if not self.__mIsShowingChart5Y:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_5Y, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_5Y_VALUES, Strings.STR_5Y_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart5Y = True

    def __on_click_ten_year_chart(self, evt):
        if not self.__mIsShowingChart10Y:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_10Y, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_10Y_VALUES, Strings.STR_10Y_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChart10Y = True

    def __on_click_ytd_chart(self, evt):
        if not self.__mIsShowingChartYTD:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_YTD, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_YTD_VALUES, Strings.STR_YTD_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChartYTD = True

    def __on_click_max_chart(self, evt):
        if not self.__mIsShowingChartMax:
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_MAX, APIConstants.VALUE_1D)
            self.__mGraphsSizer.Add(self.__get_chart_row(self.__mDataPanel, Strings.STR_MAX_VALUES, Strings.STR_MAX_VOLUME, stockView.get_timestamps(), stockView.get_opens(), stockView.get_closes(), stockView.get_volumes()), 0, wx.EXPAND)
            self.__mLeftPanel.SetupScrolling()
            self.__mIsShowingChartMax = True

    def __on_click_open_one_day_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_1D, APIConstants.VALUE_1M)
        self.__mGraphOneDayPlot = ChartFrame("One Day Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        self.__mGraphOneDayPlot.Show(True)
        self.__mGraphOneDayPlot.Bind(wx.EVT_WINDOW_DESTROY, self.__on_destroy_graph_one_day_plot)

    def __on_click_open_five_day_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_5D, APIConstants.VALUE_1M)
        cf = ChartFrame("Five Days Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)
        
    def __on_click_open_one_month_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_1MO, APIConstants.VALUE_5M)
        cf = ChartFrame("One Month Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_three_month_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_3MO, APIConstants.VALUE_1H)
        cf = ChartFrame("Three Months Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_six_month_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_6MO, APIConstants.VALUE_1H)
        cf = ChartFrame("Six Months Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_one_year_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_1Y, APIConstants.VALUE_1H)
        cf = ChartFrame("One Year Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_two_year_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_2Y, APIConstants.VALUE_1H)
        cf = ChartFrame("Two Years Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_five_year_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_5Y, APIConstants.VALUE_1D)
        cf = ChartFrame("Five Years Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_ten_year_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_10Y, APIConstants.VALUE_1D)
        cf = ChartFrame("Ten Years Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_ytd_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_YTD, APIConstants.VALUE_1H)
        cf = ChartFrame("YTD Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_max_chart(self, evt):
        stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_MAX, APIConstants.VALUE_1D)
        cf = ChartFrame("Max Chart", stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float))
        cf.Show(True)

    def __on_click_open_in_new_window(self, evt):
        cryptos = []
        for c in self.__mCryptos:
            if c is not None:
                cryptos.append(c)
        frame = ViewCryptosFrame(self.__mStockViewData.get_crypto().get_sign(), cryptos, self.__mStockViewData.get_crypto())
        frame.Show()

    def __repopulate_list(self, event):
        list_total = self.__mList.GetItemCount()
        list_top = self.__mList.GetTopItem()
        list_pp = self.__mList.GetCountPerPage()
        list_bottom = min(list_top + list_pp, list_total - 1)
        self.__mList.populate_list()
        if list_bottom != 0:
            self.__mList.EnsureVisible((list_bottom - 1))
        filtered = self.__mList.get_filtered_items()
        if filtered is not None and len(filtered) > 0:
            for i in range(0, len(filtered)):
                if self.__mStockViewData is not None and self.__mStockViewData.get_crypto() is not None and self.__mStockViewData.get_crypto().get_sign() == filtered[i].get_sign():
                    self.__mList.unbind_listener()
                    self.__mList.Select(i)
                    self.__mList.bind_listener()
                    break
        self.__mLeftPanel.Layout()

    def __update_left_panel_data(self, event):
        if self.__mStockViewData is not None:
            self.__mstMarketPercentage.SetLabel(str(round(self.__mStockViewData.get_crypto().get_market_change_percent(), 2))  + "%")
            self.__mstPrice.SetLabel("$" + str(self.__mStockViewData.get_crypto().get_price()))
            self.__mstMarketCap.SetLabel(TextUtils.convert_number_to_millions_form(self.__mStockViewData.get_crypto().get_market_cap()))
            self.__mstDayMax.SetLabel(str(self.__mStockViewData.get_crypto().get_day_max()))
            self.__mstDayMin.SetLabel(str(self.__mStockViewData.get_crypto().get_day_min()))
            self.__mstFiftyTwoWeeksHigh.SetLabel(str(self.__mStockViewData.get_crypto().get_fifty_two_weeks_high()))
            self.__mstFiftyTwoWeeksLow.SetLabel(str(self.__mStockViewData.get_crypto().get_fifty_two_weeks_low()))
            self.__mstFifityTwoWeeksPercChange.SetLabel(str(NumberUtils.safe_round(self.__mStockViewData.get_crypto().get_fifty_two_weeks_perc_change(), 2)))
            self.__mstVolume.SetLabel(TextUtils.convert_number_with_commas_form(self.__mStockViewData.get_crypto().get_volume()))
            self.__mstVolumeTwentyFourHours.SetLabel(TextUtils.convert_number_with_commas_form(self.__mStockViewData.get_crypto().get_volume_twenty_four_hours()))
            self.__mstVolumeAllCurrencies.SetLabel(TextUtils.convert_number_with_commas_form(self.__mStockViewData.get_crypto().get_volume_all_currencies()))
            self.__mLeftPanel.Layout()

    def __on_destroy_graph_one_day_plot(self, event):
        self.__mGraphOneDayPlot = None
#endregion

#region - Private Methods
    def __update_left_panel(self):
        if self.__mBoxSizerData is not None:
            for child in self.__mBoxSizerData.GetChildren():
                if child is not None and child.Window is not None:
                    self.__mBoxSizerData.Hide(child.GetWindow())
                    self.__mBoxSizerData.Layout()
        self.__mBoxSizerData = wx.BoxSizer(wx.VERTICAL)

        self.__mBoxSizerData.Add(self.__get_layout_nome_crypto(), 0, wx.EXPAND)
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

        self.__mLeftPanel.Layout()

    def __get_layout_nome_crypto(self):
        panel = wx.Panel(self.__mLeftPanel)

        vbs = wx.BoxSizer(wx.VERTICAL)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        image = wx.ImageFromStream(io.BytesIO(requests.get(self.__mStockViewData.get_crypto().get_img_url()).content)).ConvertToBitmap()
        self.__msbCryptoImage = wx.StaticBitmap(panel, wx.ID_ANY, image, wx.DefaultPosition, wx.DefaultSize, 0)
        hbs.Add(self.__msbCryptoImage, 0, wx.EXPAND)
        hbs.AddSpacer(50)        
        st = wx.StaticText(panel, label = "(" + self.__mStockViewData.get_crypto().get_sign() + ")", style = wx.ALIGN_LEFT)
        WxUtils.set_font_size_and_bold_and_roman(st, 30)
        hbs.Add(st, 0, wx.EXPAND)
        hbs.AddSpacer(25)
        st = wx.StaticText(panel, label = self.__mStockViewData.get_crypto().get_name(), style = wx.ALIGN_LEFT)
        WxUtils.set_font_size_and_bold_and_roman(st, 30)
        hbs.Add(st, 0, wx.EXPAND)
        vbs.Add(hbs, 0, wx.EXPAND)

        hbs = wx.BoxSizer(wx.HORIZONTAL)
        self.__mstMarketPercentage = wx.StaticText(panel, label = str(round(self.__mStockViewData.get_crypto().get_market_change_percent(), 2))  + "%")
        WxUtils.set_font_size_and_bold_and_roman(self.__mstMarketPercentage, 20)
        if self.__mStockViewData.get_crypto().get_market_change_percent() is not None and self.__mStockViewData.get_crypto().get_market_change_percent() > 0:
            self.__mstMarketPercentage.SetForegroundColour(Colors.GREEN)
        else:
            self.__mstMarketPercentage.SetForegroundColour(Colors.RED)
        
        self.__mstPrice = wx.StaticText(panel, label = "$" + str(self.__mStockViewData.get_crypto().get_price()))
        WxUtils.set_font_size_and_bold_and_roman(self.__mstPrice, 20)
        hbs.Add(self.__mstPrice, 0, wx.EXPAND)
        hbs.AddSpacer(50)
        hbs.Add(self.__mstMarketPercentage, 1, wx.EXPAND)
        
        vbs.Add(hbs, 0, wx.EXPAND)
        panel.SetSizer(vbs)
        return panel

    def __get_layout_data_one(self):
        self.__mDataPanel = wx.Panel(self.__mLeftPanel)
        
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
        vbs.Add(self.__get_panel_open_in_new_window(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panel_one_charts(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panel_two_charts(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panel_three_charts(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panel_four_charts(self.__mDataPanel), 0, wx.EXPAND)
        vbs.AddSpacer(10)
        vbs.Add(self.__get_panel_five_charts(self.__mDataPanel), 0, wx.EXPAND)
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
        self.__mstMarketCap = wx.StaticText(panel, label = TextUtils.convert_number_to_millions_form(self.__mStockViewData.get_crypto().get_market_cap()), style = wx.ALIGN_RIGHT)
        font = WxUtils.set_font_size(self.__mstMarketCap, 15)
        hbs.Add(self.__mstMarketCap, 0, wx.ALL|wx.EXPAND)

        dc = wx.ScreenDC()
        dc.SetFont(font)
        w, h = dc.GetTextExtent(st.GetLabel() + self.__mstMarketCap.GetLabel())

        hbs.AddSpacer(350 - w)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_CIRCULATING_SUPPLY, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        if self.__mStockViewData.get_crypto().get_circulating_supply() is not None:
            st = wx.StaticText(panel, label = TextUtils.convert_number_to_millions_form(int(self.__mStockViewData.get_crypto().get_circulating_supply())), style = wx.ALIGN_RIGHT)
        else:
            st = wx.StaticText(panel, label = Strings.STR_UNDEFINED, style = wx.ALIGN_RIGHT)
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
        self.__mstDayMax = wx.StaticText(panel, label = str(self.__mStockViewData.get_crypto().get_day_max()), style = wx.ALIGN_RIGHT)
        self.__mstDayMax.SetForegroundColour(Colors.GREEN)
        font = WxUtils.set_font_size(self.__mstDayMax, 15)
        hbs.Add(self.__mstDayMax, 0, wx.ALL|wx.EXPAND)

        dc = wx.ScreenDC()
        dc.SetFont(font)
        w, h = dc.GetTextExtent(st.GetLabel() + self.__mstDayMax.GetLabel())

        hbs.AddSpacer(350 - w)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_DAY_MIN, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstDayMin = wx.StaticText(panel, label = str(self.__mStockViewData.get_crypto().get_day_min()), style = wx.ALIGN_RIGHT)
        self.__mstDayMin.SetForegroundColour(Colors.RED)
        WxUtils.set_font_size(self.__mstDayMin, 15)
        hbs.Add(self.__mstDayMin, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_second_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_52_WEEKS_MAX, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstFiftyTwoWeeksHigh = wx.StaticText(panel, label = str(self.__mStockViewData.get_crypto().get_fifty_two_weeks_high()), style = wx.ALIGN_RIGHT)
        font = WxUtils.set_font_size(self.__mstFiftyTwoWeeksHigh, 15)
        self.__mstFiftyTwoWeeksHigh.SetForegroundColour(Colors.GREEN)
        hbs.Add(self.__mstFiftyTwoWeeksHigh, 0, wx.ALL|wx.EXPAND)

        dc = wx.ScreenDC()
        dc.SetFont(font)
        w, h = dc.GetTextExtent(st.GetLabel() + self.__mstFiftyTwoWeeksHigh.GetLabel())

        hbs.AddSpacer(350 - w)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_52_WEEKS_MIN, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstFiftyTwoWeeksLow = wx.StaticText(panel, label = str(self.__mStockViewData.get_crypto().get_fifty_two_weeks_low()), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstFiftyTwoWeeksLow, 15)
        self.__mstFiftyTwoWeeksLow.SetForegroundColour(Colors.RED)
        hbs.Add(self.__mstFiftyTwoWeeksLow, 0, wx.ALL|wx.EXPAND)

        dc = wx.ScreenDC()
        dc.SetFont(font)
        w, h = dc.GetTextExtent(st.GetLabel() + self.__mstFiftyTwoWeeksLow.GetLabel())

        hbs.AddSpacer(350 - w)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_52_WEEKS_PERC_CHANGE, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstFifityTwoWeeksPercChange = wx.StaticText(panel, label = str(NumberUtils.safe_round(self.__mStockViewData.get_crypto().get_fifty_two_weeks_perc_change(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstFifityTwoWeeksPercChange, 15)
        if self.__mStockViewData.get_crypto().get_fifty_two_weeks_perc_change() > 0:
            self.__mstFifityTwoWeeksPercChange.SetForegroundColour(Colors.GREEN)
        else:
            self.__mstFifityTwoWeeksPercChange.SetForegroundColour(Colors.RED)
        hbs.Add(self.__mstFifityTwoWeeksPercChange, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_third_row_info(self, parent):
        panel = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.AddSpacer(10)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_VOLUME, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstVolume = wx.StaticText(panel, label = TextUtils.convert_number_with_commas_form(self.__mStockViewData.get_crypto().get_volume()), style = wx.ALIGN_RIGHT)
        font = WxUtils.set_font_size(self.__mstVolume, 15)
        hbs.Add(self.__mstVolume, 0, wx.ALL|wx.EXPAND)

        dc = wx.ScreenDC()
        dc.SetFont(font)
        w, h = dc.GetTextExtent(st.GetLabel() + self.__mstVolume.GetLabel())

        hbs.AddSpacer(350 - w)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_VOLUME_24H, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstVolumeTwentyFourHours = wx.StaticText(panel, label = TextUtils.convert_number_with_commas_form(self.__mStockViewData.get_crypto().get_volume_twenty_four_hours()), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstVolumeTwentyFourHours, 15)
        hbs.Add(self.__mstVolumeTwentyFourHours, 0, wx.ALL|wx.EXPAND)

        dc = wx.ScreenDC()
        dc.SetFont(font)
        w, h = dc.GetTextExtent(st.GetLabel() + self.__mstVolumeTwentyFourHours.GetLabel())

        hbs.AddSpacer(350 - w)

        st = wx.StaticText(panel, label = Strings.STR_FIELD_VOLUME_ALL_CURRENCIES, style = wx.ALIGN_LEFT)
        WxUtils.set_font_size(st, 15)
        hbs.Add(st, 0, wx.ALL|wx.EXPAND)
        hbs.AddSpacer(5)
        self.__mstVolumeAllCurrencies = wx.StaticText(panel, label = TextUtils.convert_number_with_commas_form(NumberUtils.safe_round(self.__mStockViewData.get_crypto().get_volume_all_currencies(), 2)), style = wx.ALIGN_RIGHT)
        WxUtils.set_font_size(self.__mstVolumeAllCurrencies, 15)
        hbs.Add(self.__mstVolumeAllCurrencies, 0, wx.ALL|wx.EXPAND)

        panel.SetSizer(hbs)
        return panel

    def __get_panel_open_in_new_window(self, parent):
        p = wx.Panel(parent)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        
        hbs.AddSpacer(10)
        hbs.Add(super()._get_button(p, "Open in New Window", self.__on_click_open_in_new_window), 1, wx.EXPAND)
        hbs.AddSpacer(10)

        p.SetSizer(hbs)
        return p

    def __get_panel_one_charts(self, parent):
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

    def __get_panel_two_charts(self, parent):
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

    def __get_panel_three_charts(self, parent):
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

    def __get_panel_four_charts(self, parent):
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

    def __get_panel_five_charts(self, parent):
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

#region - Thread Methods
    def __update_graph_thread(self):
        while not self.__mThreadUpdateGraph.stopped():
            stockView = DataSynchronization.sync_get_chart(self.__mStockViewData.get_crypto().get_sign(), APIConstants.VALUE_1D, APIConstants.VALUE_1M)
            opens = np.array(stockView.get_opens(), dtype=float)

            if self.__mGraphAxValues is not None and stockView.get_timestamps() is not None and len(stockView.get_timestamps()) > 0x0:
                self.__mGraphAxValues.clear()

                try:
                    if self.__mGraphLastValue != opens[len(opens) - 1]:
                        if self.__mGraphLastValue <= opens[len(opens) - 1]:
                            self.__mGraphAxValues.plot(stockView.get_timestamps(), opens, "g")
                            self.__mGraphLastColor = "g"
                        else:
                            self.__mGraphAxValues.plot(stockView.get_timestamps(), opens, "r")
                            self.__mGraphLastColor = "r"
                    else:
                        self.__mGraphAxValues.plot(stockView.get_timestamps(), opens, self.__mGraphLastColor)
                except:
                    Environment().get_logger().error(ViewCryptosPanel.__name__ + " - " + Strings.STR_ERROR_GRAPH)

                self.__mGraphAxValues.fill_between(stockView.get_timestamps(), min(opens), opens, alpha=0.5)
                self.__mGraphLastValue = opens[len(opens) - 1]
                self.__mGraphAxValues.set_title(Strings.STR_1D_VALUES)

                self.__mGraphAxVolume.clear()
                self.__mGraphAxVolume.stem(stockView.get_timestamps(), stockView.get_volumes())
                self.__mGraphAxVolume.set_title(Strings.STR_1D_VOLUME)

                self.__mGraphOneDayCanvas.draw()
                self.__mGraphOneDayCanvas.flush_events()
                
                if self.__mGraphOneDayPlot is not None:
                    self.__mGraphOneDayPlot.update_values_with_color(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float), self.__mGraphLastColor)

            time.sleep(30)

    def __update_list_thread(self):
        while not self.__mThreadUpdateList.stopped():
            list_top = self.__mList.GetTopItem()
            pos = self.__mList.get_filtered_item_position(list_top)
            list_pp = self.__mList.GetCountPerPage()
            cryptos = []
            filteredItems = self.__mList.get_filtered_items()
            if pos + list_pp <= len(filteredItems):
                for i in range(pos, pos + list_pp):
                    s = filteredItems[i]
                    if s is not None:
                        cryptos.append(s)
                cryptos = DataSynchronization.sync_update_all_cryptos(cryptos)
                self.__mList.add_specific_filtered_items(cryptos, list_top, pos + list_pp)
            else:
                for i in range(pos, len(filteredItems)):
                    s = filteredItems[i]
                    if s is not None:
                        cryptos.append(s)
                cryptos = DataSynchronization.sync_update_all_cryptos(cryptos)
                self.__mList.add_specific_filtered_items(cryptos, list_top, len(filteredItems))
            time.sleep(30)
#endregion