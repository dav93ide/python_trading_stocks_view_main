import wx
from Frames.MainFrame import MainFrame
from Environment import Environment

class MainApplication(wx.App):

    __mMainFrame: MainFrame = None

    def __init__(self, redirect):
        wx.App.__init__(self, redirect)

    def OnInit(self):
        self.__mMainFrame = MainFrame()
        self.__mMainFrame.Show()
        self.SetTopWindow(self.__mMainFrame)
        return True

    def OnExit(self):
        return 0