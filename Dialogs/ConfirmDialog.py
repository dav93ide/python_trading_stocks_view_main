import wx
from Resources.Strings import Strings

class ConfirmDialog(wx.Dialog):

    __mMainPanel: wx.Panel = None

    __mTitle = None
    __mMessage = None

    __mCallback = None

    def __init__(self, parent, title, msg, callback):
        wx.Dialog.__init__(self, parent, title = title)
        self.__mMessage = msg
        self.__init_main_panel()
        self.__mCallback = callback

#region - Private Methods
#region - Init Methods
    def __init_main_panel(self):
        self.__mMainPanel = wx.Panel(self)

        vbs = wx.BoxSizer(wx.VERTICAL)
        vbs.AddSpacer(15)
        vbs.Add(wx.StaticText(self.__mMainPanel, label = self.__mMessage, style = wx.ALIGN_CENTRE), 1, wx.CENTER)
        vbs.AddSpacer(25)

        p = wx.Panel(self.__mMainPanel)
        p.SetBackgroundColour((0, 0, 0))
        hbs = wx.BoxSizer(wx.HORIZONTAL)
        hbs.Add(self.__get_button_abort(p), 1, wx.CENTER)
        hbs.AddSpacer(15)
        hbs.Add(self.__get_button_confirm(p), 1, wx.CENTER)
        p.SetSizer(hbs)
        p.Fit()
    
        vbs.Add(p, 1, wx.EXPAND)

        self.__mMainPanel.SetSizer(vbs)
        self.__mMainPanel.Fit()
        self.__mMainPanel.Update()
        self.__mMainPanel.SetAutoLayout(True)

    def __get_button_abort(self, panel):
        b = wx.Button(panel, wx.ID_ANY, Strings.STR_ABORT)
        b.Bind(wx.EVT_BUTTON, self.__on_click_abort)
        return b

    def __get_button_confirm(self, panel):
        b = wx.Button(panel, wx.ID_ANY, Strings.STR_CONFIRM)
        b.Bind(wx.EVT_BUTTON, self.__on_click_confirm)
        return b
#endregion

#region - Event Handler Methods
    def __on_click_abort(self, evt):
        self.Destroy()

    def __on_click_confirm(self, evt):
        self.__mCallback()
        self.Destroy()
#endregion
#endregion