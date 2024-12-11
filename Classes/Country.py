from Classes.BaseClasses.BaseClass import BaseClass

class Country(BaseClass):

    __mName = None
    __mCode = None

    def __init__(self, id):
	    super().__init__(id)

#region - Getter Methods
    def get_name(self):
        return self.mName

    def get_post_code(self):
        return self.mPostCode
#endregion

#region - Getter Methods
    def set_name(self, name):
        self.mName = name

    def set_post_code(self, postCode):
        self.mPostCode = postCode
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Country.__name__}\n"\
                f"{super().__str__()} \n"\
                f"#- __mName: {self.__mName}\n"\
                f"#- __mCode: {self.__mCode}\n"\
                "####################"