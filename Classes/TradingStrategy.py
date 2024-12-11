from Classes.BaseClasses.BaseTradingStrategy import BaseTradingStrategy
from Classes.BaseClasses.BaseClass import BaseClass
from Resources.Constants import DataFilenames

class TradingStrategy(BaseTradingStrategy):

    __mMaxDayChange = None
    __mMinDayChange = None
    __mMaxMarketCap = None
    __mMinMarketCap = None
    __mMaxDayRange = None
    __mMinDayRange = None
    __mMaxWeekRange = None
    __mMinWeekRange = None
    __mMaxMonthRange = None
    __mMinMonthRange = None
    __mMaxYearRange = None
    __mMinYearRange = None
    __mMaxDayVolume = None
    __mMinDayVolume = None
    __mMaxCompanyValue = None
    __mMinCompanyValue = None
    __mMaxRatioCompanyValueMarketCap = None
    __mMinRatioCompanyValueMarketCap = None
    __mMaxBeta = None
    __mMinBeta = None
    __mMaxRatioPE = None
    __mMinRatioPE = None
    __mMaxEPS = None
    __mMinEPS = None
    __mMaxYearTarget = None
    __mMinYearTarget = None
    __mMaxTrailingPE = None
    __mMinTrailingPE = None
    __mMaxForwardPE = None
    __mMinForwardPE = None
    __mMaxPegRatio = None
    __mMinPegRatio = None
    __mMaxPriceSales = None
    __mMinPriceSales = None
    __mMaxPriceBook = None
    __mMinPriceBook = None
    __mMaxCompanyValueRevenue = None
    __mMinCompanyValueRevenue = None
    __mMaxCompanyValueEbitda = None
    __mMinCompanyValueEbitda = None

    def __init__(self, id, name):
        super().__init__(id, name)

    #region - Get Methods
    def get_max_day_change(self):
        return self.__mMaxDayChange

    def get_min_day_change(self):
        return self.__mMinDayChange

    def get_max_market_cap(self):
        return self.__mMaxMarketCap

    def get_min_market_cap(self):
        return self.__mMinMarketCap

    def get_max_day_range(self):
        return self.__mMaxDayRange

    def get_min_day_range(self):
        return self.__mMinDayRange

    def get_max_week_range(self):
        return self.__mMaxWeekRange

    def get_min_week_range(self):
        return self.__mMinWeekRange

    def get_max_month_range(self):
        return self.__mMaxMonthRange

    def get_min_month_range(self):
        return self.__mMinMonthRange

    def get_max_year_range(self):
        return self.__mMaxYearRange

    def get_min_year_range(self):
        return self.__mMinYearRange

    def get_max_day_volume(self):
        return self.__mMaxDayVolume

    def get_min_day_volume(self):
        return self.__mMinDayVolume

    def get_max_company_value(self):
        return self.__mMaxCompanyValue

    def get_min_company_value(self):
        return self.__mMinCompanyValue

    def get_max_ratio_company_value_market_cap(self):
        return self.__mMaxRatioCompanyValueMarketCap

    def get_min_ratio_company_value_market_cap(self):
        return self.__mMinRatioCompanyValueMarketCap

    def get_max_beta(self):
        return self.__mMaxBeta

    def get_min_beta(self):
        return self.__mMinBeta

    def get_max_ratio_pe(self):
        return self.__mMaxRatioPE

    def get_min_ratio_pe(self):
        return self.__mMinRatioPE

    def get_max_eps(self):
        return self.__mMaxEPS

    def get_min_eps(self):
        return self.__mMinEPS

    def get_max_year_target(self):
        return self.__mMaxYearTarget

    def get_min_year_target(self):
        return self.__mMinYearTarget

    def get_max_trailing_pe(self):
        return self.__mMaxTrailingPE

    def get_min_trailing_pe(self):
        return self.__mMinTrailingPE

    def get_max_forward_pe(self):
        return self.__mMaxForwardPE

    def get_min_forward_pe(self):
        return self.__mMinForwardPE

    def get_max_peg_ratio(self):
        return self.__mMaxPegRatio

    def get_min_peg_ratio(self):
        return self.__mMinPegRatio

    def get_max_price_sales(self):
        return self.__mMaxPriceSales

    def get_min_price_sales(self):
        return self.__mMinPriceSales

    def get_max_price_book(self):
        return self.__mMaxPriceBook

    def get_min_price_book(self):
        return self.__mMinPriceBook

    def get_max_company_value_revenue(self):
        return self.__mMaxCompanyValueRevenue

    def get_min_company_value_revenue(self):
        return self.__mMinCompanyValueRevenue

    def get_max_company_value_ebitda(self):
        return self.__mMaxCompanyValueEbitda

    def get_min_company_value_ebitda(self):
        return self.__mMinCompanyValueEbitda
    #endregion

    #region - Set Methods
    def set_max_day_change(self, maxDayChange):
        self.__mMaxDayChange = maxDayChange

    def set_min_day_change(self, minDayChange):
        self.__mMinDayChange = minDayChange

    def set_max_market_cap(self, maxMarketCap):
        self.__mMaxMarketCap = maxMarketCap

    def set_min_market_cap(self, minMarketCap):
        self.__mMinMarketCap = minMarketCap

    def set_max_day_range(self, maxDayRange):
        self.__mMaxDayRange = maxDayRange

    def set_min_day_range(self, minDayRange):
        self.__mMinDayRange = minDayRange

    def set_max_week_range(self, maxWeekRange):
        self.__mMaxWeekRange = maxWeekRange

    def set_min_week_range(self, minWeekRange):
        self.__mMinWeekRange = minWeekRange

    def set_max_month_range(self, maxMonthRange):
        self.__mMaxMonthRange = maxMonthRange

    def set_min_month_range(self, minMonthRange):
        self.__mMinMonthRange = minMonthRange

    def set_max_year_range(self, maxYearRange):
        self.__mMaxYearRange = maxYearRange

    def set_min_year_range(self, minYearRange):
        self.__mMinYearRange = minYearRange

    def set_max_day_volume(self, maxDayVolume):
        self.__mMaxDayVolume = maxDayVolume

    def set_min_day_volume(self, minDayVolume):
        self.__mMinDayVolume = minDayVolume

    def set_max_company_value(self, maxCompanyValue):
        self.__mMaxCompanyValue = maxCompanyValue

    def set_min_company_value(self, minCompanyValue):
        self.__mMinCompanyValue = minCompanyValue

    def set_max_ratio_company_value_market_cap(self, maxRatioCompanyValueMarketCap):
        self.__mMaxRatioCompanyValueMarketCap = maxRatioCompanyValueMarketCap

    def set_min_ratio_company_value_market_cap(self, minRatioCompanyValueMarketCap):
        self.__mMinRatioCompanyValueMarketCap = minRatioCompanyValueMarketCap

    def set_max_beta(self, maxBeta):
        self.__mMaxBeta = maxBeta

    def set_min_beta(self, minBeta):
        self.__mMinBeta = minBeta

    def set_max_ratio_pe(self, maxRatioPE):
        self.__mMaxRatioPE = maxRatioPE

    def set_min_ratio_pe(self, minRatioPE):
        self.__mMinRatioPE = minRatioPE

    def set_max_eps(self, maxEPS):
        self.__mMaxEPS = maxEPS

    def set_min_eps(self, minEPS):
        self.__mMinEPS = minEPS

    def set_max_year_target(self, maxYearTarget):
        self.__mMaxYearTarget = maxYearTarget

    def set_min_year_target(self, minYearTarget):
        self.__mMinYearTarget = minYearTarget

    def set_max_trailing_pe(self, maxTrailingPE):
        self.__mMaxTrailingPE = maxTrailingPE

    def set_min_trailing_pe(self, minTrailingPE):
        self.__mMinTrailingPE = minTrailingPE

    def set_max_forward_pe(self, maxForwardPE):
        self.__mMaxForwardPE = maxForwardPE

    def set_min_forward_pe(self, minForwardPE):
        self.__mMinForwardPE = minForwardPE

    def set_max_peg_ratio(self, maxPegRatio):
        self.__mMaxPegRatio = maxPegRatio

    def set_min_peg_ratio(self, minPegRatio):
        self.__mMinPegRatio = minPegRatio

    def set_max_price_sales(self, maxPriceSales):
        self.__mMaxPriceSales = maxPriceSales

    def set_min_price_sales(self, minPriceSales):
        self.__mMinPriceSales = minPriceSales

    def set_max_price_book(self, maxPriceBook):
        self.__mMaxPriceBook = maxPriceBook

    def set_min_price_book(self, minPriceBook):
        self.__mMinPriceBook = minPriceBook

    def set_max_company_value_revenue(self, maxCompanyValueRevenue):
        self.__mMaxCompanyValueRevenue = maxCompanyValueRevenue

    def set_min_company_value_revenue(self, minCompanyValueRevenue):
        self.__mMinCompanyValueRevenue = minCompanyValueRevenue

    def set_max_company_value_ebitda(self, maxCompanyValueEbitda):
        self.__mMaxCompanyValueEbitda = maxCompanyValueEbitda

    def set_min_company_value_ebitda(self, minCompanyValueEbitda):
        self.__mMinCompanyValueEbitda = minCompanyValueEbitda
    #endregion

