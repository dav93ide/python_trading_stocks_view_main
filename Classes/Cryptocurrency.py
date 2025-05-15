from Classes.BaseClasses.BaseAsset import BaseAsset

class Cryptocurrency(BaseAsset):

    __mImageUrl = None
    __mCategory = None
    __mStartDate = None
    __mAlgorithm = None
    __mCirculatingSupply = None
    __mMaxSupply = None
    __mMarketDominance = None
    __mMarketRank = None
    __mMarketChangePercent = None
    __mFiftyTwoWeekLowChangePercent = None
    __mFiftyTwoWeekHighChangePercent = None
    __mFiftyTwoWeekLowChange = None
    __mFiftyTwoWeekHighChange = None
    __mRegularMarketDayRange = None
    __mVolumeTwentyFourHours = None
    __mVolumeAllCurrencies = None

    def __init__(self, id):
        super().__init__(id)

#region - Getter Methods
    def get_img_url(self):
        return self.__mImageUrl

    def get_category(self):
        return self.__mCategory 

    def get_start_date(self):
        return self.__mStartDate 

    def get_algorithm(self):
        return self.__mAlgorithm 

    def get_circulating_supply(self):
        return self.__mCirculatingSupply 

    def get_max_supply(self):
        return self.__mMaxSupply 

    def get_market_dominance(self):
        return self.__mMarketDominance 

    def get_market_rank(self):
        return self.__mMarketRank 

    def get_market_change_percent(self):
        return self.__mMarketChangePercent

    def get_fifty_two_week_low_change_percent(self):
        return self.__mstFifityTwoWeeksPercChange

    def get_fifty_two_week_high_change_percent(self):
        return self.__mFiftyTwoWeekHighChangePercent

    def get_fifty_two_week_low_change(self):
        return self.__mFiftyTwoWeekLowChange

    def get_fifty_two_week_high_change(self):
        return self.__mFiftyTwoWeekHighChange

    def get_regular_market_day_range(self):
        return self.__mRegularMarketDayRange
        
    def get_volume_twenty_four_hours(self):
        return self.__mVolumeTwentyFourHours

    def get_volume_all_currencies(self):
        return self.__mVolumeAllCurrencies
#endregion

#region - Setter Methods
    def set_image_url(self, url):
        self.__mImageUrl = url

    def set_category(self, category):
        self.__mCategory  = category 

    def set_start_date(self, startDate):
        self.__mStartDate  = startDate 

    def set_algorithm(self, algorithm):
        self.__mAlgorithm  = algorithm 

    def set_circulating_supply(self, circulatingSupply):
        self.__mCirculatingSupply  = circulatingSupply 

    def set_max_supply(self, maxSupply):
        self.__mMaxSupply  = maxSupply 

    def set_market_dominance(self, marketDominance):
        self.__mMarketDominance  = marketDominance 

    def set_market_rank(self, marketRank):
        self.__mMarketRank  = marketRank 

    def set_market_change_percent(self, percent):
        self.__mMarketChangePercent = percent

    def set_fifty_two_week_low_change_percent(self, percent):
        self.__mFiftyTwoWeekLowChangePercent = percent

    def set_fifty_two_week_high_change_percent(self, percent):
        self.__mFiftyTwoWeekHighChangePercent = percent

    def set_fifty_two_week_low_change(self, change):
        self.__mFiftyTwoWeekLowChange = change

    def set_fifty_two_week_high_change(self, change):
        self.__mFiftyTwoWeekHighChange = change

    def set_regular_market_day_range(self, rng):
        self.__mRegularMarketDayRange = rng

    def set_volume_twenty_four_hours(self, volume):
        self.__mVolumeTwentyFourHours = volume

    def set_volume_all_currencies(self, volume):
        self.__mVolumeAllCurrencies = volume
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {ETF.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mImageUrl: {self.__mImageUrl}\n"\
                f"#- __mCategory: {self.__mCategory}\n"\
                f"#- __mStartDate: {self.__mStartDate}\n"\
                f"#- __mAlgorithm: {self.__mAlgorithm}\n"\
                f"#- __mCirculatingSupply: {self.__mCirculatingSupply}\n"\
                f"#- __mMaxSupply: {self.__mMaxSupply}\n"\
                f"#- __mMarketDominance: {self.__mMarketDominance}\n"\
                f"#- __mMarketRank: {self.__mMarketRank}\n"\
                f"#- __mMarketChangePercent: {self.__mMarketChangePercent}\n"\
                f"#- __mFiftyTwoWeekLowChangePercent: {self.__mFiftyTwoWeekLowChangePercent}\n"\
                f"#- __mFiftyTwoWeekHighChangePercent: {self.__mFiftyTwoWeekHighChangePercent}\n"\
                f"#- __mFiftyTwoWeekLowChange: {self.__mFiftyTwoWeekLowChange}\n"\
                f"#- __mFiftyTwoWeekHighChange: {self.__mFiftyTwoWeekHighChange}\n"\
                f"#- __mRegularMarketDayRange: {self.__mRegularMarketDayRange}\n"\
                f"#- __mVolumeTwentyFourHours: {self.__mVolumeTwentyFourHours}\n"\
                f"#- __mVolumeAllCurrencies: {self.__mVolumeAllCurrencies}\n"\
                "####################"
