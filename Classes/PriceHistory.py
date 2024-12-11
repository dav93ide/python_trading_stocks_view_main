from Classes.BaseClasses.BaseClass import BaseClass

class PriceHistory(BaseClass):
    
    __mPrice = None
    __mDate = None
    __mPercVariation = None
    __mAssetId: str = None

    def __init__(self, id):
        super().__init__(id)

#region - Getter Methods
    def get_price(self):
        return self.__mPrice

    def get_date(self):
        return self.__mDate

    def get_asset_id(self):
        return self.__mAssetId
#endregion

#region - Setter Methods
    def set_price(self, price):
        self.__mPrice = price

    def set_date(self, date):
        self.__mDate = date

    def set_perc_variation(self, perc):
        self.__mPercVariation = perc

    def set_asset_id(self, id):
        self.__mAssetId = id
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {PriceHistory.__name__}\n"\
                f"{super().__str__()} \n"\
                f"#- __mPrice: {str(self.__mPrice)}\n"\
                f"#- __mDate: {self.__mDate}\n"\
                f"#- __mPercVariation: {self.__mPercVariation}\n"\
                f"#- __mAssetId: {self.__mAssetId}\n"\
                "####################"
