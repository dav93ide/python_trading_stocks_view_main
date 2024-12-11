from Resources.Constants import PlatformType
from Classes.TradingExecution import TradingExecution
from Classes.BaseClasses.BaseTradingStrategy import BaseTradingStrategy
from Classes.BaseClasses.BaseClass import BaseClass
from Classes.BaseClasses.BaseAsset import BaseAsset
from typing import TypeVar

class TradingBot(BaseClass):
    
    __mName = None
    __mCapital = None
    __mTradingStrategies: BaseTradingStrategy = None
    __mTradingExecutions: TradingExecution = None
    __mTargetAssets: [BaseAsset] = []

    def __init__(self, id, name, capital):
        super().__init__(id)
        self.__mName = name
        self.__mCapital = capital
        self.__mTradingStrategies = []
        self.__mTradingExecutions = []
        self.__mTargetAssets = []

    # Getter Methods
    def get_name(self):
        return self.__mName

    def get_capital(self):
        return self.__mCapital

    def get_trading_strategies(self):
        return self.__mTradingStrategies

    def get_trading_executions(self):
        return self.__mTradingExecutions

    def get_target_assets(self):
        return self.__mTargetAssets

    # Setter Methods
    def set_name(self, name):
        self.__mName = name

    def set_capital(self, tot):
        self.__mCapital = tot

    def set_trading_strategies(self, strategies):
        self.__mTradingStrategies = strategies

    def set_trading_executions(self, executions):
        self.__mTradingExecutions = executions

    def set_target_assets(self, assets):
        self.__mTargetAssets = assets

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {TradingBot.__name__}\n"\
                "####################\n"\
                f"{super().__str__()} \n"\
                f"#- __mName: {self.__mName}\n"\
                f"#- __mCapital: {self.__mCapital}\n"\
                f"#- __mTradingStrategies: {self.__mTradingStrategies}\n"\
                f"#- __mTradingExecutions: {self.__mTradingExecutions}\n"\
                f"#- __mTargetAssets: {self.__mTargetAssets}\n"\
                "####################"
