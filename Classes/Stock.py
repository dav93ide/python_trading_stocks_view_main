from Classes.Company import Company
from Classes.Exchange import Exchange
from Classes.BaseClasses.BaseAsset import BaseAsset
from Classes.BaseClasses.BaseClass import BaseClass
from Resources.Constants import DataFilenames

class Stock(BaseAsset):

    __mAsk = None
    __mAskSize = None
    __mBid = None
    __mBidSize = None
    __mCompany: Company = None
    __mSharesFloat = None
    __mSharesOutstanding = None
    __mImpliedSharesOutstanding = None
    __mPercSharesInsiders = None
    __mPercSharesInstitutions = None
    __mSharesShort = None
    __mShortRatio = None
    __mPercShortOfFloat = None
    __mPercShortOfOutstanding = None
    __mTrailingPriceEarnings = None
    __mForwardPriceEarnings = None
    __mPEGRatioFiveYears = None
    __mPriceToSales = None
    __mPriceToBook = None
    __mReturnOnEquity = None
    __mDilutedEPS = None
    __mBookValuePerShare = None
    __mOneYearTargetEstimated = None
    __mBeta = None
    __mFiftyDaysMovingAvg = None
    __mTwoHundredsDaysMovingAvg = None
    __mLastSplitFactor = None
    __mLastSplitDate = None
    __mNetIncomeToCommonShares = None
    __mHasPrePostMarketData = None
    __mExDividendDate = None
    __mDividendDate = None
    __mDividend = None
    __mPayoutRatio = None
    __mForwardAnnualDividendRate = None
    __mPercForwardAnnualDividendYeld = None
    __mTrailingAnnualDividendRate = None
    __mTrailingAnnualDividendYeld = None
    __mFiveYearAvgDividendYeld = None
    __mDividendRate = None
    __mEnterpriseValue = None
    __mPeRatio = None
    __mPegRatio = None
    __mPbRatio = None
    __mEnterprisesValueRevenueRatio = None
    __mEnterprisesValueEBITDARatio = None
    __mAverageAnalystRating = None
    __mMarketChangePercent = None
    __mPreMarketPrice = None
    __mPostMarketChangePercent = None
    __mPostMarketTime = None
    __mPostMarketPrice = None
    __mPostMarketChange = None
    __mEarningsTimestamp = None
    __mEpsTrailingTwelveMonths = None
    __mEpsForward = None
    __mEpsCurrentYear = None
    __mPriceEpsCurrentYearRatio = None

    def __init__(self, id):
        super(BaseAsset, self).__init__(id)

