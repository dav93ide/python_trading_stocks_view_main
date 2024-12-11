from Classes import BaseAsset
from Resources.Constants import ResourceType

class Commodity(BaseAsset):

    __mType = None
    __mOneYearReturn = None

    def __init__(self, t: ResourceType):
        self.__mType = t

#region - Getter Method
    def get_type(self):
        return self.__mType

    def get_one_year_return(self):
        return self.__mOneYearReturn
#endregion

#region - Setter Methods
    def set_type(self, t):
        self.__mType = t

    def set_one_year_return(self, ret):
        self.__mOneYearReturn = ret
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Commodity.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mType: {self.__mType}\n"\
                f"#- __mOneYearReturn: {self.__mOneYearReturn}\n"\
                "####################"
