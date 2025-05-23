

class FilterSearchCryptoPanel():

    __mMaxPrice = None
    __mMinPrice = None
    __mMaxVolume = None
    __mMinVolume = None

    __mMaxPriceMover = None
    __mMinPriceMover = None
    __mMaxVolumeMover = None
    __mMinVolumeMover = None

    __mValueMaxMover = None
    __mValueMinMover = None

    __mMoverAboveZero = None
    __mMoverAboveFifty = None
    __mMoverAboveHundred = None
    __mMoverBelowZero = None
    __mMoverBelowFifty = None

    __mMoverAboveZeroToTen = None
    __mMoverAboveTenToTwenty = None
    __mMoverAboveTwentyToThirty = None
    __mMoverAboveThirtyToFourty = None

    __mMoverBelowZeroToTen = None
    __mMoverBelowTenToTwenty = None
    __mMoverBelowTwentyToThirty = None
    __mMoverBelowThirtyToFourty = None

    __mFiftyValueMaxMover = None
    __mFiftyValueMinMover = None

    __mMoverFiftyWeeksAboveZero = None
    __mMoverFiftyWeeksAboveFifty = None
    __mMoverFiftyWeeksAboveHundred = None
    __mMoverFiftyWeeksBelowZero = None
    __mMoverFiftyWeeksBelowFifty = None

    __mMoverFiftyWeeksAboveZeroToTen = None
    __mMoverFiftyWeeksAboveTenToTwenty = None
    __mMoverFiftyWeeksAboveTwentyThirty = None
    __mMoverFiftyWeeksAboveThirtyFourty = None

    __mMoverFiftyWeeksBelowZeroToTen = None
    __mMoverFiftyWeeksBelowTenToTwenty = None
    __mMoverFiftyWeeksBelowTwentyThirty = None
    __mMoverFiftyWeeksBelowThirtyFourty = None

#region - Get Methods
    def get_max_price(self):
        return self.__mMaxPrice

    def get_min_price(self):
        return self.__mMinPrice

    def get_max_volume(self):
        return self.__mMaxVolume

    def get_min_volume(self):
        return self.__mMinVolume

    def get_max_price_mover(self):
        return self.__mMaxPriceMover

    def get_min_price_mover(self):
        return self.__mMinPriceMover

    def get_max_volume_mover(self):
        return self.__mMaxVolumeMover

    def get_min_volume_mover(self):
        return self.__mMinVolumeMover

    def get_value_max_mover(self):
	    return self.__mValueMaxMover

    def get_value_min_mover(self):
	    return self.__mValueMinMover

    def get_mover_above_zero(self):
        return self.__mMoverAboveZero

    def get_mover_above_fifty(self):
        return self.__mMoverAboveFifty

    def get_mover_above_hundred(self):
        return self.__mMoverAboveHundred

    def get_mover_below_zero(self):
        return self.__mMoverBelowZero

    def get_mover_below_fifty(self):
        return self.__mMoverBelowFifty

    def get_mover_above_zero_to_ten(self):
        return self.__mMoverAboveZeroToTen

    def get_mover_above_ten_to_twenty(self):
        return self.__mMoverAboveTenToTwenty

    def get_mover_above_twenty_to_thirty(self):
        return self.__mMoverAboveTwentyToThirty

    def get_mover_above_thirty_to_fourty(self):
        return self.__mMoverAboveThirtyToFourty

    def get_mover_below_zero_to_ten(self):
        return self.__mMoverBelowZeroToTen

    def get_mover_below_ten_to_twenty(self):
        return self.__mMoverBelowTenToTwenty

    def get_mover_below_twenty_to_thirty(self):
        return self.__mMoverBelowTwentyToThirty

    def get_mover_below_thirty_to_fourty(self):
        return self.__mMoverBelowThirtyToFourty

    def get_fifty_value_max_mover(self):
        return self.__mFiftyValueMaxMover

    def get_fifty_value_min_mover(self):
        return self.__mFiftyValueMinMover

    def get_mover_fifty_weeks_above_zero(self):
	    return self.__mMoverFiftyWeeksAboveZero 

    def get_mover_fifty_weeks_above_fifty(self):
        return self.__mMoverFiftyWeeksAboveFifty 

    def get_mover_fifty_weeks_above_hundred(self):
        return self.__mMoverFiftyWeeksAboveHundred 

    def get_mover_fifty_weeks_below_zero(self):
        return self.__mMoverFiftyWeeksBelowZero 

    def get_mover_fifty_weeks_below_fifty(self):
        return self.__mMoverFiftyWeeksBelowFifty 

    def get_mover_fifty_weeks_above_zero_to_ten(self):
	    return self.__mMoverFiftyWeeksAboveZeroToTen

    def get_mover_fifty_weeks_above_ten_to_twenty(self):
        return self.__mMoverFiftyWeeksAboveTenToTwenty

    def get_mover_fifty_weeks_above_twenty_to_thirty(self):
        return self.__mMoverFiftyWeeksAboveTwentyThirty

    def get_mover_fifty_weeks_above_thirty_to_fourty(self):
        return self.__mMoverFiftyWeeksAboveThirtyFourty

    def get_mover_fifty_weeks_below_zero_to_ten(self):
        return self.__mMoverFiftyWeeksBelowZeroToTen 

    def get_mover_fifty_weeks_below_ten_to_twenty(self):
        return self.__mMoverFiftyWeeksBelowTenToTwenty 

    def get_mover_fifty_weeks_below_twenty_to_thirty(self):
        return self.__mMoverFiftyWeeksBelowTwentyThirty 

    def get_mover_fifty_weeks_below_thirty_to_fourty(self):
        return self.__mMoverFiftyWeeksBelowThirtyFourty
