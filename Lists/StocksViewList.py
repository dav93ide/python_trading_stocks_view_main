import wx
import math
from Classes.Stock import Stock

class StocksViewList(wx.ListCtrl):

    LIST_COLUMNS = ["%", "Symbol", "Name", "Price", "Exchange"]
    LIST_COLUMNS_SIZES = [75, 75, 250, 100, 150]

    __mCallback = None
    __mFilter = None
    __mItems: [Stock] = None
    __mFilteredItems: [Stock] = None

    def __init__(self, parent, id, style, width, callback):
        wx.ListCtrl.__init__(self, parent, id, style=style)
        self.__mCallback = callback
        self.__mWidth = width
        self.__mItems = []

#region - Get Methods
    def get_items(self):
        return self.__mItems

    def set_items(self, items):
        self.__mItems = items

    def get_filtered_items(self):
        return self.__mFilteredItems

    def add_item(self, item):
        self.__mItems.append(item)
#endregion

#region - Public Methods
    def init_layout(self):
        for i in range(0, len(self.LIST_COLUMNS_SIZES)):
            self.InsertColumn(i, self.LIST_COLUMNS[i])
            self.SetColumnWidth(i, self.LIST_COLUMNS_SIZES[i])

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected)

    def add_items_and_populate(self, items):
        self.__mItems = items
        if self.__mFilter is not None:
            self.filter_items(self.__mFilter)
        else:
            self.__mFilteredItems = items
            self.populate_list()

    def populate_list(self):
        self.DeleteAllItems()
        if self.__mFilteredItems:
            for i in range(0, len(self.__mFilteredItems)):
                item = self.__mFilteredItems[i]
                if item.get_market_change_percent() is not None and item.get_market_change_percent() > 0:
                    self.InsertItem(i, "+" + str(round(item.get_market_change_percent(), 2)))
                else:
                    if item.get_market_change_percent() is not None:
                        self.InsertItem(i, str(round(item.get_market_change_percent(), 2)))
                    else:
                        self.InsertItem(i, str(0))
                self.SetItem(i, 1, str(item.get_sign()))
                self.SetItem(i, 2, str(item.get_company().get_name()))
                self.SetItem(i, 3, str(item.get_price()))
                if item.get_exchange():
                    self.SetItem(i, 4, str(item.get_exchange().get_full_name()))
                else:
                    self.SetItem(i, 4, "")

    def on_item_selected(self, event):
        if self.__mCallback is not None:
            self.__mCurrentItem = self.__mFilteredItems[event.Index]
            self.__mCallback(self.__mCurrentItem)

    def filter_items(self, ffilter):
        self.__mFilter = ffilter
        if ffilter:
            self.__mFilteredItems = []
            for item in self.__mItems:
                if ffilter.lower() in item.get_sign().lower() or ffilter.lower() in item.get_company().get_name().lower() or ffilter.lower() in item.get_exchange().get_full_name().lower():
                    self.__mFilteredItems.append(item)
        else:
            self.__mFilteredItems = self.__mItems
        self.populate_list()

    def unbind_listener(self):
        self.Unbind(wx.EVT_LIST_ITEM_SELECTED)

    def bind_listener(self):
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected)
#endregion