#region - Getter Methods
    def get_ask(self):
	    return self.__mAsk 

    def get_ask_size(self):
        return self.__mAskSize

    def get_bid(self):
        return self.__mBid 

    def get_bid_size(self):
        return self.__mBidSize

    def get_company(self):
        return self.__mCompany 

    def get_shares_float(self):
        return self.__mSharesFloat 

    def get_shares_outstanding(self):
        return self.__mSharesOutstanding 

    def get_implied_shares_outstanding(self):
        return self.__mImpliedSharesOutstanding 

    def get_perc_shares_insiders(self):
        return self.__mPercSharesInsiders 

    def get_perc_shares_institutions(self):
        return self.__mPercSharesInstitutions 

    def get_shares_short(self):
        return self.__mSharesShort 

    def get_short_ratio(self):
        return self.__mShortRatio 

    def get_perc_short_of_float(self):
        return self.__mPercShortOfFloat 

    def get_perc_short_of_outstanding(self):
        return self.__mPercShortOfOutstanding 

    def get_trailing_price_earnings(self):
        return self.__mTrailingPriceEarnings 

    def get_forward_price_earnings(self):
        return self.__mForwardPriceEarnings 

    def get_peg_ratioFiveYears(self):
        return self.__mPEGRatioFiveYears 

    def get_price_to_sales(self):
        return self.__mPriceToSales 

    def get_price_to_book(self):
        return self.__mPriceToBook 

    def get_return_on_equity(self):
        return self.__mReturnOnEquity 

    def get_diluted_eps(self):
        return self.__mDilutedEPS 

    def get_book_value_per_share(self):
        return self.__mBookValuePerShare 

    def get_one_year_target_estimated(self):
        return self.__mOneYearTargetEstimated 

    def get_beta(self):
        return self.__mBeta 

    def get_fifty_days_moving_avg(self):
        return self.__mFiftyDaysMovingAvg 

    def get_two_hundreds_days_moving_avg(self):
        return self.__mTwoHundredsDaysMovingAvg 

    def get_last_split_factor(self):
        return self.__mLastSplitFactor 

    def get_last_split_date(self):
        return self.__mLastSplitDate 

    def get_net_income_to_common_shares(self):
        return self.__mNetIncomeToCommonShares 

    def get_has_pre_post_market_data(self):
        return self.__mHasPrePostMarketData

    def get_ex_dividend_date(self):
	    return self.__mExDividendDate

    def get_dividend_date(self):
        return self.__mDividendDate

    def get_dividend(self):
        return self.__mDividend

    def get_payout_ratio(self):
        return self.__mPayoutRatio

    def get_forward_annual_dividend_rate(self):
        return self.__mForwardAnnualDividendRate

    def get_perc_forward_annual_dividend_yeld(self):
        return self.__mPercForwardAnnualDividendYeld

    def get_trailing_annual_dividend_rate(self):
        return self.__mTrailingAnnualDividendRate

    def get_trailing_annual_dividend_yeld(self):
        return self.__mTrailingAnnualDividendYeld

    def get_five_year_avg_dividend_yeld(self):
        return self.__mFiveYearAvgDividendYeld

    def get_dividend_rate():
        return self.__mDividendRate

    def get_enterprise_value(self):
	    return self.__mEnterpriseValue

    def get_pe_ratio(self):
        return self.__mPeRatio

    def get_peg_ratio(self):
        return self.__mPegRatio

    def get_pb_ratio(self):
        return self.__mPbRatio

    def get_enterprises_value_revenue_ratio(self):
        return self.__mEnterprisesValueRevenueRatio

    def get_enterprises_value_ebitda_ratio(self):
        return self.__mEnterprisesValueEBITDARatio

    def get_average_analyst_rating(self):
	    return self.__mAverageAnalystRating

    def get_market_change_percent(self):
        return self.__mMarketChangePercent

    def get_pre_market_price(self):
        return self.__mPreMarketPrice

    def get_post_market_change_percent(self):
        return self.__mPostMarketChangePercent

    def get_post_market_time(self):
        return self.__mPostMarketTime

    def get_post_market_price(self):
        return self.__mPostMarketPrice

    def get_post_market_change(self):
        return self.__mPostMarketChange

    def get_earnings_timestamp(self):
        return self.__mEarningsTimestamp
        
    def get_eps_trailing_twelve_months(self):
	    return self.__mEpsTrailingTwelveMonths

    def get_eps_forward(self):
        return self.__mEpsForward

    def get_eps_current_year(self):
        return self.__mEpsCurrentYear

    def get_price_eps_current_year_ratio(self):
        return self.__mPriceEpsCurrentYearRatio 
#endregion

