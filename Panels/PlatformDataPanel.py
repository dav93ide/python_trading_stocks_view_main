import wx, threading, uuid
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN
from Resources.Strings import Strings
from Resources.Constants import Constants, Directories, Colors, Sizes, PlatformType, DataFilenames
from Lists.PlatformDataList import PlatformDataList
from Utils.RegexUtils import RegexUtils
from Utils.WxUtils import WxUtils
from Utils.StoredDataUtils import StoredDataUtils
from Utils.NumberUtils import NumberUtils
from Panels.Base.BasePanel import BasePanel
from Classes.PlatformData import PlatformData
from Classes.MainUser import MainUser
from Environment import Environment

CHECK_OK = True
CHECK_NOT_OK = False
CHECK_WRONG_MAIL = -0x1
CHECK_DIFFERENT_PASSWORDS = -0x2
CHECK_ALREADY_PRESENT = -0x3
CHECK_VAL_TO_HIGH = -0x4

class PlatformDataPanel(BasePanel):

    __mbsMainBox: wx.BoxSizer = None
    __mbsLeftDataBox: wx.BoxSizer = None
    __mgsTopDataGrid: wx.GridSizer = None
    __mgsBottomDataGrid: wx.GridSizer = None
    __mTxtName: wx.TextCtrl = None
    __mChoType: wx.Choice = None
    __mTxtUsername: wx.TextCtrl = None
    __mTxtPassword: wx.TextCtrl = None
    __mTxtPasswordCheck: wx.TextCtrl = None
    __mTxtEmail: wx.TextCtrl = None
    __mFSPercCapital: FloatSpin = None
    __mFSValCapital: wx.TextCtrl = None
    __mStTxtTotCapital: wx.StaticText = None
    __mList: wx.ListCtrl = None

    __mMainUser: MainUser = None

    def __init__(self, parent, size):
        super().__init__(parent, size)
        self.__init_main_user()
        self.__init_layout()

#region - Private Methods
#region - Init Methods
    def __init_main_user(self):
        self.__mMainUser = Environment().get_main_user()

    def __init_layout(self):
        self.SetBackgroundColour(Colors.COLOR_PLATFORM_BACKGROUND_GREY)
        self.__mbsMainBox = wx.BoxSizer(wx.VERTICAL)
        self.__mgsTopDataGrid = wx.FlexGridSizer(1, 7, 25, 50)
        self.__mgsBottomDataGrid = wx.FlexGridSizer(2, 0, 25, 50)
        self.__mbsMainBox.AddSpacer(25)
        self.__mbsMainBox.Add(self.__mgsTopDataGrid, 0, wx.SHAPED)
        self.__mbsMainBox.AddSpacer(25)
        horBox = wx.BoxSizer(wx.HORIZONTAL)
        horBox.Add(self.__mgsBottomDataGrid, 0, wx.SHAPED)
        horBox.AddSpacer(100)
        verBox = wx.BoxSizer(wx.VERTICAL)
        verBox.AddSpacer(100)
        verBox.Add(super()._get_vbs_button(self, Strings.STR_SAVE, self.__on_click_button_save), 1, wx.SHAPED|wx.CENTER|wx.ALL)
        horBox.Add(verBox)
        self.__mbsMainBox.Add(horBox, 0, wx.SHAPED)
        self.SetSizer(self.__mbsMainBox)
        self.__init_top_data_box()
        self.__init_bottom_data_box()
        self.__init_list()

    def __init_top_data_box(self):
        self.__mgsTopDataGrid.AddMany([
            (1, 1), self.__get_boxsizer_name(), (1, 1), (1, 1), (1, 1), self.__get_boxsizer_type(), (1, 1)
        ])

