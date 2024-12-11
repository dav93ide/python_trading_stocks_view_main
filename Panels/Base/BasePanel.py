import wx, threading

class BasePanel(wx.Panel, threading.Thread):

    def __init__(self, parent, size):
        wx.Panel.__init__(self, parent, size = size)
        threading.Thread.__init__(self)
        self.Fit()

#region - Protected Methods
#region - BoxSizer Methods
    def _get_vbs_button(self, panel, text, f):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self._get_button(panel, text, f), 0, wx.EXPAND)
        return sizer

    def _get_hbs_button(self, panel, text, f):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self._get_button(panel, text, f), 0, wx.EXPAND)
        return sizer
#endregion
#region - Buttons Methods
    def _get_button(self, panel, text, f):
        button = wx.Button(panel, wx.ID_ANY, text)
        button.Bind(wx.EVT_BUTTON, f)
        return button
#endregion

#region - Message Methods
    def _show_error_message(self, title, msg):
        wx.MessageBox(msg, title, wx.OK | wx.ICON_ERROR)

    def _show_message(self, title, msg):
        wx.MessageBox(msg, title, wx.OK)
#endregion
#endregion