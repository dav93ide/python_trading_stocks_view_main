import json, yaml
from Classes.Stock import Stock
from Classes.Cryptocurrency import Cryptocurrency

class StockView(object):
    
    __mStock : Stock = None
    __mCrypto : Cryptocurrency = None
    __mQuarterlyMarketCap = None
    __mTrailingMarketCap = None
    __mQuarterlyEnterpriseValue = None
    __mTrailingEnterpriseValue = None
    __mQuarterlyPeRatio = None
    __mTrailingPeRatio = None
    __mQuarterlyForwardPeRatio = None
    __mTrailingForwardPeRatio = None
    __mQuarterlyPegRatio = None
    __mTrailingPegRatio = None
    __mQuarterlyPsRatio = None
    __mTrailingPsRatio = None
    __mQuarterlyPbRatio = None
    __mTrailingPbRatio = None
    __mQuarterlyEnterprisesValueRevenueRatio = None
    __mTrailingEnterprisesValueRevenueRatio = None
    __mQuarterlyEnterprisesValueEBITDARatio = None
    __mTrailingEnterprisesValueEBITDARatio = None

    __mTimestamps = None
    __mVolumes = None
    __mOpens = None
    __mCloses = None

#region - Get Methods
    def get_stock(self):
        return self.__mStock

    def get_crypto(self):
        return self.__mCrypto

    def get_quarterly_market_cap(self):
        return self.__mQuarterlyMarketCap

    def get_trailing_market_cap(self):
        return self.__mTrailingMarketCap

    def get_quarterly_enterprise_value(self):
        return self.__mQuarterlyEnterpriseValue

    def get_trailing_enterprise_value(self):
        return self.__mTrailingEnterpriseValue

    def get_quarterly_forward_pe_ratio(self):
        return self.__mQuarterlyForwardPeRatio

    def get_trailing_forward_pe_ratio(self):
        return self.__mTrailingForwardPeRatio

    def get_quarterly_pe_ratio(self):
        return self.__mQuarterlyPeRatio

    def get_trailing_pe_ratio(self):
        return self.__mTrailingPeRatio

    def get_quarterly_ps_ratio(self):
        return self.__mQuarterlyPsRatio

    def get_quarterly_forward_pe_ratio(self):
        return self.__mQuarterlyForwardPeRatio

    def get_trailing_forward_pe_ratio(self):
        return self.__mTrailingForwardPeRatio

    def get_quarterly_peg_ratio(self):
        return self.__mQuarterlyPegRatio

    def get_trailing_peg_ratio(self):
        return self.__mTrailingPegRatio

    def get_quarterly_ps_ratio(self):
        return self.__mQuarterlyPsRatio

    def get_trailing_ps_ratio(self):
        return self.__mTrailingPsRatio

    def get_quarterly_pb_ratio(self):
        return self.__mQuarterlyPbRatio

    def get_trailing_pb_ratio(self):
        return self.__mTrailingPbRatio

    def get_quarterly_enterprises_value_revenue_ratio(self):
        return self.__mQuarterlyEnterprisesValueRevenueRatio

    def get_trailing_enterprises_value_revenue_ratio(self):
        return self.__mTrailingEnterprisesValueRevenueRatio

    def get_quarterly_enterprises_value_ebitda_ratio(self):
        return self.__mQuarterlyEnterprisesValueEBITDARatio

    def get_trailing_enterprises_value_ebitda_ratio(self):
        return self.__mTrailingEnterprisesValueEBITDARatio

    def get_timestamps(self):
    	return self.__mTimestamps

    def get_volumes(self):
        return self.__mVolumes

    def get_opens(self):
        return self.__mOpens

    def get_closes(self):
        return self.__mCloses
#endregion

