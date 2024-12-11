from Classes.BaseClasses.BaseClass import BaseClass
from Resources.Constants import PlatformType
import logging

class Platform(BaseClass):

    NAME_ETORO = "eToro"
    NAME_WEBULL = "WeBull"
    NAME_IB = "Interactive Brokers"
    NAME_PLUS500 = "Plus500"
    NAME_ROBINHOOD = "RobinHood"

    __mName = None
    __mType: PlatformType = None
    __mInvestors = []

    def __init__(self, id, name: str, typ: PlatformType):
        super().__init__(id)
        self.__id = id
        self.__mName = name
        self.__mType = typ
        self.__mInvestors = []

    # Getter Methods
    def get_name(self):
        return self.__mName

    def get_type(self):
        return self.__mType

    def get_investors(self):
        return self.__mInvestors

    # Setter Methods
    def set_name(self, name):
        self.__mName = name

    def set_type(self, t):
        self.__mType = t

    def set_investors(self, investors):
        self.__mInvestors = investors

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Platform.__name__}\n"\
                "####################\n"\
                f"{super().__str__()} \n"\
                f"#- __mName: {self.__mName}\n"\
                f"#- __mType: {self.__mType}\n"\
                f"#- __mInvestors: DOING\n"\
                "####################"