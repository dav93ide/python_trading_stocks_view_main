import wx, threading, Resources.Strings

class MainPanel(wx.Panel, threading.Thread):

    def __init__(self, parent, size):
        wx.Panel.__init__(self, parent, size=size)
        threading.Thread.__init__(self)

        self.size = size
        self.running = True
        self.__init_layout()

#region - Private Methods
    def __init_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(self, wx.ID_ANY, pos = wx.DefaultPosition, label = "PANNELLO PRINCIPALE", style = wx.ALIGN_CENTRE | wx.EXPAND), 0, wx.EXPAND)
#endregion