from Resources.Constants import AssetType
from Classes.PriceHistory import PriceHistory
from Classes.CountDailyLongShort import CountDailyLongShort
from Classes.Exchange import Exchange
from Classes.BaseClasses.BaseClass import BaseClass

class BaseAsset(BaseClass):

    __mName = None
    __mSign = None
    __mType: AssetType = None
    __mExchange: Exchange = None
    __mPrice = None
    __mOpenPrice = None
    __mPricePreviousClose = None
    __mMarketCap = None
    __mFirstTradeDate = None
    __mVolume = None
    __mAvgVolumeTenDays = None
    __mAvgVolumeThreeMonths = None
    __mAvgVolumeFiftyTwoWeeks = None
    __mDayRange = None
    __mDayMax = None
    __mDayMin = None
    __mDayPercChange = None
    __mFiftyTwoWeeksRange = None
    __mFiftyTwoWeeksHigh = None
    __mFifityTwoWeeksLow = None
    __mFiftyTwoWeeksPercChange = None
    __mPriceHistory: PriceHistory = None
    __mDailyLongShort: CountDailyLongShort = None

    def __init__(self, id):
        super().__init__(id)

#region - Getter Method
    def get_name(self):
        return self.__mName

    def get_sign(self):
        return self.__mSign

    def get_type(self):
        return self.__mType

    def get_exchange(self):
        return self.__mExchange

    def get_price(self):
        return self.__mPrice

    def get_open_price(self):
        return self.__mOpenPrice

    def get_price_previous_close(self):
        return self.__mPricePreviousClose

    def get_market_cap(self):
        return self.__mMarketCap

    def get_first_trade_date(self):
        return self.__mFirstTradeDate

    def get_volume(self):
        return self.__mVolume

    def get_avg_volume_ten_days(self):
        return self.__mAvgVolumeTenDays

    def get_avg_volume_three_months(self):
        return self.__mAvgVolumeThreeMonths

    def get_avg_volume_fifty_two_weeks(self):
        return self.__mAvgVolumeFiftyTwoWeeks

    def get_day_range(self):
        return self.__mDayRange

    def get_day_max(self):
        return self.__mDayMax

    def get_day_min(self):
        return self.__mDayMin

    def get_day_perc_change(self):
        return self.__mDayPercChange

    def get_fifty_two_weeks_range(self):
        return self.__mFiftyTwoWeeksRange

    def get_fifty_two_weeks_high(self):
        return self.__mFiftyTwoWeeksHigh

    def get_fifty_two_weeks_low(self):
        return self.__mFifityTwoWeeksLow

    def get_fifty_two_weeks_perc_change(self):
        return self.__mFiftyTwoWeeksPercChange

    def get_price_history(self):
        return self.__mPriceHistory

    def get_daily_long_short(self):
        return self.__mDailyLongShort
#endregion

#region - Set Methods
    def set_name(self, name):
        self.__mName = name

    def set_sign(self, sign):
        self.__mSign = sign

    def set_type(self, type):
        self.__mType = type

    def set_exchange(self, exchange):
        self.__mExchange = exchange

    def set_price(self, price):
        self.__mPrice = price

    def set_open_price(self, openPrice):
        self.__mOpenPrice = openPrice

    def set_price_previous_close(self, pricePreviousClose):
        self.__mPricePreviousClose = pricePreviousClose

    def set_market_cap(self, marketCap):
        self.__mMarketCap = marketCap

    def set_first_trade_date(self, firstTradeDate):
        self.__mFirstTradeDate = firstTradeDate

    def set_volume(self, volume):
        self.__mVolume = volume

    def set_avg_volume_ten_days(self, avgVolumeTenDays):
        self.__mAvgVolumeTenDays = avgVolumeTenDays

    def set_avg_volume_three_months(self, avgVolumeThreeMonths):
        self.__mAvgVolumeThreeMonths = avgVolumeThreeMonths

    def set_avg_volume_fifty_two_weeks(self, avgVolumeFiftyTwoWeeks):
        self.__mAvgVolumeFiftyTwoWeeks = avgVolumeFiftyTwoWeeks

    def set_day_range(self, dayRange):
        self.__mDayRange = dayRange

    def set_day_max(self, dayMax):
        self.__mDayMax = dayMax

    def set_day_min(self, dayMin):
        self.__mDayMin = dayMin

    def set_day_perc_change(self, dayPercChange):
        self.__mDayPercChange = dayPercChange

    def set_fifty_two_weeks_range(self, fiftyTwoWeeksRange):
        self.__mFiftyTwoWeeksRange = fiftyTwoWeeksRange

    def set_fifty_two_weeks_high(self, fiftyTwoWeeksHigh):
        self.__mFiftyTwoWeeksHigh = fiftyTwoWeeksHigh

    def set_fifty_two_weeks_low(self, fifityTwoWeeksLow):
        self.__mFifityTwoWeeksLow = fifityTwoWeeksLow

    def set_fifty_two_weeks_perc_change(self, fiftyTwoWeeksPercChange):
        self.__mFiftyTwoWeeksPercChange = fiftyTwoWeeksPercChange

    def set_price_history(self, priceHistory):
        self.__mPriceHistory = priceHistory

    def set_daily_long_short(self, dailyLongShort):
        self.__mDailyLongShort = dailyLongShort
#endregion


    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {BaseAsset.__name__}\n"\
                f"{super().__str__()} \n"\
                f"#- __mName: {str(self.__mName)}\n"\
                f"#- __mSign: {self.__mSign}\n"\
                f"#- __mType: {self.__mType}\n"\
                f"#- __mExchange: {self.__mExchange}\n"\
                f"#- __mPrice: {self.__mPrice}\n"\
                f"#- __mOpenPrice: {self.__mOpenPrice}\n"\
                f"#- __mPricePreviousClose: {self.__mPricePreviousClose}\n"\
                f"#- __mMarketCap: {self.__mMarketCap}\n"\
                f"#- __mFirstTradeDate: {self.__mFirstTradeDate}\n"\
                f"#- __mVolume: {self.__mVolume}\n"\
                f"#- __mAvgVolumeTenDays: {self.__mAvgVolumeTenDays}\n"\
                f"#- __mAvgVolumeThreeMonths: {self.__mAvgVolumeThreeMonths}\n"\
                f"#- __mAvgVolumeFiftyTwoWeeks: {self.__mAvgVolumeFiftyTwoWeeks}\n"\
                f"#- __mDayRange: {self.__mDayRange}\n"\
                f"#- __mDayMax: {self.__mDayMax}\n"\
                f"#- __mDayMin: {self.__mDayMin}\n"\
                f"#- __mDayPercChange: {self.__mDayPercChange}\n"\
                f"#- __mFiftyTwoWeeksRange: {self.__mFiftyTwoWeeksRange}\n"\
                f"#- __mFiftyTwoWeeksHigh: {self.__mFiftyTwoWeeksHigh}\n"\
                f"#- __mFifityTwoWeeksLow: {self.__mFifityTwoWeeksLow}\n"\
                f"#- __mFiftyTwoWeeksPercChange: {self.__mFiftyTwoWeeksPercChange}\n"\
                f"#- __mPriceHistory: {self.__mPriceHistory}\n"\
                f"#- __mDailyLongShort: {self.__mDailyLongShort}\n"\
                "####################"
