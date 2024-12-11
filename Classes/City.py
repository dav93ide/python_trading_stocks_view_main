from Classes import Country
from Classes.BaseClasses.BaseClass import BaseClass

class City(BaseClass):

    __mName = None
    __mPostCode = None
    __mCountry: Country = None

    def __init__(self, id):
        super().__init__(id)

#region - Getter Methods
    def get_name(self):
        return self.mName

    def get_post_code(self):
        return self.mPostCode

    def get_country(self):
        return self.mCountry
#endregion

#region - Getter Methods
    def set_name(self, name):
        self.mName = name

    def set_post_code(self, postCode):
        self.mPostCode = postCode

    def set_country(self, country):
        self.mCountry = country
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {City.__name__}\n"\
                f"{super().__str__()} \n"\
                f"#- __mName: {self.__mName}\n"\
                f"#- __mCode: {self.__mCode}\n"\
                "####################"
