from Resources.Constants import InvestmentType

class InvestmentPosition(BaseClass):

    __id = None
    __mInvestmentType: InvestmentType = None
    __mOpenPrice = None
    __mCurrentPrice = None
    __mPercPL = None
    __mPL = None

    def __init__(self, id, type: InvestmentType):
        self.__id = id
        self.__mInvestmentType = type

#region - Getter Methods
    def get_id(self):
        return self.__id

    def get_investment_type(self):
        return self.__mInvestmentType

    def get_open_price(self):
        return self.__mOpenPrice

    def get_current_price(self):
        return self.__mCurrentPrice

    def get_perc_pl(self):
        return self.__mPercPL

    def get_pl(self):
        return self.__mPL
#endregion

#region - Setter Methods
    def set_id(self, id):
        self.__id = id

    def set_investment_type(self, type: InvestmentType):
        self.__mInvestmentType = type

    def set_open_price(self, price):
        self.__mOpenPrice = price

    def set_current_price(self, price):
        self.__mCurrentPrice = price

    def set_perc_pl(self, perc):
        self.__mPercPL = perc

    def set_pl(self, pl):
        self.__mPL = pl
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {InvestmentPosition.__name__}\n"\
                "####################\n"\
                f"#- __id: {self.__id}\n"\
                f"#- __mInvestmentType: {self.__mInvestmentType.name}\n"\
                f"#- __mOpenPrice: {self.__mOpenPrice}\n"\
                f"#- __mCurrentPrice: {self.__mCurrentPrice}\n"\
                f"#- __mPercPL: {self.__mPercPL}\n"\
                f"#- __mPL: {self.__mPL}\n"\
                "####################"
