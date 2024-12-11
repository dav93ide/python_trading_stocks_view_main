from Classes.BaseClasses.BaseClass import BaseClass

class Exchange(BaseClass):

    __id = None
    __mName = None
    __mFullName = None
    __mCountry = None
    __mCurrency = None
    __mStocks = None
    __mETFs = None

#region - Getter Methods
    def get_id (self):
	    return self.__id 

    def get_name (self):
        return self.__mName 

    def get_full_name(self):
        return self.__mFullName

    def get_country (self):
        return self.__mCountry 

    def get_currency (self):
        return self.__mCurrency 

    def get_stocks (self):
        return self.__mStocks 

    def get_etf(self):
        return self.__mETFs
#endregion

#region - Setter Methods
    def set_id (self, id):
        self.__id  = id 

    def set_name (self, name):
        self.__mName  = name 

    def set_full_name(self, name):
        self.__mFullName = name

    def set_country (self, country):
        self.__mCountry  = country 

    def set_currency (self, currency):
        self.__mCurrency  = currency 

    def set_stocks (self, stocks):
        self.__mStocks  = stocks 

    def set_etf(self, etf):
        self.__mETFs = etf
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Exchange.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __id: {self.__id}\n"\
                f"#- __mName: {self.__mName}\n"\
                f"#- __mFullName: {self.__mFullName}\n"\
                f"#- __mCountry: {self.__mCountry}\n"\
                f"#- __mCurrency: {self.__mCurrency}\n"\
                f"#- __mStocks: {self.__mStocks}\n"\
                f"#- __mETFs: {self.__mETFs}\n"\
                "####################"