#region - Setter Methods
    def set_ask(self, ask):
	    self.__mAsk = ask

    def set_ask_size(self, size):
        self.__mAskSize = size

    def set_bid(self, bid):
        self.__mBid = bid

    def set_bid_size(self, size):
        self.__mBidSize = size

    def set_company(self, company):
        self.__mCompany = company

    def set_shares_float(self, sharesFloat):
        self.__mSharesFloat = sharesFloat

    def set_shares_outstanding(self, sharesOutstanding):
        self.__mSharesOutstanding = sharesOutstanding

    def set_implied_shares_outstanding(self, impliedSharesOutstanding):
        self.__mImpliedSharesOutstanding = impliedSharesOutstanding

    def set_perc_shares_insiders(self, percSharesInsiders):
        self.__mPercSharesInsiders = percSharesInsiders

    def set_perc_shares_institutions(self, percSharesInstitutions):
        self.__mPercSharesInstitutions = percSharesInstitutions

    def set_shares_short(self, sharesShort):
        self.__mSharesShort = sharesShort

    def set_short_ratio(self, shortRatio):
        self.__mShortRatio = shortRatio

    def set_perc_short_of_float(self, percShortOfFloat):
        self.__mPercShortOfFloat = percShortOfFloat

    def set_perc_short_of_outstanding(self, percShortOfOutstanding):
        self.__mPercShortOfOutstanding = percShortOfOutstanding

    def set_trailing_price_earnings(self, trailingPriceEarnings):
        self.__mTrailingPriceEarnings = trailingPriceEarnings

    def set_forward_price_earnings(self, forwardPriceEarnings):
        self.__mForwardPriceEarnings = forwardPriceEarnings

    def set_peg_ratio_five_years(self, pEGRatioFiveYears):
        self.__mPEGRatioFiveYears = pEGRatioFiveYears

    def set_price_to_sales(self, priceToSales):
        self.__mPriceToSales = priceToSales

    def set_price_to_book(self, priceToBook):
        self.__mPriceToBook = priceToBook

    def set_return_on_equity(self, returnOnEquity):
        self.__mReturnOnEquity = returnOnEquity

    def set_diluted_eps(self, dilutedEPS):
        self.__mDilutedEPS = dilutedEPS

    def set_book_value_per_share(self, bookValuePerShare):
        self.__mBookValuePerShare = bookValuePerShare

    def set_one_year_target_estimated(self, oneYearTargetEstimated):
        self.__mOneYearTargetEstimated = oneYearTargetEstimated

    def set_beta(self, beta):
        self.__mBeta = beta

    def set_fifty_days_moving_avg(self, fiftyDaysMovingAvg):
        self.__mFiftyDaysMovingAvg = fiftyDaysMovingAvg

    def set_two_hundreds_days_moving_avg(self, twoHundredsDaysMovingAvg):
        self.__mTwoHundredsDaysMovingAvg = twoHundredsDaysMovingAvg

    def set_last_split_factor(self, lastSplitFactor):
        self.__mLastSplitFactor = lastSplitFactor

    def set_last_split_date(self, lastSplitDate):
        self.__mLastSplitDate = lastSplitDate

    def set_net_income_to_common_shares(self, netIncomeToCommonShares):
        self.__mNetIncomeToCommonShares = netIncomeToCommonShares

    def set_has_pre_post_market_data(self, hasPrePostMarketData):
        self.__mHasPrePostMarketData = hasPrePostMarketData

    def set_ex_dividend_date(self, date):
        self.__mExDividendDate = date

    def set_dividend_date(self, date):
        self.__mDividendDate = date

    def set_dividend(self, dividend):
        self.__mDividend = dividend

    def set_payout_ratio(self, payoutRatio):
        self.__mPayoutRatio = payoutRatio

    def set_forward_annual_dividend_rate(self, rate):
        self.__mForwardAnnualDividendRate = rate

    def set_perc_forward_annual_dividend_yeld(self, yeld):
        self.__mPercForwardAnnualDividendYeld = yeld

    def set_trailing_annual_dividend_rate(self, rate):
        self.__mTrailingAnnualDividendRate = rate

    def set_trailing_annual_dividend_yeld(self, yeld):
        self.__mTrailingAnnualDividendYeld = yeld

    def set_five_year_avg_dividend_yeld(self, yeld):
        self.__mFiveYearAvgDividendYeld = yeld

    def set_dividend_rate(self, rate):
        self.__mDividendRate = rate

    def set_enterprise_value(self, enterpriseValue):
	    self.__mEnterpriseValue = enterpriseValue

    def set_pe_ratio(self, peRatio):
        self.__mPeRatio = peRatio

    def set_peg_ratio(self, pegRatio):
        self.__mPegRatio = pegRatio

    def set_pb_ratio(self, pbRatio):
        self.__mPbRatio = pbRatio

    def set_enterprises_value_revenue_ratio(self, enterprisesValueRevenueRatio):
        self.__mEnterprisesValueRevenueRatio = enterprisesValueRevenueRatio

    def set_enterprises_value_ebitda_ratio(self, enterprisesValueEBITDARatio):
        self.__mEnterprisesValueEBITDARatio = enterprisesValueEBITDARatio

    def set_average_analyst_rating(self, averageAnalystRating):
	    self.__mAverageAnalystRating = averageAnalystRating

    def set_market_change_percent(self, marketChangePercent):
        self.__mMarketChangePercent = marketChangePercent

    def set_pre_market_price(self, price):
        self.__mPreMarketPrice = price

    def set_post_market_change_percent(self, postMarketChangePercent):
        self.__mPostMarketChangePercent = postMarketChangePercent

    def set_post_market_time(self, postMarketTime):
        self.__mPostMarketTime = postMarketTime

    def set_post_market_price(self, postMarketPrice):
        self.__mPostMarketPrice = postMarketPrice

    def set_post_market_change(self, postMarketChange):
        self.__mPostMarketChange = postMarketChange

    def set_earnings_timestamp(self, earningsTimestamp):
        self.__mEarningsTimestamp = earningsTimestamp

    def set_eps_trailing_twelve_months(self, epsTralingTwelveMonths):
	    self.__mEpsTrailingTwelveMonths = epsTralingTwelveMonths

    def set_eps_forward(self, epsForward):
        self.__mEpsForward = epsForward

    def set_eps_current_year(self, epsCurrentYear):
        self.__mEpsCurrentYear = epsCurrentYear

    def set_price_eps_current_year_ratio(self, priceEpsCurrentYearRatio):
        self.__mPriceEpsCurrentYearRatio = priceEpsCurrentYearRatio
