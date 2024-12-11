from Classes.BaseClasses.BaseClass import BaseClass
from Resources.Constants import Sector

class BotTradingStrategy(BaseClass):

    __mName = None

    __mValueStopLoss = None
    __mPercStopLoss = None
    __mValueTakeProfit = None
    __mPercTakeProfit = None1

    __mAlwaysAskConfirmation = None
    __mTargetSectors: [Sector] = [Sector]
    __mTargetAssets: [None] = [None]
    __mPercOfCapital: None
    __mValueOfCapital: None

    def __init__(self, id, ask: bool):
        super().__init__(id)
        self.__mAlwaysAskConfirmation = ask
        self.__mTargetSectors = []
        self.__mTargetAssets = []

#region - Getter Methods
    def get_name(self):
        return self.__mName

    def get_value_stop_loss(self):
        return self.__mValueStopLoss

    def get_perc_stop_loss(self):
        return self.__mPercStopLoss

    def get_value_take_profit(self):
        return self.__mValueTakeProfit

    def get_perc_take_profit(self):
        return self.__mPercTakeProfit

    def get_always_ask_confirmation(self):
        return self.__mAlwaysAskConfirmation

    def get_target_sectors(self):
        return self.__mTargetSectors

    def get_target_assets(self):
        return self.__mTargetAssets

    def get_perc_of_capital(self):
        return self.__mPercOfCapital

    def get_value_of_capital(self):
        return self.__mValueOfCapital
#endregion

#region - Setter Methods
    def set_name(self, name):
        self.__mName = name

    def set_value_stop_loss(self, valueStopLoss):
        self.__mValueStopLoss = valueStopLoss

    def set_perc_stop_loss(self, percStopLoss):
        self.__mPercStopLoss = percStopLoss

    def set_value_take_profit(self, valueTakeProfit):
        self.__mValueTakeProfit = valueTakeProfit

    def set_perc_take_profit(self, percTakeProfit):
        self.__mPercTakeProfit = percTakeProfit

    def set_always_ask_confirmation(self, ask):
        self.__mAlwaysAskConfirmation = ask

    def set_target_sectors(self, sectors: [Sector]):
        self.__mTargetSectors = sectors

    def set_target_assets(self, assets):
        self.__mTargetAssets = assets

    def set_perc_of_capital(self, perc):
        self.__mPercOfCapital = perc

    def set_value_of_capital(self, val):
        self.__mValueOfCapital = val
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {BaseTradingStrategy.__name__}\n"\
                "####################\n"\
                f"{super().__str__()} \n"\
                f"#- __mName: {self.__mName}\n"\
                f"#- __mValueStopLoss: {self.__mValueStopLoss}\n"
                f"#- __mPercStopLoss: {self.__mPercStopLoss}\n"
                f"#- __mValueTakeProfit: {self.__mValueTakeProfit}\n"
                f"#- __mPercTakeProfit: {self.__mPercTakeProfit}\n"
                f"#- __mAlwaysAskConfirmation: {self.__mAlwaysAskConfirmation}\n"\
                f"#- __mTargetSectors: {self.__mTargetSectors}\n"\
                f"#- __mTargetAssets: {self.__mTargetAssets}\n"\
                f"#- __mPercOfCapital: {self.__mPercOfCapital}\n"\
                f"#- __mValueOfCapital: {self.__mValueOfCapital}\n"\
                "####################"