#region - Set Methods
    def set_stock(self, stock):
        self.__mStock = stock

    def set_crypto(self, crypto):
        self.__mCrypto = crypto

    def set_quarterly_market_cap(self, stockQuarterlyMarketCap):
        self.__mStock__mQuarterlyMarketCap = stockQuarterlyMarketCap

    def set_trailing_market_cap(self, trailingMarketCap):
        self.__mTrailingMarketCap = trailingMarketCap

    def set_quarterly_enterprise_value(self, quarterlyEnterpriseValue):
        self.__mQuarterlyEnterpriseValue = quarterlyEnterpriseValue

    def set_trailing_enterprise_value(self, trailingEnterpriseValue):
        self.__mTrailingEnterpriseValue = trailingEnterpriseValue

    def set_quarterly_forward_pe_ratio(self, quarterlyForwardPeRatio):
        self.__mQuarterlyForwardPeRatio = quarterlyForwardPeRatio

    def set_trailing_forward_pe_ratio(self, trailingForwardPeRatio):
        self.__mTrailingForwardPeRatio = trailingForwardPeRatio

    def set_quarterly_pe_ratio(self, quarterlyPeRatio):
        self.__mQuarterlyPeRatio = quarterlyPeRatio

    def set_trailing_pe_ratio(self, trailingPeRatio):
        self.__mTrailingPeRatio = trailingPeRatio

    def set_quarterly_ps_ratio(self, quarterlyPsRatio):
        self.__mQuarterlyPsRatio = quarterlyPsRatio

    def set_quarterly_forward_pe_ratio(self, quarterlyForwardPeRatio):
        self.__mQuarterlyForwardPeRatio = quarterlyForwardPeRatio

    def set_trailing_forward_pe_ratio(self, trailingForwardPeRatio):
        self.__mTrailingForwardPeRatio = trailingForwardPeRatio

    def set_quarterly_peg_ratio(self, quarterlyPegRatio):
        self.__mQuarterlyPegRatio = quarterlyPegRatio

    def set_trailing_peg_ratio(self, trailingPegRatio):
        self.__mTrailingPegRatio = trailingPegRatio

    def set_quarterly_ps_ratio(self, quarterlyPsRatio):
        self.__mQuarterlyPsRatio = quarterlyPsRatio

    def set_trailing_ps_ratio(self, ratio):
        self.__mTrailingPsRatio = ratio

    def set_quarterly_pb_ratio(self, ratio):
        self.__mQuarterlyPbRatio = ratio

    def set_trailing_pb_ratio(self, trailingPbRatio):
        self.__mTrailingPbRatio = trailingPbRatio

    def set_quarterly_enterprises_value_revenue_ratio(self, quarterlyEnterprisesValueRevenueRatio):
        self.__mQuarterlyEnterprisesValueRevenueRatio = quarterlyEnterprisesValueRevenueRatio

    def set_trailing_enterprises_value_revenue_ratio(self, trailingEnterprisesValueRevenueRatio):
        self.__mTrailingEnterprisesValueRevenueRatio = trailingEnterprisesValueRevenueRatio

    def set_quarterly_enterprises_value_ebitda_ratio(self, quarterlyEnterprisesValueEBITDARatio):
        self.__mQuarterlyEnterprisesValueEBITDARatio = quarterlyEnterprisesValueEBITDARatio

    def set_trailing_enterprises_value_ebitda_ratio(self, trailingEnterprisesValueEBITDARatio):
        self.__mTrailingEnterprisesValueEBITDARatio = trailingEnterprisesValueEBITDARatio

    def set_timestamps(self, timestamps):
	    self.__mTimestamps = timestamps

    def set_volumes(self, volume):
        self.__mVolumes = volume

    def set_opens(self, opens):
        self.__mOpens = opens

    def set_closes(self, closes):
        self.__mCloses = closes
#endregion


    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {StockView.__name__}\n"\
                f"#- __mStock: {str(self.__mStock)}\n"\
                f"#- __mCrypto: {str(self.__mCrypto)}\n"\
                f"#- __mQuarterlyMarketCap:\t\t\t\t\t\t{yaml.dump(self.get_quarterly_market_cap())}\n"\
                f"#- __mTrailingMarketCap:\t\t{yaml.dump(self.get_trailing_market_cap())}\n"\
                f"#- __mQuarterlyEnterpriseValue:\t\t{yaml.dump(self.get_quarterly_enterprise_value())}\n"\
                f"#- __mTrailingEnterpriseValue:\t\t{yaml.dump(self.get_trailing_enterprise_value())}\n"\
                f"#- __mQuarterlyPeRatio:\t\t{yaml.dump(self.get_quarterly_pe_ratio())}\n"\
                f"#- __mTrailingPeRatio:\t\t{yaml.dump(self.get_trailing_pe_ratio())}\n"\
                f"#- __mQuarterlyForwardPeRatio:\t\t{yaml.dump(self.get_quarterly_forward_pe_ratio())}\n"\
                f"#- __mTrailingForwardPeRatio:\t\t{yaml.dump(self.get_quarterly_forward_pe_ratio())}\n"\
                f"#- __mQuarterlyPegRatio:\t\t{yaml.dump(self.get_quarterly_peg_ratio())}\n"\
                f"#- __mTrailingPegRatio:\t\t{yaml.dump(self.get_trailing_peg_ratio())}\n"\
                f"#- __mQuarterlyPsRatio:\t\t{yaml.dump(self.get_quarterly_ps_ratio())}\n"\
                f"#- __mTrailingPsRatio:\t\t{yaml.dump(self.get_trailing_ps_ratio())}\n"\
                f"#- __mQuarterlyPbRatio:\t\t{yaml.dump(self.get_quarterly_pb_ratio())}\n"\
                f"#- __mTrailingPbRatio:\t\t{yaml.dump(self.get_trailing_pb_ratio())}\n"\
                f"#- __mQuarterlyEnterprisesValueRevenueRatio:\t\t{yaml.dump(self.get_quarterly_enterprises_value_revenue_ratio())}\n"\
                f"#- __mTrailingEnterprisesValueRevenueRatio:\t\t{yaml.dump(self.get_trailing_enterprises_value_revenue_ratio())}\n"\
                f"#- __mQuarterlyEnterprisesValueEBITDARatio:\t\t{yaml.dump(self.get_quarterly_enterprises_value_ebitda_ratio())}\n"\
                f"#- __mTrailingEnterprisesValueEBITDARatio:\t\t{yaml.dump(self.get_trailing_enterprises_value_ebitda_ratio())}\n"\
                f"#- __mTimestamps: {self.__mTimestamps}\n"\
                f"#- __mVolumes: {self.__mVolumes}\n"\
                f"#- __mOpens: {self.__mOpens}\n"\
                f"#- __mCloses: {self.__mCloses}\n"\
                "####################"