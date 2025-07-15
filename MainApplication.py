import wx, sys
from Frames.MainFrame import MainFrame
from Environment import Environment
from Utils.NetworkingUtils import NetworkingUtils
from Dialogs.ConfirmDialog import ConfirmDialog
from Resources.Strings import Strings

class MainApplication(wx.App):

    __mMainFrame: MainFrame = None
    __mDialog = None
    __mStarted = False

    def __init__(self, redirect):
        wx.App.__init__(self, redirect)

    def OnInit(self):
        self.__check_internet_connection()
        return True

    def OnExit(self):
        return 0

    def __check_internet_connection(self):
        if NetworkingUtils.check_internet_connection():
            if not self.__mStarted:
                self.__mStarted = True
                self.__mMainFrame = MainFrame()
                self.__mMainFrame.Show()
                self.SetTopWindow(self.__mMainFrame)
        else:
            self.__mDialog = ConfirmDialog(None, Strings.STR_ERROR_INTERNET_CONNECTION, Strings.STR_MSG_ERROR_INTERNET_CONNECTION, self.__on_confirm_internet_connection_check, self.__on_abort_internet_connection_check)
            self.__mDialog.Show()

    def __on_abort_internet_connection_check(self):
        self.__mDialog.Destroy()
        sys.exit(0)

    def __on_confirm_internet_connection_check(self):
        self.__mDialog.Destroy()
        self.__check_internet_connection()
