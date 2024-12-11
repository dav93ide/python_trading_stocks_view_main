from Classes.BaseClasses.BaseClass import BaseClass

class BalanceSheet(BaseClass):

    __mDate = None
    __mQuarter = None
    __mQuartersBalanceSheet: "BalanceSheet" = None
    __mTotalAssets = None
    __mTotalLiabilitiesMI = None
    __mTotalEquityGrossMI = None
    __mTotalCapitalization = None
    __mPreferredStockEquity = None
    __mCommonStockEquity = None
    __mCapitalLeaseObligations = None
    __mNetTangibleAssets = None
    __mTotalDebt = None
    __mSharesIssued = None
    __mOrdinarySharesNumber = None
    __mPreferredSharesNumber = None
    __mTreasurySharesNumber = None

    def __init__(self, id):
        super().__init__(id)

#region - Getter Methods
    def get_date(self):
        return self.__mDate

    def get_quarter(self):
        return self.__mQuarter

    def get_quarters_balance_sheet(self):
        return self.__mQuartersBalanceSheet

    def get_total_assets(self):
        return self.__mTotalAssets

    def get_total_liabilities_mi(self):
        return self.__mTotalLiabilitiesMI

    def get_total_equity_gross_mi(self):
        return self.__mTotalEquityGrossMI

    def get_total_capitalization(self):
        return self.__mTotalCapitalization

    def get_preferred_stock_equity(self):
        return self.__mPreferredStockEquity

    def get_common_stock_equity(self):
        return self.__mCommonStockEquity

    def get_capital_lease_obligations(self):
        return self.__mCapitalLeaseObligations

    def get_net_tangible_assets(self):
        return self.__mNetTangibleAssets

    def get_total_debt(self):
        return self.__mTotalDebt

    def get_shares_issued(self):
        return self.__mSharesIssued

    def get_ordinary_shares_number(self):
        return self.__mOrdinarySharesNumber

    def get_preferred_shares_number(self):
        return self.__mPreferredSharesNumber

    def get_treasury_shares_number(self):
        return self.__mTreasurySharesNumber
#endregion

#region - Setter Methods
    def set_date(self, date):
        self.__mDate = date

    def set_quarter(self, quarter):
        self.__mQuarter = quarter

    def set_quarters_balance_sheet(self, quarter):
        self.__mQuartersBalanceSheet = quarter

    def set_total_assets(self, assets):
        self.__mTotalAssets = assets

    def set_total_liabilities_mi(self, total):
        self.__mTotalLiabilitiesMI = total

    def set_total_equity_gross_mi(self, total):
        self.__mTotalEquityGrossMI = total

    def set_total_capitalization(self, total):
        self.__mTotalCapitalization = total

    def set_preferred_stock_equity(self, stock):
        self.__mPreferredStockEquity = stock

    def set_common_stock_equity(self, stock):
        self.__mCommonStockEquity = stock

    def set_capital_lease_obligations(self, capital):
        self.__mCapitalLeaseObligations = capital

    def set_net_tangible_assets(self, assets):
        self.__mNetTangibleAssets = assets

    def set_total_debt(self, debt):
        self.__mTotalDebt = debt

    def set_shares_issued(self, shares):
        self.__mSharesIssued = shares

    def set_ordinary_shares_number(self, shares):
        self.__mOrdinarySharesNumber = shares

    def set_preferred_shares_number(self, shares):
        self.__mPreferredSharesNumber = shares

    def set_treasury_shares_number(self, shares):
        self.__mTreasurySharesNumber = shares
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {BalanceSheet.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mDate: {self.__mDate}\n"\
                f"#- __mQuarter: {self.__mQuarter}\n"\
                f"#- __mQuartersBalanceSheet: {self.__mQuartersBalanceSheet}\n"\
                f"#- __mTotalAssets: {self.__mTotalAssets}\n"\
                f"#- __mTotalLiabilitiesMI: {self.__mTotalLiabilitiesMI}\n"\
                f"#- __mTotalEquityGrossMI: {self.__mTotalEquityGrossMI}\n"\
                f"#- __mTotalCapitalization: {self.__mTotalCapitalization}\n"\
                f"#- __mPreferredStockEquity: {self.__mPreferredStockEquity}\n"\
                f"#- __mCapitalLeaseObligations: {self.__mCapitalLeaseObligations}\n"\
                f"#- __mNetTangibleAssets: {self.__mNetTangibleAssets}\n"\
                f"#- __mTotalDebt: {self.__mTotalDebt}\n"\
                f"#- __mSharesIssued: {self.__mSharesIssued}\n"\
                f"#- __mOrdinarySharesNumber: {self.__mOrdinarySharesNumber}\n"\
                f"#- __mPreferredSharesNumber: {self.__mPreferredSharesNumber}\n"\
                f"#- __mTreasurySharesNumber: {self.__mTreasurySharesNumber}\n"\
                "####################"