#endregion

#region - Set Methods
    def set_max_price(self, maxPrice):
        self.__mMaxPrice = maxPrice

    def set_min_price(self, minPrice):
        self.__mMinPrice = minPrice

    def set_max_volume(self, maxVolume):
        self.__mMaxVolume = maxVolume

    def set_min_volume(self, minVolume):
        self.__mMinVolume = minVolume

    def set_max_price_mover(self, maxPriceMover):
        self.__mMaxPriceMover = maxPriceMover

    def set_min_price_mover(self, minPriceMover):
        self.__mMinPriceMover = minPriceMover

    def set_max_volume_mover(self, maxVolumeMover):
        self.__mMaxVolumeMover = maxVolumeMover

    def set_min_volume_mover(self, minVolumeMover):
        self.__mMinVolumeMover = minVolumeMover

    def set_value_max_mover(self, valueMaxMover):
	    self.__mValueMaxMover = valueMaxMover

    def set_value_min_mover(self, valueMinMover):
	    self.__mValueMinMover = valueMinMover

    def set_mover_above_zero(self, moverAboveZero):
        self.__mMoverAboveZero = moverAboveZero

    def set_mover_above_fifty(self, moverAboveFifty):
        self.__mMoverAboveFifty = moverAboveFifty

    def set_mover_above_hundred(self, moverAboveHundred):
        self.__mMoverAboveHundred = moverAboveHundred

    def set_mover_below_zero(self, moverBelowZero):
        self.__mMoverBelowZero = moverBelowZero

    def set_mover_below_fifty(self, moverBelowFifty):
        self.__mMoverBelowFifty = moverBelowFifty

    def set_mover_above_zero_to_ten(self, moverAboveZeroToTen):
        self.__mMoverAboveZeroToTen = moverAboveZeroToTen

    def set_mover_above_ten_to_twenty(self, moverAboveTenToTwenty):
        self.__mMoverAboveTenToTwenty = moverAboveTenToTwenty

    def set_mover_above_twenty_to_thirty(self, moverAboveTwentyToThirty):
        self.__mMoverAboveTwentyToThirty = moverAboveTwentyToThirty

    def set_mover_above_thirty_to_fourty(self, moverAboveThirtyToFourty):
        self.__mMoverAboveThirtyToFourty = moverAboveThirtyToFourty

    def set_mover_below_zero_to_ten(self, moverBelowZeroToTen):
        self.__mMoverBelowZeroToTen = moverBelowZeroToTen

    def set_mover_below_ten_to_twenty(self, moverBelowTenToTwenty):
        self.__mMoverBelowTenToTwenty = moverBelowTenToTwenty

    def set_mover_below_twenty_to_thirty(self, moverBelowTwentyToThirty):
        self.__mMoverBelowTwentyToThirty = moverBelowTwentyToThirty

    def set_mover_below_thirty_to_fourty(self, moverBelowThirtyToFourty):
        self.__mMoverBelowThirtyToFourty = moverBelowThirtyToFourty

    def set_fifty_value_max_mover(self, fiftyValueMaxMover):
        self.__mFiftyValueMaxMover = fiftyValueMaxMover

    def set_fifty_value_min_mover(self, fiftyValueMinMover):
        self.__mFiftyValueMinMover = fiftyValueMinMover

    def set_mover_fifty_weeks_above_zero(self, moverFiftyWeeksAboveZero):
	    self.__mMoverFiftyWeeksAboveZero  = moverFiftyWeeksAboveZero 

    def set_mover_fifty_weeks_above_fifty(self, moverFiftyWeeksAboveFifty):
        self.__mMoverFiftyWeeksAboveFifty  = moverFiftyWeeksAboveFifty 

    def set_mover_fifty_weeks_above_hundred(self, moverFiftyWeeksAboveHundred):
        self.__mMoverFiftyWeeksAboveHundred  = moverFiftyWeeksAboveHundred 

    def set_mover_fifty_weeks_below_zero(self, moverFiftyWeeksBelowZero):
        self.__mMoverFiftyWeeksBelowZero  = moverFiftyWeeksBelowZero 

    def set_mover_fifty_weeks_below_fifty(self, moverFiftyWeeksBelowFifty):
        self.__mMoverFiftyWeeksBelowFifty  = moverFiftyWeeksBelowFifty 

    def set_mover_fifty_weeks_above_zero_to_ten(self, moverFiftyWeeksAboveZeroToTen):
	    self.__mMoverFiftyWeeksAboveZeroToTen = moverFiftyWeeksAboveZeroToTen

    def set_mover_fifty_weeks_above_ten_to_twenty(self, moverFiftyWeeksAboveTenToTwenty):
        self.__mMoverFiftyWeeksAboveTenToTwenty = moverFiftyWeeksAboveTenToTwenty

    def set_mover_fifty_weeks_above_twenty_to_thirty(self, moverFiftyWeeksAboveTwentyThirty):
        self.__mMoverFiftyWeeksAboveTwentyThirty = moverFiftyWeeksAboveTwentyThirty

    def set_mover_fifty_weeks_above_thirty_to_fourty(self, moverFiftyWeeksAboveThirtyFourty):
        self.__mMoverFiftyWeeksAboveThirtyFourty = moverFiftyWeeksAboveThirtyFourty

    def set_mover_fifty_weeks_below_zero_to_ten(self, moverFiftyWeeksBelowZeroToTen):
        self.__mMoverFiftyWeeksBelowZeroToTen  = moverFiftyWeeksBelowZeroToTen 

    def set_mover_fifty_weeks_below_ten_to_twenty(self, moverFiftyWeeksBelowTenToTwenty):
        self.__mMoverFiftyWeeksBelowTenToTwenty  = moverFiftyWeeksBelowTenToTwenty 

    def set_mover_fifty_weeks_below_twenty_to_thirty(self, moverFiftyWeeksBelowTwentyThirty):
        self.__mMoverFiftyWeeksBelowTwentyThirty  = moverFiftyWeeksBelowTwentyThirty 

    def set_mover_fifty_weeks_below_thirty_to_fourty(self, moverFiftyWeeksBelowThirtyFourty):
        self.__mMoverFiftyWeeksBelowThirtyFourty  = moverFiftyWeeksBelowThirtyFourty 
