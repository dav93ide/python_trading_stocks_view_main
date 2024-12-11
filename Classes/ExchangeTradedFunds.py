# Exchange Traded Funds

from Classes import Exchange
from Classes import BaseAsset

class ExchangeTradedFunds(BaseAsset):

    __mAsk = None
    __mBid = None
    __mNetAssets = None
    __mNAV = None
    __mPERatio = None
    __mYeld = None
    __mYTFDailyTotalReturn = None
    __mBetaFiveYMonthly = None
    __mExpenseRatio = None
    __mInceptionDate = None
    __mHasPrePostMarketData = None

#region - Getter Methods
    def get_ask(self):
	    return self.__mAsk 

    def get_bid(self):
        return self.__mBid 

    def get_net_assets(self):
        return self.__mNetAssets 

    def get_nav(self):
        return self.__mNAV 

    def get_peratio(self):
        return self.__mPERatio 

    def get_yeld(self):
        return self.__mYeld 

    def get_ytf_daily_total_return(self):
        return self.__mYTFDailyTotalReturn 

    def get_beta_five_y_monthly(self):
        return self.__mBetaFiveYMonthly 

    def get_expense_ratio(self):
        return self.__mExpenseRatio 

    def get_inception_date(self):
        return self.__mInceptionDate 

    def get_has_pre_post_market_data(self):
        return self.__mHasPrePostMarketData
#endregion

#region - Setter Methods
    def set_ask(self, ask):
        self.__mAsk  = ask 

    def set_bid(self, bid):
        self.__mBid  =Bid 

    def set_net_assets(self, netAssets):
        self.__mNetAssets  = netAssets 

    def set_nav(self, nav):
        self.__mNAV  = nav 

    def set_peratio(self, ratio):
        self.__mPERatio  = ratio 

    def set_yeld(self, yeld):
        self.__mYeld  = yeld 

    def set_ytf_daily_total_return(self, ytfDailyTotalReturn):
        self.__mYTFDailyTotalReturn  = YTFDailyTotalReturn 

    def set_beta_five_y_monthly(self, betaFiveYMonthly):
        self.__mBetaFiveYMonthly  = betaFiveYMonthly 

    def set_expense_ratio(self, expenseRatio):
        self.__mExpenseRatio  = expenseRatio 

    def set_inception_date(self, inceptionDate):
        self.__mInceptionDate  = inceptionDate 

    def set_has_pre_post_market_data(self, hasPrePostMarketData):
        self.__mHasPrePostMarketData = hasPrePostMarketData
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {ETF.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mAsk: {self.__mAsk}\n"\
                f"#- __mBid: {self.__mBid}\n"\
                f"#- __mNetAssets: {self.__mNetAssets}\n"\
                f"#- __mNAV: {self.__mNAV}\n"\
                f"#- __mPERatio: {self.__mPERatio}\n"\
                f"#- __mYeld: {self.__mYeld}\n"\
                f"#- __mYTFDailyTotalReturn: {self.__mYTFDailyTotalReturn}\n"\
                f"#- __mBetaFiveYMonthly: {self.__mBetaFiveYMonthly}\n"\
                f"#- __mExpenseRatio: {self.__mExpenseRatio}\n"\
                f"#- __mInceptionDate: {self.__mInceptionDate}\n"\
                f"#- __mHasPrePostMarketData: {self.__mHasPrePostMarketData}\n"\
                "####################"
