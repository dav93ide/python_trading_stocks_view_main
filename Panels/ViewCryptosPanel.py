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
from Resources.Constants import Colors
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure
from Threads.StoppableThread import StoppableThread
from Networking.APIConstants import APIConstants

class ViewCryptosPanel(BasePanel):

    __mThreadUpdateGraph: StoppableThread = None

    __mbsMainBox = None
    __mMainSplitter = None
    __mLeftPanel = None
    __mRightPanel = None

    __mtxSearchList = None
    __mList = None

    __mBoxSizerData = None
    __msbCryptoImage = None
    __mstMarketPercentage = None

    __mDataPanel = None
    __mGraphsSizer = None

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
        self.Bind(wx.EVT_WINDOW_DESTROY, self.__on_destroy_self)
        self.__init_layout()

        # if crypto is not None:
        #     self.__on_click_item_list(crypto)

    def __init_threads(self):
        self.__mThreadUpdateGraph = StoppableThread(None, self.__update_graph_thread)

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

    def __init_left_panel(self):
        self.__mLeftPanel = wx.lib.scrolledpanel.ScrolledPanel(self.__mMainSplitter, wx.ID_ANY)
        self.__mLeftPanel.Fit()
        self.__mLeftPanel.SetupScrolling()
        self.__mLeftPanel.Layout()

#region - Event Handler Methods
    def __on_destroy_self(self, evt):
        self.__mThreadUpdateGraph.stop()

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
        frame = ViewStocksFrame(self.__mStockViewData.get_crypto().get_sign(), stocks, self.__mStockViewData.get_crypto())
        frame.Show()
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
        st = wx.StaticText(panel, label = self.__mStockViewData.get_crypto().get_sign(), style = wx.ALIGN_LEFT)
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
                self.__mGraphAxValues.set_title(Strings.STR_1D_VALUES)

                self.__mGraphAxVolume.clear()
                self.__mGraphAxVolume.stem(stockView.get_timestamps(), stockView.get_volumes())
                self.__mGraphAxVolume.set_title(Strings.STR_1D_VOLUME)

                self.__mGraphOneDayCanvas.draw()
                self.__mGraphOneDayCanvas.flush_events()
                
                if self.__mGraphOneDayPlot is not None:
                    self.__mGraphOneDayPlot.update_values_with_color(stockView.get_timestamps(), np.array(stockView.get_opens(), dtype=float), self.__mGraphLastColor)

            time.sleep(30)
#endregion