#endregion

#region Public Methods
    def to_dict(self):
        return {"mMaxPrice": self.__mMaxPrice, "mMinPrice" : self.__mMinPrice, 
                "mMaxVolume": self.__mMaxVolume, "mMinVolume" : self.__mMinVolume, 

                "mMaxPriceMover" : self.__mMaxPriceMover, "mMinPriceMover" : self.__mMinPriceMover,
                "mMaxVolumeMover" : self.__mMaxVolumeMover, "mMinVolumeMover"  : self.__mMinVolumeMover,

                "mValueMaxMover": self.__mValueMaxMover, "mValueMinMover": self.__mValueMinMover,

                "mMoverAboveZero" : self.__mMoverAboveZero, "mMoverAboveFifty" : self.__mMoverAboveFifty, "mMoverAboveHundred" : self.__mMoverAboveHundred,
                "mMoverBelowZero" : self.__mMoverBelowZero, "mMoverBelowFifty" : self.__mMoverBelowFifty,

                "mMoverAboveZeroToTen": self.__mMoverAboveZeroToTen, "mMoverAboveTenToTwenty": self.__mMoverAboveTenToTwenty, 
                "mMoverAboveTwentyToThirty" : self.__mMoverAboveTwentyToThirty, "mMoverAboveThirtyToFourty": self.__mMoverAboveThirtyToFourty,  

                "mMoverBelowZeroToTen" : self.__mMoverBelowZeroToTen, "mMoverBelowTenToTwenty": self.__mMoverBelowTenToTwenty, 
                "mMoverBelowTwentyToThirty" : self.__mMoverBelowTwentyToThirty, "mMoverBelowThirtyToFourty": self.__mMoverBelowThirtyToFourty,

                "mFiftyValueMaxMover": self.__mFiftyValueMaxMover, "mFiftyValueMinMover": self.__mFiftyValueMinMover,

                "mMoverFiftyWeeksAboveZero": self.__mMoverFiftyWeeksAboveZero, "mMoverFiftyWeeksAboveFifty": self.__mMoverFiftyWeeksAboveFifty, "mMoverFiftyWeeksAboveHundred": self.__mMoverFiftyWeeksAboveHundred,
                "mMoverFiftyWeeksBelowZero": self.__mMoverFiftyWeeksBelowZero, "mMoverFiftyWeeksBelowFifty": self.__mMoverFiftyWeeksBelowFifty,

                "mMoverFiftyWeeksAboveZeroToTen": self.__mMoverFiftyWeeksAboveZeroToTen, "mMoverFiftyWeeksAboveTenToTwenty": self.__mMoverFiftyWeeksAboveTenToTwenty,
                "mMoverFiftyWeeksAboveTwentyThirty": self.__mMoverFiftyWeeksAboveTwentyThirty, "mMoverFiftyWeeksAboveThirtyFourty": self.__mMoverFiftyWeeksAboveThirtyFourty,

                "mMoverFiftyWeeksBelowZeroToTen": self.__mMoverFiftyWeeksBelowZeroToTen, "mMoverFiftyWeeksBelowTenToTwenty": self.__mMoverFiftyWeeksBelowTenToTwenty,
                "mMoverFiftyWeeksBelowTwentyThirty": self.__mMoverFiftyWeeksBelowTwentyThirty, "mMoverFiftyWeeksBelowThirtyFourty": self.__mMoverFiftyWeeksBelowThirtyFourty
        }

    def from_json(self, json):
        self.set_min_price(json["mMinPrice"])
        self.set_max_price(json["mMaxPrice"])
        self.set_min_volume(json["mMinVolume"])
        self.set_max_volume(json["mMaxVolume"])
        self.set_max_price_mover(json["mMaxPriceMover"])
        self.set_min_price_mover(json["mMinPriceMover"])
        self.set_max_volume_mover(json["mMaxVolumeMover"])
        self.set_min_volume_mover(json["mMinVolumeMover"])
        self.set_value_max_mover(json["mValueMaxMover"])
        self.set_value_min_mover(json["mValueMinMover"])
        self.set_mover_above_zero(json["mMoverAboveZero"])
        self.set_mover_above_fifty(json["mMoverAboveFifty"])
        self.set_mover_above_hundred(json["mMoverAboveHundred"])
        self.set_mover_below_zero(json["mMoverBelowZero"])
        self.set_mover_below_fifty(json["mMoverBelowFifty"])
        self.set_mover_above_zero_to_ten(json["mMoverAboveZeroToTen"])
        self.set_mover_above_ten_to_twenty(json["mMoverAboveTenToTwenty"])
        self.set_mover_above_twenty_to_thirty(json["mMoverAboveTwentyToThirty"])
        self.set_mover_above_thirty_to_fourty(json["mMoverAboveThirtyToFourty"])
        self.set_mover_below_zero_to_ten(json["mMoverBelowZeroToTen"])
        self.set_mover_below_ten_to_twenty(json["mMoverBelowTenToTwenty"])
        self.set_mover_below_twenty_to_thirty(json["mMoverBelowTwentyToThirty"])
        self.set_mover_below_thirty_to_fourty(json["mMoverBelowThirtyToFourty"])
        self.set_fifty_value_max_mover(json["mFiftyValueMaxMover"])
        self.set_fifty_value_min_mover(json["mFiftyValueMinMover"])
        self.set_mover_fifty_weeks_above_zero(json["mMoverFiftyWeeksAboveZero"])
        self.set_mover_fifty_weeks_above_fifty(json["mMoverFiftyWeeksAboveFifty"])
        self.set_mover_fifty_weeks_above_hundred(json["mMoverFiftyWeeksAboveHundred"])
        self.set_mover_fifty_weeks_below_zero(json["mMoverFiftyWeeksBelowZero"])
        self.set_mover_fifty_weeks_below_fifty(json["mMoverFiftyWeeksBelowFifty"])
        self.set_mover_fifty_weeks_above_zero_to_ten(json["mMoverFiftyWeeksAboveZeroToTen"])
        self.set_mover_fifty_weeks_above_ten_to_twenty(json["mMoverFiftyWeeksAboveTenToTwenty"])
        self.set_mover_fifty_weeks_above_twenty_to_thirty(json["mMoverFiftyWeeksAboveTwentyThirty"])
        self.set_mover_fifty_weeks_above_thirty_to_fourty(json["mMoverFiftyWeeksAboveThirtyFourty"])
        self.set_mover_fifty_weeks_below_zero_to_ten(json["mMoverFiftyWeeksBelowZeroToTen"])
        self.set_mover_fifty_weeks_below_ten_to_twenty(json["mMoverFiftyWeeksBelowTenToTwenty"])
        self.set_mover_fifty_weeks_below_twenty_to_thirty(json["mMoverFiftyWeeksBelowTwentyThirty"])
        self.set_mover_fifty_weeks_below_thirty_to_fourty(json["mMoverFiftyWeeksBelowThirtyFourty"])
