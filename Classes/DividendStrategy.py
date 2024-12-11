from Classes import BaseTradingStrategy

class DividendStrategy(BaseTradingStrategy):

    __mMaxDividend = None
    __mMinDividend = None
    __mBuyNumDaysBeforeExDividend = None
    __mSellNumDaysAfterExDividend = None

    def __init__(self, id, ask: bool):
        super().__init__(id, ask)

#region - Getter Methods
    def get_max_dividend(self):
        return self.__mMaxDividend

    def get_min_dividend(self):
        return self.__mMinDividend

    def get_buy_num_days_before_ex_dividend(self):
        return self.__mBuyNumDaysBeforeExDividend

    def get_sell_num_days_after_ex_dividend(self):
        return self.__mSellNumDaysAfterExDividend
#endregion

#region - Setter Methods
    def set_max_dividend(self, max):
        self.__mMaxDividend = max

    def set_min_dividend(self, min):
        self.__mMinDividend = min

    def set_buy_num_days_before_ex_dividend(self, num):
        self.__mBuyNumDaysBeforeExDividend = num

    def set_sell_num_days_after_ex_dividend(self, num):
        self.__mSellNumDaysAfterExDividend = num
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {DividendStrategy.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mMaxDividend: {self.__mMaxDividend}\n"\
                f"#- __mMinDividend: {self.__mMinDividend}\n"\
                f"#- __mBuyNumDaysBeforeExDividend: {self.__mBuyNumDaysBeforeExDividend}\n"\
                f"#- __mTargetSect__mSellNumDaysAfterExDividendors: {self.__mSellNumDaysAfterExDividend}\n"\
                "####################"
