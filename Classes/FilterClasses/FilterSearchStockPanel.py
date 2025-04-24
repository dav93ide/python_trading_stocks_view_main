
class FilterSearchStockPanel(object):

    __mMinPrice = None
    __mMaxPrice = None
    __mMinVolume = None
    __mMaxVolume = None

    __mMaxPriceMover = None
    __mMinPriceMover = None
    __mMaxVolumeMover = None
    __mMinVolumeMover = None

    __mMoverAboveZero = None
    __mMoverAboveFifty = None
    __mMoverAboveHundred = None
    __mMoverBelowZero = None
    __mMoverBelowFifty = None
    __mMoverBelowHundred = None

    __mMoverAboveZeroToTen = None
    __mMoverAboveTenToTwenty = None
    __mMoverAboveTwentyToThirty = None
    __mMoverAboveThirtyToFourty = None

    __mMoverBelowZeroToTen = None
    __mMoverBelowTenToTwenty = None
    __mMoverBelowTwentyToThirty = None
    __mMoverBelowThirtyToFourty = None

    #region - Get Methods
    def get_min_price(self):
        return self.__mMinPrice

    def get_max_price(self):
        return self.__mMaxPrice

    def get_min_volume(self):
        return self.__mMinVolume

    def get_max_volume(self):
        return self.__mMaxVolume

    def get_max_price_mover(self):
        return self.__mMaxPriceMover

    def get_min_price_mover(self):
        return self.__mMinPriceMover

    def get_max_volume_mover(self):
        return self.__mMaxVolumeMover

    def get_min_volume_mover(self):
        return self.__mMinVolumeMover

    def get_mover_above_zero(self):
        return self.__mMoverAboveZero

    def get_mover_above_fifty_mover_above_hundred(self):
        return self.__mMoverAboveFifty__mMoverAboveHundred

    def get_mover_below_zero(self):
        return self.__mMoverBelowZero

    def get_mover_below_fifty(self):
        return self.__mMoverBelowFifty

    def get_mover_below_hundred(self):
        return self.__mMoverBelowHundred

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
    #endregion

    #region - Set Methods
    def set_min_price(self, minPrice):
        self.__mMinPrice = minPrice

    def set_max_price(self, maxPrice):
        self.__mMaxPrice = maxPrice

    def set_min_volume(self, minVolume):
        self.__mMinVolume = minVolume

    def set_max_volume(self, maxVolume):
        self.__mMaxVolume = maxVolume

    def set_max_price_mover(self, maxPriceMover):
        self.__mMaxPriceMover = maxPriceMover

    def set_min_price_mover(self, minPriceMover):
        self.__mMinPriceMover = minPriceMover

    def set_max_volume_mover(self, maxVolumeMover):
        self.__mMaxVolumeMover = maxVolumeMover

    def set_min_volume_mover(self, minVolumeMover):
        self.__mMinVolumeMover = minVolumeMover

    def set_mover_above_zero(self, moverAboveZero):
        self.__mMoverAboveZero = moverAboveZero

    def set_mover_above_fifty(self, moverAboveFifty):
        self.__mMoverAboveFifty__mMoverAboveHundred = moverAboveFiftyMoverAboveHundred

    def set_mover_above_hundred(self, moverAboveHundred):
        self.__mMoverAboveFifty__mMoverAboveHundred = moverAboveFiftyMoverAboveHundred

    def set_mover_below_zero(self, moverBelowZero):
        self.__mMoverBelowZero = moverBelowZero

    def set_mover_below_fifty(self, moverBelowFifty):
        self.__mMoverBelowFifty = moverBelowFifty

    def set_mover_below_hundred(self, moverBelowHundred):
        self.__mMoverBelowHundred = moverBelowHundred

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
    #endregion