#enderegion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"#- __mMaxPrice: {self.__mMaxPrice}\n"\
                f"#- __mMinPrice: {self.__mMinPrice}\n"\
                f"#- __mMaxVolume: {self.__mMaxVolume}\n"\
                f"#- __mMinVolume: {self.__mMinVolume}\n"\
                f"#- __mMaxPriceMover: {self.__mMaxPriceMover}\n"\
                f"#- __mMinPriceMover: {self.__mMinPriceMover}\n"\
                f"#- __mMaxVolumeMover: {self.__mMaxVolumeMover}\n"\
                f"#- __mMinVolumeMover: {self.__mMinVolumeMover}\n"\
                f"#- __mValueMaxMover: {self.__mValueMaxMover}\n"\
                f"#- __mValueMinMover: {self.__mValueMinMover}\n"\
                f"#- __mMoverAboveZero: {self.__mMoverAboveZero}\n"\
                f"#- __mMoverAboveFifty: {self.__mMoverAboveFifty}\n"\
                f"#- __mMoverAboveHundred: {self.__mMoverAboveHundred}\n"\
                f"#- __mMoverBelowZero: {self.__mMoverBelowZero}\n"\
                f"#- __mMoverBelowFifty: {self.__mMoverBelowFifty}\n"\
                f"#- __mMoverAboveZeroToTen: {self.__mMoverAboveZeroToTen}\n"\
                f"#- __mMoverAboveTenToTwenty: {self.__mMoverAboveTenToTwenty}\n"\
                f"#- __mMoverAboveTwentyToThirty: {self.__mMoverAboveTwentyToThirty}\n"\
                f"#- __mMoverAboveThirtyToFourty: {self.__mMoverAboveThirtyToFourty}\n"\
                f"#- __mMoverBelowZeroToTen: {self.__mMoverBelowZeroToTen}\n"\
                f"#- __mMoverBelowTenToTwenty: {self.__mMoverBelowTenToTwenty}\n"\
                f"#- __mMoverBelowTwentyToThirty: {self.__mMoverBelowTwentyToThirty}\n"\
                f"#- __mMoverBelowThirtyToFourty: {self.__mMoverBelowThirtyToFourty}\n"\
                f"#- __mFiftyValueMaxMover: {self.__mFiftyValueMaxMover}\n"\
                f"#- __mFiftyValueMinMover: {self.__mFiftyValueMinMover}\n"\
                f"#- __mMoverFiftyWeeksAboveZero: {self.__mMoverFiftyWeeksAboveZero}\n"\
                f"#- __mMoverFiftyWeeksAboveFifty: {self.__mMoverFiftyWeeksAboveFifty}\n"\
                f"#- __mMoverFiftyWeeksAboveHundred: {self.__mMoverFiftyWeeksAboveHundred}\n"\
                f"#- __mMoverFiftyWeeksBelowZero: {self.__mMoverFiftyWeeksBelowZero}\n"\
                f"#- __mMoverFiftyWeeksBelowFifty: {self.__mMoverFiftyWeeksBelowFifty}\n"\
                f"#- __mMoverFiftyWeeksAboveZeroToTen: {self.__mMoverFiftyWeeksAboveZeroToTen}\n"\
                f"#- __mMoverFiftyWeeksAboveTenToTwenty: {self.__mMoverFiftyWeeksAboveTenToTwenty}\n"\
                f"#- __mMoverFiftyWeeksAboveTwentyThirty: {self.__mMoverFiftyWeeksAboveTwentyThirty}\n"\
                f"#- __mMoverFiftyWeeksAboveThirtyFourty: {self.__mMoverFiftyWeeksAboveThirtyFourty}\n"\
                f"#- __mMoverFiftyWeeksBelowZeroToTen: {self.__mMoverFiftyWeeksBelowZeroToTen}\n"\
                f"#- __mMoverFiftyWeeksBelowTenToTwenty: {self.__mMoverFiftyWeeksBelowTenToTwenty}\n"\
                f"#- __mMoverFiftyWeeksBelowTwentyThirty: {self.__mMoverFiftyWeeksBelowTwentyThirty}\n"\
                f"#- __mMoverFiftyWeeksBelowThirtyFourty: {self.__mMoverFiftyWeeksBelowThirtyFourty}\n"\
                "####################\n"