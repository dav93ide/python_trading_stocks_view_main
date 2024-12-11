from Classes.BaseClasses.BaseClass import BaseClass

class Investment(BaseClass):

    __id = None
    __mAsset = None
    __mTotCapitalInvested = None
    __mTotActualCapital = None
    __mTotPercCapitalInvested = None
    __mTotPercActualCapital = None
    __mTotPercPL = None
    __mTotPL = None
    __mOpenPositions = []


    def __init__(self, id):
        self.__id = id
        self.__mOpenPositions = []

    # Getter Methods
    def get_id(self):
        return self.__id

    def get_assets(self):
        return self.__mAsset

    def get_tot_capital_invested(self):
        return self.__mTotCapitalInvested

    def get_tot_actual_capital(self):
        return self.__mTotActualCapital

    def get_tot_perc_capital_invested(self):
        return self.__mTotPercCapitalInvested

    def get_tot_perc_actual_capital(self):
        return self.__mTotPercActualCapital

    def get_tot_perc_pl(self):
        return self.__mTotPercPL

    def get_tot_pl(self):
        return self.__mTotPL

    def get_open_positions(self):
        return self.__mOpenPositions

    # Setter Methods
    def set_id(self, id):
        self.__id = id

    def set_assets(self, asset):
        self.__mAsset = asset

    def set_tot_capital_invested(self, tot):
        self.__mTotCapitalInvested = tot

    def set_tot_actual_capital(self, tot):
        self.__mTotActualCapital = tot

    def set_tot_perc_capital_invested(self, perc):
        self.__mTotPercCapitalInvested = perc

    def set_tot_perc_actual_capital(self, perc):
        self.__mTotPercActualCapital = perc

    def set_tot_perc_pl(self, perc):
        self.__mTotPercPL = perc

    def set_tot_pl(self, pl):
        self.__mTotPL = pl

    def set_open_positions(self, pos):
        self.__mOpenPositions = pos

    # To String
    def __str__(self):
        return "####################\n"\
                f"# {Investment.__name__}\n"\
                "####################\n"\
                f"#- __id: {self.__id}\n"\
                f"#- __mAsset: {self.__mAsset}\n"\
                f"#- __mTotCapitalInvested: {self.__mTotCapitalInvested}\n"\
                f"#- __mTotActualCapital: {self.__mTotActualCapital}\n"\
                f"#- __mTotPercCapitalInvested: {self.__mTotPercCapitalInvested}\n"\
                f"#- __mTotPercActualCapital: {self.__mTotPercActualCapital}\n"\
                f"#- __mTotPercPL: {self.__mTotPercPL}\n"\
                f"#- __mTotPL: {self.__mTotPL}\n"\
                f"#- __mOpenPositions: {self.__mOpenPositions}\n"\
                "####################"