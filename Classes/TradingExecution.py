from Classes.BaseClasses.BaseClass import BaseClass
from Resources.Constants import PlatformType
from Classes import Investment

class TradingExecution(BaseClass):

    __id = None
    __mIsSimulation = True
    __mInvestments: [Investment] = [Investment]
    __mTotPercPL = None
    __mTotPL = None

    def __init__(self, id, botId, platformType: PlatformType, isSimulation: bool):
        self.__id = id
        self.__mBotId = botId
        self.__mPlatformType = platformType
        self.__mIsSimulation = isSimulation
        self.__mInvestments = []


    # Getter Methods
    def get_id(self):
        return self.__id

    def get_is_simulation(self):
        return self.__mIsSimulation

    def get_investments(self):
        return self.__mInvestments

    def get_tot_perc_pl(self):
        return self.__mTotPercPL

    def get_tot_pl(self):
        return self.__mTotPL

    # Setter Methods
    def set_id(self, id):
        self.__id = id

    def set_is_simulation(self, isSimulation: bool):
        self.__mIsSimulation = isSimulation

    def set_investments(self, investments: [Investment]):
        self.__mInvestments = investment

    def set_tot_perc_pl(self, perc):
        self.__mTotPercPL = perc

    def set_tot_pl(self, pl):
        self.__mTotPL = pl

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Investment.__name__}\n"\
                "####################\n"\
                f"#- __id: {self.__id}\n"\
                f"#- __mIsSimulation: {self.__mIsSimulation}\n"\
                f"#- __mInvestments: {self.__mInvestments}\n"\
                f"#- __mTotPercPL: {self.__mTotPercPL}\n"\
                f"#- __mTotPL: {self.__mTotPL}\n"\
                "####################"

    
