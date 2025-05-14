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

class ViewCryptosPanel(BasePanel):

    __mbsMainBox = None
    __mMainSplitter = None
    __mLeftPanel = None
    __mRightPanel = None

    __mBoxSizerData = None
    __msbCryptoImage = None
    __mstMarketPercentage = None

    __mtxSearchList = None
    __mList = None

    __mCryptos = None
    __mCrypto = None

    def __init__(self, parent, size, cryptos, crypto):
        super().__init__(parent, size)
        self.__mCryptos = cryptos
        self.__init_layout()

        # if crypto is not None:
        #     self.__on_click_item_list(crypto)


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
    def __on_change_search_list_value(self, evt):
        self.__mList.filter_items_by_name(evt.GetString())

    def __on_click_search(self, evt):
        print("Search")

    def __on_click_item_list(self, item):
        self.__mCrypto = item
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

    def __get_layout_nome_crypto(self):
        panel = wx.Panel(self.__mLeftPanel)

        vbs = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(panel, label = self.__mCrypto.get_sign(), style = wx.ALIGN_LEFT)
        WxUtils.set_font_size_and_bold_and_roman(st, 30)
        vbs.Add(st, 0, wx.EXPAND)

        image = wx.ImageFromStream(io.BytesIO(requests.get(self.__mCrypto.get_img_url()).content)).ConvertToBitmap()
        self.__msbCryptoImage = wx.StaticBitmap(panel, wx.ID_ANY, image, wx.DefaultPosition, wx.DefaultSize, 0)

        hbs.Add(self.__msbCryptoImage, 0, wx.EXPAND)
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        self.__mstMarketPercentage = wx.StaticText(panel, label = str(round(self.__mCrypto.get_market_change_percent(), 2))  + "%")
        WxUtils.set_font_size_and_bold_and_roman(self.__mstMarketPercentage, 20)
        if self.__mCrypto.get_market_change_percent() is not None and self.__mCrypto.get_market_change_percent() > 0:
            self.__mstMarketPercentage.SetForegroundColour(Colors.GREEN)
        else:
            self.__mstMarketPercentage.SetForegroundColour(Colors.RED)
        
        self.__mstPrice = wx.StaticText(panel, label = "$" + str(self.__mCrypto.get_price()))
        WxUtils.set_font_size_and_bold_and_roman(self.__mstPrice, 20)
        hbs.Add(self.__mstPrice, 0, wx.EXPAND)
        hbs.AddSpacer(50)
        hbs.Add(self.__mstMarketPercentage, 1, wx.EXPAND)
        
        vbs.Add(hbs, 1, wx.EXPAND)
        panel.SetSizer(vbs)
        return panel
#endregion