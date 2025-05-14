import wx
import io
import requests
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

class ViewCryptosPanel(BasePanel):

    __mThreadUpdateGraph = None

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

    __mGraphOneDayCanvas = None
    __mGraphAxValues = None
    __mGraphAxVolume = None
    __mGraphLastValue = None

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
        self.__update_left_panel()
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

        if not self.__mThreadUpdateGraph.is_alive():
            self.__mThreadUpdateGraph.start()

        self.__mLeftPanel.SetSizer(self.__mBoxSizerData)
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