#region - Public Methods
#region - Store Data Methods
    @staticmethod
    def store_data_list(l):
        BaseClass.store_data_list(l, DataFilenames.FILENAME_TRADING_STRATEGIES)

    def add_to_stored_data_list(self):
        BaseClass.add_to_stored_data_list(self, DataFilenames.FILENAME_TRADING_STRATEGIES)

    @staticmethod
    def get_stored_data():
        return BaseClass.get_stored_data(DataFilenames.FILENAME_TRADING_STRATEGIES)
#endregion
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {TradingStrategy.__name__}\n"\
                "####################\n"\
                f"{super().__str__()}\n"\
                f"#- __mMaxDayChange: {self.__mMaxDayChange}\n"\
                f"#- __mMinDayChange: {self.__mMinDayChange}\n"\
                f"#- __mMaxMarketCap: {self.__mMaxMarketCap}\n"\
                f"#- __mMinMarketCap: {self.__mMinMarketCap}\n"\
                f"#- __mMaxDayRange: {self.__mMaxDayRange}\n"\
                f"#- __mMinDayRange: {self.__mMinDayRange}\n"\
                f"#- __mMaxWeekRange: {self.__mMaxWeekRange}\n"\
                f"#- __mMinWeekRange: {self.__mMinWeekRange}\n"\
                f"#- __mMaxMonthRange: {self.__mMaxMonthRange}\n"\
                f"#- __mMinMonthRange: {self.__mMinMonthRange}\n"\
                f"#- __mMaxYearRange: {self.__mMaxYearRange}\n"\
                f"#- __mMinYearRange: {self.__mMinYearRange}\n"\
                f"#- __mMaxDayVolume: {self.__mMaxDayVolume}\n"\
                f"#- __mMinDayVolume: {self.__mMinDayVolume}\n"\
                f"#- __mMaxCompanyValue: {self.__mMaxCompanyValue}\n"\
                f"#- __mMinCompanyValue: {self.__mMinCompanyValue}\n"\
                f"#- __mMaxRatioCompanyValueMarketCap: {self.__mMaxRatioCompanyValueMarketCap}\n"\
                f"#- __mMinRatioCompanyValueMarketCap: {self.__mMinRatioCompanyValueMarketCap}\n"\
                f"#- __mMaxBeta: {self.__mMaxBeta}\n"\
                f"#- __mMinBeta: {self.__mMinBeta}\n"\
                f"#- __mMaxRatioPE: {self.__mMaxRatioPE}\n"\
                f"#- __mMinRatioPE: {self.__mMinRatioPE}\n"\
                f"#- __mMaxEPS: {self.__mMaxEPS}\n"\
                f"#- __mMinEPS: {self.__mMinEPS}\n"\
                f"#- __mMaxYearTarget: {self.__mMaxYearTarget}\n"\
                f"#- __mMinYearTarget: {self.__mMinYearTarget}\n"\
                f"#- __mMaxTrailingPE: {self.__mMaxTrailingPE}\n"\
                f"#- __mMinTrailingPE: {self.__mMinTrailingPE}\n"\
                f"#- __mMaxForwardPE: {self.__mMaxForwardPE}\n"\
                f"#- __mMinForwardPE: {self.__mMinForwardPE}\n"\
                f"#- __mMaxPegRatio: {self.__mMaxPegRatio}\n"\
                f"#- __mMinPegRatio: {self.__mMinPegRatio}\n"\
                f"#- __mMaxPriceSales: {self.__mMaxPriceSales}\n"\
                f"#- __mMinPriceSales: {self.__mMinPriceSales}\n"\
                f"#- __mMaxPriceBook: {self.__mMaxPriceBook}\n"\
                f"#- __mMinPriceBook: {self.__mMinPriceBook}\n"\
                f"#- __mMaxCompanyValueRevenue: {self.__mMaxCompanyValueRevenue}\n"\
                f"#- __mMinCompanyValueRevenue: {self.__mMinCompanyValueRevenue}\n"\
                f"#- __mMaxCompanyValueEbitda: {self.__mMaxCompanyValueEbitda}\n"\
                f"#- __mMinCompanyValueEbitda: {self.__mMinCompanyValueEbitda}\n"\
                "####################"