#endregion

#region - Public Methods
#region - Store Data Methods
    @staticmethod
    def store_data_list(l):
        BaseClass.store_data_list(l, DataFilenames.FILENAME_STOCK_DATA)

    def add_to_stored_data_list(self):
        BaseClass.add_to_stored_data_list(self, DataFilenames.FILENAME_STOCK_DATA)

    @staticmethod
    def get_stored_data():
        return BaseClass.get_stored_data(DataFilenames.FILENAME_STOCK_DATA)
#endregion
#endregion


    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Stock.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mAsk: {self.__mAsk}\n"\
                f"#- __mAskSize: {self.__mAskSize}\n"\
                f"#- __mBid: {self.__mBid}\n"\
                f"#- __mBidSize: {self.__mBidSize}\n"\
                f"#- __mCompany: {self.__mCompany}\n"\
                f"#- __mSharesFloat: {self.__mSharesFloat}\n"\
                f"#- __mSharesOutstanding: {self.__mSharesOutstanding}\n"\
                f"#- __mPercSharesInsiders: {self.__mPercSharesInsiders}\n"\
                f"#- __mPercSharesInstitutions: {self.__mPercSharesInstitutions}\n"\
                f"#- __mSharesShort: {self.__mSharesShort}\n"\
                f"#- __mShortRatio: {self.__mShortRatio}\n"\
                f"#- __mPercShortOfFloat: {self.__mPercShortOfFloat}\n"\
                f"#- __mPercShortOfOutstanding: {self.__mPercShortOfOutstanding}\n"\
                f"#- __mTrailingPriceEarnings: {self.__mTrailingPriceEarnings}\n"\
                f"#- __mForwardPriceEarnings: {self.__mForwardPriceEarnings}\n"\
                f"#- __mPEGRatioFiveYears: {self.__mPEGRatioFiveYears}\n"\
                f"#- __mPriceToSales: {self.__mPriceToSales}\n"\
                f"#- __mPriceToBook: {self.__mPriceToBook}\n"\
                f"#- __mReturnOnEquity: {self.__mReturnOnEquity}\n"\
                f"#- __mDilutedEPS: {self.__mDilutedEPS}\n"\
                f"#- __mBookValuePerShare: {self.__mBookValuePerShare}\n"\
                f"#- __mOneYearTargetEstimated: {self.__mOneYearTargetEstimated}\n"\
                f"#- __mBeta: {self.__mBeta}\n"\
                f"#- __mFiftyDaysMovingAvg: {self.__mFiftyDaysMovingAvg}\n"\
                f"#- __mTwoHundredsDaysMovingAvg: {self.__mTwoHundredsDaysMovingAvg}\n"\
                f"#- __mLastSplitFactor: {self.__mLastSplitFactor}\n"\
                f"#- __mLastSplitDate: {self.__mLastSplitDate}\n"\
                f"#- __mNetIncomeToCommonShares: {self.__mNetIncomeToCommonShares}\n"\
                f"#- __mHasPrePostMarketData: {self.__mHasPrePostMarketData}\n"\
                f"#- __mExDividendDate: {self.__mExDividendDate}\n"\
                f"#- __mDividendDate: {self.__mDividendDate}\n"\
                f"#- __mDividend: {self.__mDividend}\n"\
                f"#- __mPayoutRatio: {self.__mPayoutRatio}\n"\
                f"#- __mForwardAnnualDividendRate: {self.__mForwardAnnualDividendRate}\n"\
                f"#- __mPercForwardAnnualDividendYeld: {self.__mPercForwardAnnualDividendYeld}\n"\
                f"#- __mTrailingAnnualDividendRate: {self.__mTrailingAnnualDividendRate}\n"\
                f"#- __mTrailingAnnualDividendYeld: {self.__mTrailingAnnualDividendYeld}\n"\
                f"#- __mFiveYearAvgDividendYeld: {self.__mFiveYearAvgDividendYeld}\n"\
                f"#- __mDividendRate: {self.__mDividendRate}\n"\
                f"#- __mEnterpriseValue: {self.__mEnterpriseValue}\n"\
                f"#- __mPeRatio: {self.__mPeRatio}\n"\
                f"#- __mPegRatio: {self.__mPegRatio}\n"\
                f"#- __mPbRatio: {self.__mPbRatio}\n"\
                f"#- __mEnterprisesValueRevenueRatio: {self.__mEnterprisesValueRevenueRatio}\n"\
                f"#- __mEnterprisesValueEBITDARatio: {self.__mEnterprisesValueEBITDARatio}\n"\
                f"#- __mAverageAnalystRating: {self.__mAverageAnalystRating}\n"\
                f"#- __mMarketChangePercent: {self.__mMarketChangePercent}\n"\
                f"#- __mPreMarketPrice: {self.__mPreMarketPrice}\n"\
                f"#- __mPostMarketChangePercent: {self.__mPostMarketChangePercent}\n"\
                f"#- __mPostMarketTime: {self.__mPostMarketTime}\n"\
                f"#- __mPostMarketPrice: {self.__mPostMarketPrice}\n"\
                f"#- __mPostMarketChange: {self.__mPostMarketChange}\n"\
                f"#- __mEarningsTimestamp: {self.__mEarningsTimestamp}\n"\
                f"#- __mEpsTrailingTwelveMonths: {self.__mEpsTrailingTwelveMonths}\n"\
                f"#- __mEpsForward: {self.__mEpsForward}\n"\
                f"#- __mEpsCurrentYear: {self.__mEpsCurrentYear}\n"\
                f"#- __mPriceEpsCurrentYearRatio: {self.__mPriceEpsCurrentYearRatio}\n"\
                "####################"
    