#region - BoxSizers Methods 
    def __get_boxsizer_name(self):
        self.__mTxtName = wx.TextCtrl(self, wx.ID_ANY, value = "", size = Sizes.INPUT_TEXT_SIZE_PLATFORM_DATA_PANEL)
        bsName = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label = Strings.STR_NAME, style = wx.ALIGN_CENTRE)
        label.SetForegroundColour(Colors.WHITE)
        bsName.Add(label, 0, wx.EXPAND)
        WxUtils.set_font_bold(label)
        bsName.Add(self.__mTxtName, 0, wx.EXPAND)
        return bsName

    def __get_boxsizer_type(self):
        self.__mChoType = wx.Choice(self, wx.ID_ANY, size = Sizes.INPUT_TEXT_SIZE_PLATFORM_DATA_PANEL)
        bsType = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, wx.ID_ANY, label = Strings.STR_TYPE, style = wx.ALIGN_CENTRE)
        label.SetForegroundColour(Colors.WHITE)
        bsType.Add(label, 0, wx.EXPAND)
        WxUtils.set_font_bold(label)
        bsType.Add(self.__mChoType, 0, wx.EXPAND)
        self.__mChoType.SetItems(PlatformType.get_all_names())
        return bsType

    def __init_bottom_data_box(self):
        self.__mgsBottomDataGrid.AddMany([
            (1, 1), self.__get_boxsizer_username(), (1, 1), (1, 1), (1, 1), self.__get_boxsizer_password(), self.__get_boxsizer_password_check(),
            (1, 1), self.__get_boxsizer_email(), (1, 1), (1, 1), (1, 1), self.__get_boxsizer_capital(), (1,1)
        ])

    def __get_boxsizer_username(self):
        self.__mTxtUsername = wx.TextCtrl(self, wx.ID_ANY, pos = wx.DefaultPosition, value = "", size = Sizes.INPUT_TEXT_SIZE_PLATFORM_DATA_PANEL)
        bsUsername = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, wx.ID_ANY, pos = wx.DefaultPosition, label = Strings.STR_USERNAME, style = wx.ALIGN_CENTRE)
        label.SetForegroundColour(Colors.WHITE)
        bsUsername.Add(label, 0, wx.EXPAND)
        WxUtils.set_font_bold(label)
        bsUsername.Add(self.__mTxtUsername, 0, wx.EXPAND)
        return bsUsername

    def __get_boxsizer_password(self):
        self.__mTxtPassword = wx.TextCtrl(self, wx.ID_ANY, pos = wx.DefaultPosition, value = "", style = wx.TE_PASSWORD, size = Sizes.INPUT_TEXT_SIZE_PLATFORM_DATA_PANEL)
        bsPassword = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, wx.ID_ANY, pos = wx.DefaultPosition, label = Strings.STR_PASSWORD, style = wx.ALIGN_CENTRE)
        label.SetForegroundColour(Colors.WHITE)
        bsPassword.Add(label, 0, wx.EXPAND)
        WxUtils.set_font_bold(label)
        bsPassword.Add(self.__mTxtPassword, 0, wx.EXPAND)
        return bsPassword

    def __get_boxsizer_password_check(self):
        self.__mTxtPasswordCheck = wx.TextCtrl(self, wx.ID_ANY, pos = wx.DefaultPosition, value = "", style = wx.TE_PASSWORD, size = Sizes.INPUT_TEXT_SIZE_PLATFORM_DATA_PANEL)
        bsPassword = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, wx.ID_ANY, pos = wx.DefaultPosition, label = Strings.STR_PASSWORD_CHECK, style = wx.ALIGN_CENTRE)
        label.SetForegroundColour(Colors.WHITE)
        bsPassword.Add(label, 0, wx.EXPAND)
        WxUtils.set_font_bold(label)
        bsPassword.Add(self.__mTxtPasswordCheck, 0, wx.EXPAND)
        return bsPassword

    def __get_boxsizer_email(self):
        self.__mTxtEmail = wx.TextCtrl(self, wx.ID_ANY, pos = wx.DefaultPosition, value = "", size = Sizes.INPUT_TEXT_SIZE_PLATFORM_DATA_PANEL, style = wx.BORDER_SIMPLE)
        bsEmail = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, wx.ID_ANY, pos = wx.DefaultPosition, label = Strings.STR_EMAIL, style = wx.ALIGN_CENTRE)
        label.SetForegroundColour(Colors.WHITE)
        bsEmail.Add(label, 0, wx.EXPAND)
        WxUtils.set_font_bold(label)
        bsEmail.Add(self.__mTxtEmail, 0, wx.EXPAND, border = 10)
        return bsEmail

    def __get_boxsizer_capital(self):
        totCapMainUser = self.__mMainUser.get_diff_tot_capital_platforms()
        self.__mFSPercCapital = FloatSpin(self, value = 10.0, min_val = 1/totCapMainUser, max_val = 100.0, increment = 1, digits = 2, size = (150, -1))
        self.__mFSValCapital = FloatSpin(self, value = totCapMainUser/10, min_val = 0.01, max_val = totCapMainUser, increment = 100, digits = 2, size = (150, -1))
        self.__mStTxtTotCapital = wx.StaticText(self, wx.ID_ANY, pos = wx.DefaultPosition, label = "{:.2f}".format(totCapMainUser), style = wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        WxUtils.set_font_bold(self.__mStTxtTotCapital)
        self.__mStTxtTotCapital.SetForegroundColour(Colors.COLOR_USER_CAPITAL)

        self.__mFSPercCapital.Bind(EVT_FLOATSPIN, self.__on_change_perc_capital)
        self.__mFSValCapital.Bind(EVT_FLOATSPIN, self.__on_change_val_capital)
        
        bsCapital = wx.BoxSizer(wx.VERTICAL)

        bsCapital.Add(self.__get_vertical_box_perc_val_capital(), 0, wx.EXPAND)

        bsCapital.Add(self.__mStTxtTotCapital, 0, wx.EXPAND)
        labelUserCapital = wx.StaticText(self, wx.ID_ANY, pos = wx.DefaultPosition, label = Strings.STR_USER_CAPITAL, style = wx.ALIGN_CENTRE)
        labelUserCapital.SetForegroundColour(Colors.COLOR_USER_CAPITAL)
        bsCapital.Add(labelUserCapital, 0, wx.EXPAND)
        WxUtils.set_font_bold(labelUserCapital)
        
        return bsCapital

    def __get_vertical_box_perc_val_capital(self):
        main = wx.BoxSizer(wx.VERTICAL)
        horOneBox = wx.BoxSizer(wx.HORIZONTAL)
        horTwoBox = wx.BoxSizer(wx.HORIZONTAL)

        horOneBox.AddSpacer(50)
        labelPercCapital = wx.StaticText(self, wx.ID_ANY, pos = wx.DefaultPosition, label = Strings.STR_PERCENTAGE_CAPITAL, style = wx.ALIGN_CENTRE)
        labelPercCapital.SetForegroundColour(Colors.WHITE)
        WxUtils.set_font_bold(labelPercCapital)
        horOneBox.Add(labelPercCapital)
        horOneBox.AddSpacer(125)
        labelTotCapital = wx.StaticText(self, wx.ID_ANY, pos = wx.DefaultPosition, label = Strings.STR_TOT_CAPITAL, style = wx.ALIGN_CENTRE)
        labelTotCapital.SetForegroundColour(Colors.WHITE)
        WxUtils.set_font_bold(labelTotCapital)
        horOneBox.Add(labelTotCapital)
        
        horTwoBox.Add(self.__mFSPercCapital)
        horTwoBox.AddSpacer(50)
        horTwoBox.Add(self.__mFSValCapital)

        main.Add(horOneBox)
        main.Add(horTwoBox)
        
        return main
#endregion

#region - List Methods
    def __init_list(self):
        self.__mList = PlatformDataList(self, wx.ID_ANY, wx.EXPAND|wx.LC_REPORT|wx.SUNKEN_BORDER, self.GetSize()[0] + 500)
        self.__mbsMainBox.Add(self.__mList, wx.EXPAND)
        self.__mList.init_layout()
        items = PlatformData.get_stored_data()
        if items is not None:
            self.__mList.add_items_and_populate(items)
#endregion
#endregion

#region - Save Methods
    def __on_click_button_save(self, evt):
        if self.__check_fields():
            platformData = PlatformData(uuid.uuid4(), self.__mTxtName.GetValue(), PlatformType(self.__mChoType.GetCurrentSelection()))
            platformData.set_username(self.__mTxtUsername.GetValue())
            platformData.set_password(self.__mTxtPassword.GetValue())
            platformData.set_email(self.__mTxtEmail.GetValue())
            platformData.set_tot_capital_value(round(self.__mFSValCapital.GetValue(), 2))
            platformData.set_perc_capital(self.__mFSPercCapital.GetValue())

            Environment().get_logger().info("] Storing PlatformData: \n\n%s\n\n" % platformData)

            self.__check_add_to_stored_platform_data_and_populate(platformData)
            self.__mChoType.SetSelection(Constants.CHOICE_EMPTY_INDEX)

            self.__mMainUser.set_from_stored_platform_data()
            self.__mMainUser.store_data()
            self.__mStTxtTotCapital.SetLabel(str(round(self.__mMainUser.get_diff_tot_capital_platforms(), 2)))

    def __check_add_to_stored_platform_data_and_populate(self, platformData):
        if(StoredDataUtils.check_stored_data_file_exists(DataFilenames.FILENAME_PLATFORM_DATA_LIST)):
                platformData.add_to_stored_data_list()
        else:
            l = []
            l.append(platformData)
            PlatformData.store_data_list(l)

        self.__mList.add_item(platformData)
        self.__mList.populate_list()
#endregion

#region - Check Methods
    def __check_fields(self):
        check = CHECK_OK
        fields = []
        if self.__mTxtName.IsEmpty():
            check = CHECK_NOT_OK
            fields.append(Strings.STR_NAME)

        if self.__mChoType.GetSelection() == Constants.CHOICE_EMPTY_INDEX:
            check = CHECK_NOT_OK
            fields.append(Strings.STR_TYPE)

        if self.__mTxtUsername.IsEmpty():
            check = CHECK_NOT_OK
            fields.append(Strings.STR_USERNAME)
        elif self.__mChoType.GetCurrentSelection() > -1 and self.__check_platform_username_already_present(self.__mTxtUsername.GetValue(), self.__mChoType.GetCurrentSelection()):
            check = CHECK_ALREADY_PRESENT
            self.__show_error_username_platform_already_present()

        if self.__mTxtPassword.IsEmpty():
            check = CHECK_NOT_OK
            fields.append(Strings.STR_PASSWORD)
        elif self.__mTxtPasswordCheck.IsEmpty():
            check = CHECK_NOT_OK
            fields.append(Strings.STR_PASSWORD_CHECK)
        elif self.__mTxtPassword.GetValue() != self.__mTxtPasswordCheck.GetValue():
            check = CHECK_DIFFERENT_PASSWORDS
            self.__show_error_message_different_passwords()

        if self.__mTxtEmail.IsEmpty():
            check = CHECK_NOT_OK
            fields.append(Strings.STR_EMAIL)
        elif not RegexUtils.check_email_format(self.__mTxtEmail.GetValue()):
            check = CHECK_WRONG_MAIL
            self.__show_error_message_email_format()

        if self.__mFSPercCapital.GetValue() <= 0x0:
            check = CHECK_NOT_OK
            fields.append(Strings.STR_PERCENTAGE_CAPITAL)

        if self.__mFSValCapital.GetValue() <= 0x0:
            check = CHECK_NOT_OK
            fields.append(Strings.STR_TOT_CAPITAL)
        elif float(self.__mStTxtTotCapital.GetLabel()) - float(self.__mFSValCapital.GetValue()) < 0x0:
            check = CHECK_VAL_TO_HIGH
            self.__show_error_message_inserted_capital_too_high()

        if not check:
            self.__show_errors_message_dialog(fields)
        elif check < 0x0:
            check = CHECK_NOT_OK

        return check

    def __check_platform_username_already_present(self, username, typ):
        for data in self.__mList.get_items():
            if data.get_username() == username and data.get_type() == PlatformType(typ):
                return True
        return False
#endregion

#region - OnChange Methods
    def __on_change_perc_capital(self, evt):
        totCapMainUser = self.__mMainUser.get_diff_tot_capital_platforms()
        p = self.__mFSPercCapital.GetValue()
        if p >= (1/totCapMainUser):
            val = round((self.__mMainUser.get_diff_tot_capital_platforms() / 100) * self.__mFSPercCapital.GetValue(), 2)
            self.__mFSValCapital.SetValue(val)
            self.__mFSPercCapital.SetValue((val * 100) / totCapMainUser)
        else:
            self.__show_error_message_value()
            self.__mFSPercCapital.SetValue(10)
            self.__on_change_perc_capital(None)

    def __on_change_val_capital(self, evt):
        totCapMainUser = self.__mMainUser.get_diff_tot_capital_platforms()
        val = self.__mFSValCapital.GetValue()
        if val >= 0.01:
            self.__mFSPercCapital.SetValue((val / totCapMainUser) * 100)
        else:
            self.__show_error_message_value()
            self.__mFSPercCapital.SetValue(10)
            self.__on_change_val_capital(None)
#endregion

#region - Messages Methods
    def __show_errors_message_dialog(self, fields):
        super()._show_error_message(Strings.STR_ERROR, Strings.STR_MSG_ERROR_MISSING_VALUES % ",\n".join(fields))

    def __show_error_message_email_format(self):
        super()._show_error_message(Strings.STR_ERROR, Strings.STR_MSG_ERROR_WRONG_EMAIL_FORMAT)

    def __show_error_message_different_passwords(self):
        super()._show_error_message(Strings.STR_ERROR, Strings.STR_MSG_ERROR_DIFFERENT_PASSWORDS)

    def __show_error_message_value(self):
        super()._show_error_message(Strings.STR_ERROR, Strings.STR_MSG_ERROR_VALUE)

    def __show_error_username_platform_already_present(self):
        super()._show_error_message(Strings.STR_ERROR, Strings.STR_MSG_ERROR_USERNAME_PLATFORM_ALREADY_PRESENT)

    def __show_error_message_inserted_capital_too_high(self):
        super()._show_error_message(Strings.STR_ERROR, Strings.STR_MSG_ERROR_INSERTED_CAPITAL_TOO_HIGH)
#endregion
#endregion