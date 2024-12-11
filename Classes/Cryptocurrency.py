from Classes import BaseAsset

class Cryptocurrency(BaseAsset):

    __mCategory = None
    __mStartDate = None
    __mAlgorithm = None
    __mCirculatingSupply = None
    __mMaxSupply = None
    __mMarketDominance = None
    __mMarketRank = None

    def __init__(self, id):
        super().__init__(id)

#region - Getter Methods
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
#endregion

#region - Setter Methods
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
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {ETF.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mCategory: {self.__mCategory}\n"\
                f"#- __mStartDate: {self.__mStartDate}\n"\
                f"#- __mAlgorithm: {self.__mAlgorithm}\n"\
                f"#- __mCirculatingSupply: {self.__mCirculatingSupply}\n"\
                f"#- __mMaxSupply: {self.__mMaxSupply}\n"\
                f"#- __mMarketDominance: {self.__mMarketDominance}\n"\
                f"#- __mMarketRank: {self.__mMarketRank}\n"\
                "####################"
