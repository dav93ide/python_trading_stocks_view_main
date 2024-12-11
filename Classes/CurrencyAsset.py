from Classes import BaseAsset
from Resources.Constants import Currency

class CurrencyAsset(BaseAsset):

    __mBid = None
    __mAsk = None
    __mCurrencyFrom: Currency = None
    __mCurrencyTo: Currency = None

    def __init__(self, id):
		super().__init__(id)

#region - Getter Methods
    def get_bid (self):
	    return self.__mBid 

    def get_ask (self):
        return self.__mAsk 

    def get_currencyFrom: Currency (self):
        return self.__mCurrencyFrom 

    def get_currencyTo: Currency (self):
        return self.__mCurrencyTo
#endregion

#region - Setter Methods
    def set_bid (self, bid):
        self.__mBid = bid 

    def set_Ask (self, ask):
        self.__mAsk = ask 

    def set_CurrencyFrom: Currency (self, currencyFrom):
        self.__mCurrencyFrom  = currencyFrom 

    def set_CurrencyTo: Currency (self, currencyTo):
        self.__mCurrencyTo  = currencyTo 
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {ETF.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mBid: {self.__mBid}\n"\
                f"#- __mAsk: {self.__mAsk}\n"\
                f"#- __mCurrencyFrom: {self.__mCurrencyFrom}\n"\
                f"#- __mCurrencyTo: {self.__mCurrencyTo}\n"\
                "####################"
