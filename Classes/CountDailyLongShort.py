from typing import overload
from Classes.BaseClasses.BaseClass import BaseClass

class CountDailyLongShort(BaseClass):

    __mAsset = None
    __mDate = None
    __mNumLongs = 0x0
    __mNumShorts = 0x0

    def __init__(self, id):
        super().__init__(id)

#region - Getter Methods
    def get_asset(self):
        return self.__mAsset

    def get_date(self):
        return self.__mDate

    def get_num_longs(self):
        return self.__mNumLongs

    def get_num_shorts(self):
        return self.__mNumShorts
#endregion

#region - Setter Methods
    def set_asset(self, asset):
        self.__mAsset = asset

    def set_date(self, date):
        self.__mDate = date

    def set_num_longs(self, num):
        self.__mNumLongs = num

    def set_num_shorts(self, num):
        self.__mNumShorts = num
#endregion

#region - Add Methods
    def add_long(self, add):
        self.__mNumLongs += add

    def add_long(self):
        +(+self.__mNumLongs)

    @overload
    def add_short(self, add: int) -> None:
        self.__mNumShorts += add

    def add_short(self) -> None:
        +(+self.__mNumShorts)
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {CountDailyLongShort.__name__}\n"\
                f"{super().__str__()} \n"\
                f"#- __mAsset: {self.__mAsset}\n"\
                f"#- __mDate: {self.__mDate}\n"\
                f"#- __mNumLongs: {self.__mNumLongs}\n"\
                f"#- __mNumShorts: {self.__mNumShorts}\n"\
                "####################"
    