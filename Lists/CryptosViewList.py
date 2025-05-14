import wx
from Classes.Cryptocurrency import Cryptocurrency

class CryptosViewList(wx.ListCtrl):

    LIST_COLUMNS = ["%", "Symbol", "Name", "Price"]
    LIST_COLUMNS_SIZES = [75, 75, 250, 100]

    __mCallback = None
    __mFilterData = None
    __mFilterName = None
    __mItems: [Cryptocurrency] = None
    __mFilteredItems: [Cryptocurrency] = None

    def __init__(self, parent, id, style, width, callback):
        wx.ListCtrl.__init__(self, parent, id, style=style)
        self.__mCallback = callback
        self.__mWidth = width
        self.__mItems = []

#region - Public Methods
    def init_layout(self):
        for i in range(0, len(self.LIST_COLUMNS_SIZES)):
            self.InsertColumn(i, self.LIST_COLUMNS[i])
            self.SetColumnWidth(i, self.LIST_COLUMNS_SIZES[i])

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected)

    def add_items_and_populate(self, items):
        self.__mItems = items
        self.__mFilteredItems = items
        self.filter_items()
        self.populate_list()

    def populate_list(self):
        self.DeleteAllItems()
        if self.__mFilteredItems:
            for i in range(0, len(self.__mFilteredItems)):
                item = self.__mFilteredItems[i]
                if item.get_market_change_percent() is not None and float(item.get_market_change_percent()) > 0:
                    self.InsertItem(i, "+" + str(round(float(item.get_market_change_percent()), 2)))
                else:
                    if item.get_market_change_percent() is not None:
                        self.InsertItem(i, str(round(float(item.get_market_change_percent()), 2)))
                    else:
                        self.InsertItem(i, str(0))
                self.SetItem(i, 1, str(item.get_sign()))
                self.SetItem(i, 2, str(item.get_company().get_name()))
                self.SetItem(i, 3, str(item.get_price()))

    def on_item_selected(self, event):
        if self.__mCallback is not None:
            self.__mCurrentItem = self.__mFilteredItems[event.Index]
            self.__mCallback(self.__mCurrentItem)

    def filter_items_by_name(self, ffilter):
        self.__mFilterName = ffilter
        self.filter_items()

    def filter_items(self):
        for item in self.__mItems:
            if item.get_market_change_percent() is None:
                item.set_market_change_percent(0)
            if item.get_volume() is None:
                item.set_volume(0) 
        self.filter_name()
        if self.__mFilterData is not None:
            self.filter_values()
            self.filter_order()
        self.populate_list()

    def filter_order(self):
        print("Filter")

    def filter_values(self):
        print("Filter")
#endregion