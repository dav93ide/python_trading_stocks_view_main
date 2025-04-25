import wx
import math
from Classes.Stock import Stock
from Classes.FilterClasses.FilterSearchStockPanel import FilterSearchStockPanel

class StocksViewList(wx.ListCtrl):

    LIST_COLUMNS = ["%", "Symbol", "Name", "Price", "Exchange"]
    LIST_COLUMNS_SIZES = [75, 75, 250, 100, 150]

    __mCallback = None
    __mFilterData = None
    __mFilterName = None
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

#region - Set Methods
    def set_filter_data(self, filter):
        self.__mFilterData = filter
#enderegion

#region - Public Methods
    def init_layout(self):
        for i in range(0, len(self.LIST_COLUMNS_SIZES)):
            self.InsertColumn(i, self.LIST_COLUMNS[i])
            self.SetColumnWidth(i, self.LIST_COLUMNS_SIZES[i])

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected)

    def add_items_and_populate(self, items):
        self.__mItems = items
        if self.__mFilterName is not None:
            self.filter_items()
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
        self.__mFilterName = ffilter
        filter_items()

    def filter_items(self):
        for item in self.__mItems:
            if item.get_market_change_percent() is None:
                    item.set_market_change_percent(0)
        self.filter_name()
        self.filter_order()
        self.filter_prices()

    def filter_name(self):
        if self.__mFilterName:
            self.__mFilteredItems = []
            for item in self.__mItems:
                if self.__mFilterName.lower() in item.get_sign().lower() or self.__mFilterName.lower() in item.get_company().get_name().lower() or self.__mFilterName.lower() in item.get_exchange().get_full_name().lower():
                    self.__mFilteredItems.append(item)
        else:
            self.__mFilteredItems = self.__mItems

    def filter_order(self):
        if self.__mFilterData.get_max_price_mover() is not None:
            items = []
            i = 1
            for item in self.__mFilteredItems:
                max = item
                for j in range(1, len(items)):
                    item = items[j]
                    if item.get_market_change_percent() > max.get_market_change_percent():
                        max = item
                print(max.get_name())
                items.append(max)
            if len(items) > 0:
                self.__mFilteredItems = items
        else:
            self.__mFilteredItems = self.__mItems

    def filter_prices(self):
        if self.__mFilterData is not None:
            items = []
            for item in self.__mFilteredItems:
                if self.__mFilterData.get_min_price() is not None:
                    if item.get_price() >= float(self.__mFilterData.get_min_price()):
                        items.append(item)

                if self.__mFilterData.get_max_price() is not None:
                    if item.get_price() <= float(self.__mFilterData.get_max_price()):
                        items.append(item)

                if self.__mFilterData.get_min_volume() is not None:
                    if item.get_volume() >= int(self.__mFilterData.get_min_volume()):
                        items.append(item)

                if self.__mFilterData.get_max_volume() is not None:
                    if item.get_volume <= int(self.__mFilterData.get_max_volume()):
                        items.append(item)

                if self.__mFilterData.get_mover_above_zero() is not None:
                    if item.get_market_change_percent() >= 0:
                        items.append(item)

                if self.__mFilterData.get_mover_above_fifty() is not None:
                    if item.get_market_change_percent() >= 50:
                        items.append(item)

                if self.__mFilterData.get_mover_above_hundred() is not None:
                    if item.get_market_change_percent() >= 100:
                        items.append(item)

                if self.__mFilterData.get_mover_below_zero() is not None:
                    if item.get_market_change_percent() <= 0:
                        items.append(item)

                if self.__mFilterData.get_mover_below_fifty() is not None:
                    if item.get_market_change_percent() <= -50:
                        items.append(item)

                if self.__mFilterData.get_mover_above_zero_to_ten() is not None:
                    if item.get_market_change_percent() >= 0 and item.get_market_change_percent() <= 10:
                        items.append(item)

                if self.__mFilterData.get_mover_above_ten_to_twenty() is not None:
                    if item.get_market_change_percent() >= 10 and item.get_market_change_percent() <= 20:
                        items.append(item)

                if self.__mFilterData.get_mover_above_twenty_to_thirty() is not None:
                    if item.get_market_change_percent() >= 20 and item.get_market_change_percent() <= 30:
                        items.append(item)

                if self.__mFilterData.get_mover_above_thirty_to_fourty() is not None:
                    if item.get_market_change_percent() >= 30 and item.get_market_change_percent() <= 40:
                        items.append(item)

                if self.__mFilterData.get_mover_below_zero_to_ten() is not None:
                    if item.get_market_change_percent() <= 0 and item.get_market_change_percent() >= -10:
                        items.append(item)

                if self.__mFilterData.get_mover_below_ten_to_twenty() is not None:
                    if item.get_market_change_percent() <= -10 and item.get_market_change_percent() >= -20:
                        items.append(item)

                if self.__mFilterData.get_mover_below_twenty_to_thirty() is not None:
                    if item.get_market_change_percent() <= -20 and item.get_market_change_percent() >= -30:
                        items.append(item)

                if self.__mFilterData.get_mover_below_thirty_to_fourty() is not None:
                    if item.get_market_change_percent() <= -30 and item.get_market_change_percent() >= -40:
                        items.append(item)

                if len(items) > 0:
                    self.__mFilteredItems = items
        else:
            self.__mFilteredItems = self.__mItems

        self.populate_list()

    def unbind_listener(self):
        self.Unbind(wx.EVT_LIST_ITEM_SELECTED)

    def bind_listener(self):
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected)
#endregion