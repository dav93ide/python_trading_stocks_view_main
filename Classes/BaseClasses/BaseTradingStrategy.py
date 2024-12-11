from Classes.BaseClasses.BaseClass import BaseClass

class BaseTradingStrategy(BaseClass):

    __mName = None

    def __init__(self, id, name):
        super().__init__(id)
        self.__mName = name

#region - Get Methods
    def get_name(self):
        return self.__mName
#endregion

#region - Set Methods
    def set_name(self, name):
        self.__mName = name
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {BaseTradingStrategy.__name__}\n"\
                "####################\n"\
                f"{super().__str__()}\n"\
                f"#- __mName: {self.__mName}\n"\
                "####################"