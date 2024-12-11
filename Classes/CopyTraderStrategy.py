from Classes import BaseTradingStrategy, Investor

class CopyTraderStrategy(BaseTradingStrategy):

    __mIdInvestorsToCopy = []
    __mUsernameInvestorsToCopy = []
    __mInvestorsToCopy: [Investor] = []
    __mBuyWhenBuy = None
    __mBuyWhenBuyIfGreen = None
    __mBuyWhenBuyIfRed = None
    __mSellWhenSell = None
    __mSellWhenSellIfGreen = None
    __mSellWhenSellIfRed = None
    __mBuyWhenSell = None
    __mBuyWhenSellIfGreen = None
    __mBuyWhenSellIfRed = None
    __mSellWhenBuy = None
    __mSellWhenBuyIfGreen = None
    __mSellWhenBuyIfRed = None

    def __init__(self, id):
        super(BaseTradingStrategy, self).__init__(id)

#region - Getter Method
    def get_ids_investors_to_copy(self):
        return self.__mIdInvestorsToCopy

    def get_usernames_investors_to_copy(self):
        return self.__mUsernameInvestorsToCopy

    def get_investors_to_copy(self):
        return self.__mInvestorsToCopy

    def getBuyWhenBuy(self):
        return self.__mBuyWhenBuy

    def getBuyWhenBuyIfGree(self):
        return self.__mBuyWhenBuyIfGreen

    def getBuyWhenBuyIfRed(self):
        return self.__mBuyWhenBuyIfRed

    def getSellWhenSell(self):
        return self.__mSellWhenSell

    def getSellWhenSellIfGreen(self):
        return self.__mSellWhenSellIfGreen

    def getSellWhenSellIfRed(self):
        return self.__mSellWhenSellIfRed

    def getBuyWhenSell(self):
        return self.__mBuyWhenSell

    def getBuyWhenSellIfGreen(self):
        return self.__mBuyWhenSellIfGreen

    def getBuyWhenSellIfRed(self):
        return self.__mBuyWhenSellIfRed

    def getSellWhenBuy(self):
        return self.__mSellWhenBuy

    def getSellWhenSellIfGreen(self):
        return self.__mSellWhenSellIfGreen

    def getSellWhenSellIfRed(self):
        return self.__mSellWhenSellIfRed
#endregion

#region - Setter Methods
    def set_ids_investors_to_copy(self, ids):
        self.__mIdInvestorsToCopy = ids

    def set_usernames_investors_to_copy(self, usernames):
        self.__mUsernameInvestorsToCopy = usernames

    def set_investors_to_copy(self, investor: [Investor]):
        self.__mInvestorsToCopy = investor

    def setBuyWhenBuy(self, buy: bool):
        self.__mBuyWhenBuy = buy

    def setBuyWhenBuyIfGree(self, buyIf: bool):
        self.__mBuyWhenBuyIfGreen = buyIf

    def setBuyWhenBuyIfRed(self, buyIf: bool):
        self.__mBuyWhenBuyIfRed = buyIf

    def setSellWhenSell(self, sell: bool):
        self.__mSellWhenSell = sell

    def setSellWhenSellIfGreen(self, sellIf: bool):
        self.__mSellWhenSellIfGreen = sellIf

    def setSellWhenSellIfRed(self, selfIf: bool):
        self.__mSellWhenSellIfRed = selfIf

    def setBuyWhenSell(self, buy: bool):
        self.__mBuyWhenSell = buy

    def setBuyWhenSellIfGreen(self, buyIf: bool):
        self.__mBuyWhenSellIfGreen = buyIf

    def setBuyWhenSellIfRed(self, buyIf: bool):
        self.__mBuyWhenSellIfRed = buyIf

    def setSellWhenBuy(self, sell: bool):
        self.__mSellWhenBuy = sell

    def setSellWhenSellIfGreen(self, sellIf: bool):
        self.__mSellWhenSellIfGreen = sellIf

    def setSellWhenSellIfRed(self, sellIf: bool):
        self.__mSellWhenSellIfRed = sellIf
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {CopyTraderStrategy.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mIdInvestorsToCopy: {self.__mIdInvestorsToCopy}\n"\
                f"#- __mUsernameInvestorsToCopy: {self.__mUsernameInvestorsToCopy}\n"\
                f"#- __mInvestorsToCopy: {self.__mInvestorsToCopy}\n"\
                f"#- __mBuyWhenBuy: {self.__mBuyWhenBuy}\n"\
                f"#- __mBuyWhenBuyIfGreen: {self.__mBuyWhenBuyIfGreen}\n"\
                f"#- __mBuyWhenBuyIfRed: {self.__mBuyWhenBuyIfRed}\n"\
                f"#- __mSellWhenSell: {self.__mSellWhenSell}\n"\
                f"#- __mSellWhenSellIfGreen: {self.__mSellWhenSellIfGreen}\n"\
                f"#- __mSellWhenSellIfRed: {self.__mSellWhenSellIfRed}\n"\
                f"#- __mBuyWhenSell: {self.__mBuyWhenSell}\n"\
                f"#- __mBuyWhenSellIfGreen: {self.__mSellNumDaysAfterExDividend}\n"\
                f"#- __mBuyWhenSellIfRed: {self.__mBuyWhenSellIfRed}\n"\
                f"#- __mSellWhenBuy: {self.__mSellWhenBuy}\n"\
                f"#- __mSellWhenSellIfGreen: {self.__mSellWhenSellIfGreen}\n"\
                f"#- __mSellWhenSellIfRed: {self.__mSellWhenSellIfRed}\n"\
                "####################"
