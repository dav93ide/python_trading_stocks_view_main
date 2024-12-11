import wx
from Classes.PlatformData import PlatformData
from Resources.Constants import *

class PlatformDataList(wx.ListCtrl):

    LIST_COLUMNS = ["Platform", "Name", "email", "Tot Capital", "Tot P/L", "Num Positions", "Num Bots"]

    __mItems: [PlatformData] = None
    __mWidth = None
    __mCurrentItem: PlatformData = None

    def __init__(self, parent, id, style, width):
        wx.ListCtrl.__init__(self, parent, id, style=style)
        self.__mWidth = width
        self.__mItems = []

#region - Get Methods
    def get_items(self):
        return self.__mItems

    def set_items(self, items):
        self.__mItems = items
#endregion

#region - Public Methods
    def add_item(self, item):
        self.__mItems.append(item)
        
    def init_layout(self):
        cWidth = self.__mWidth / len(self.LIST_COLUMNS)
        for i in range(0, len(self.LIST_COLUMNS)):
            self.InsertColumn(i, self.LIST_COLUMNS[i])
            self.SetColumnWidth(i, round(cWidth))

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected)

    def add_items_and_populate(self, items):
        self.__mItems = items
        self.populate_list()

    def populate_list(self):
        self.DeleteAllItems()
        if self.__mItems:
            for i in range(0, len(self.__mItems)):
                item = self.__mItems[i]
                self.InsertItem(i, str(item.get_type().name))
                self.SetItem(i, 1, item.get_name())
                self.SetItem(i, 2, item.get_email())
                self.SetItem(i, 3, str("%s $" % item.get_tot_capital_value()))
                self.SetItem(i, 4, str("%s" % item.get_tot_pl()))
                self.SetItem(i, 5, str(item.get_num_open_positions()))
                self.SetItem(i, 6, str(item.get_num_bots()))

    def on_item_selected(self, event):
        self.__mCurrentItem = event.Index
#endregion