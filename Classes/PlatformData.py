from multipledispatch import dispatch
from Classes.Platform import Platform, PlatformType
from Classes.TradingBot import TradingBot
from Resources.Constants import DataFilenames
from Classes.BaseClasses.BaseClass import BaseClass

class PlatformData(Platform):

    __mUsername = None
    __mPassword = None
    __mEmail = None
    __mTotCapitalValue = None
    __mPercCapital = None
    __mTotPL = None
    __mPercPL = None
    __mNumOpenPositions = None
    __mNumBots = None
    __mNumBotsRunning = None
    __mTradingBots = []

    def __init__(self, id: str, name: str, pType: PlatformType):
        super(PlatformData, self).__init__(id, name, pType)
        self.__mTradingBots = []

#region - Getter Methods
    def get_username(self):
        return self.__mUsername

    def get_password(self):
        return self.__mPassword

    def get_email(self):
        return self.__mEmail

    def get_tot_capital_value(self):
        return self.__mTotCapitalValue

    def get_perc_capital(self):
        return self.__mPercCapital

    def get_tot_pl(self):
        return self.__mTotPL

    def get_perc_pl(self):
        return self.__mPercPL

    def get_num_open_positions(self):
        return self.__mNumOpenPositions

    def get_num_bots(self):
        return self.__mNumBots

    def get_num_bots_running(self):
        return self.__mNumBotsRunning

    def get_bots(self):
        return self.__mTradingBots
#endregion

#region - Setter Methods
    def set_username(self, username):
        self.__mUsername = username

    def set_password(self, password):
        self.__mPassword = password

    def set_email(self, email):
        self.__mEmail = email

    def set_tot_capital_value(self, tot):
        self.__mTotCapitalValue = tot

    def set_perc_capital(self, perc):
        self.__mPercCapital = perc

    def set_tot_pl(self, pl):
        self.__mTotPL = pl

    def set_perc_pl(self, pl):
        self.__mPercPL = pl

    def set_num_open_positions(self, pos):
        self.__mNumOpenPositions = pos

    def set_num_bots(self, bots):
        self.__mNumBots = bots

    def set_num_bots_running(self, bots):
        self.__mNumBotsRunning = bots

    def set_bots(self, bots: [TradingBot]):
        self.__mTradingBots = bots
#endregion

#region - Public Methods
#region - Store Data Methods
    @staticmethod
    def store_data_list(l):
        BaseClass.store_data_list(l, DataFilenames.FILENAME_PLATFORM_DATA_LIST)

    def add_to_stored_data_list(self):
        BaseClass.add_to_stored_data_list(self, DataFilenames.FILENAME_PLATFORM_DATA_LIST)

    @staticmethod
    def get_stored_data():
        return BaseClass.get_stored_data(DataFilenames.FILENAME_PLATFORM_DATA_LIST)
#endregion
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {PlatformData.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mUsername: {self.__mUsername}\n"\
                f"#- __mPassword: {self.__mPassword}\n"\
                f"#- __mEmail: {self.__mEmail}\n"\
                f"#- __mTotCapitalValue: {self.__mTotCapitalValue}\n"\
                f"#- __mPercCapital: {self.__mPercCapital}\n"\
                f"#- __mTotPL: {self.__mTotPL}\n"\
                f"#- __mPercPL: {self.__mPercPL}\n"\
                f"#- __mNumOpenPositions: {self.__mNumOpenPositions}\n"\
                f"#- __mNumBots: {self.__mNumBots}\n"\
                f"#- __mNumBotsRunning: {self.__mNumBotsRunning}\n"\
                f"#- __mTradingBots: {self.__mTradingBots}\n"\
                "####################"
