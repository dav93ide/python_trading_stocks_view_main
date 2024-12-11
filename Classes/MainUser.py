from Classes.Investor import Investor, BaseClass, dispatch
from Resources.Constants import Directories, DataFilenames

class MainUser(Investor):
    
    __mPassword = None
    __mTradingBots = []
    __mPlatformsData = []
    __mPercCapitalBots = None

    def __init__(self, id):
        super().__init__(id)
        self.__mTradingBots = []
        self.__mPlatformsData = []

#region - Getter Methods
    def get_password(self):
        return self.__mPassword

    def get_trading_bots(self):
        return self.__mTradingBots

    def get_platforms_data(self):
        return self.__mPlatformsData

    def get_perc_capital_bots(self):
        return self.__mPercCapitalBots
#endregion

#region - Setter Methods
    def set_password(self, password):
        self.__mPassword = password

    def set_trading_bots(self, bots):
        self.__mTradingBots = bots

    def set_platforms_data(self, data):
        self.__mPlatformsData = data

    def set_perc_capital_bots(self, perc):
        self.__mPercCapitalBots = perc
#endregion

#region - Public Methods
#region - Store Data Methods
    def store_data(self):
        BaseClass.store_data(self, DataFilenames.FILENAME_MAIN_USER_DATA)

    def get_stored_data():
        return BaseClass.get_stored_data(DataFilenames.FILENAME_MAIN_USER_DATA)

    def set_from_stored_platform_data(self):
        stored = BaseClass.get_stored_data(DataFilenames.FILENAME_PLATFORM_DATA_LIST)
        if stored is not None:
            self.__mPlatformsData = stored
#endregion

#region - Public Methods
    def get_diff_tot_capital_platforms(self):
        tot = super().get_tot_capital()
        if len(self.__mPlatformsData) > 0x0:
            for data in self.__mPlatformsData:
                tot = tot - data.get_tot_capital_value()
        return round(tot, 2)
#endregion
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {MainUser.__name__}\n"\
                f"{super().__str__()} \n"\
                f"#- __mPassword: {self.__mPassword}\n"\
                f"#- __mTradingBots: {str(self.__mTradingBots)}\n"\
                f"#- __mPlatformsData: {self.__mPlatformsData}\n"\
                f"#- __mPercCapitalBots: {self.__mPercCapitalBots}\n"\
                "####################"
