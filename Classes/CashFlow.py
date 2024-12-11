from Classes.BaseClasses.BaseClass import BaseClass

class CashFlow(BaseClass):

    __mDate = None
    __mQuarter = None   
    __mQuartersCashFlow: "CashFlow" = None
    __mOperatingCashFlow = None
    __mInvestingCashFlow = None
    __mFinancingCashFlow = None
    __mEndCashPosition = None
    __mIncomeTaxPaidSuppData = None
    __mInterestPaidSuppData = None
    __mCapitalExpenditure = None
    __mIssuanceOfDebt = None
    __mRepaymentOfDebt = None
    __mRepurchaseOfCapitalStock = None
    __mFreeCashFlow = None

    def __init__(self, id):
        super().__init__(id)

#region - Getter Methods
    def get_date(self):
        return self.__mDate

    def get_quarter(self):
        return self.__mQuarter

    def get_quarters_cash_flow(self):
        return self.__mQuartersCashFlow

    def get_operating_cash_flow(self):
        return self.__mOperatingCashFlow

    def get_investing_cash_flow(self):
        return self.__mInvestingCashFlow

    def get_financing_cash_flow(self):
        return self.__mFinancingCashFlow

    def get_end_cash_position(self):
        return self.__mEndCashPosition

    def get_mIncomeTaxPaidSuppData(self):
	    return self.__mIncomeTaxPaidSuppData

    def get_mInterestPaidSuppData(self):
        return self.__mInterestPaidSuppData

    def get_capital_expenditure(self):
        return self.__mCapitalExpenditure

    def get_issuance_of_debt(self):
        return self.__mIssuanceOfDebt

    def get_repayment_of_debt(self):
        return self.__mRepaymentOfDebt

    def get_repurchase_of_capital_stock(self):
        return self.__mRepurchaseOfCapitalStock

    def get_free_cash_flow(self):
        return self.__mFreeCashFlow
#endregion

#region - Setter Methods
    def set_date(self, date):
        self.__mDate = date

    def set_quarter(self, quarter):
        self.__mQuarter = quarter

    def set_quarters_cash_flow(self, quarter):
        self.__mQuartersCashFlow = quarter

    def set_operating_cash_flow(self, cashFlow):
        self.__mOperatingCashFlow = cashFlow

    def set_investing_cash_flow(self, cashFlow):
        self.__mInvestingCashFlow = cashFlow

    def set_financing_cash_flow(self, cashFlow):
        self.__mFinancingCashFlow = cashFlow

    def set_end_cash_position(self, cashFlow):
        self.__mEndCashPosition = cashFlow

    def set_mIncomeTaxPaidSuppData(self, incomeTaxPaidSuppData):
	    self.__mIncomeTaxPaidSuppData = incomeTaxPaidSuppData

    def set_mInterestPaidSuppData(self, interestPaidSuppData):
        self.__mInterestPaidSuppData = interestPaidSuppData

    def set_mCapitalExpenditure(self, capitalExpenditure):
        self.__mCapitalExpenditure = capitalExpenditure

    def set_mIssuanceOfDebt(self, issuanceOfDebt):
        self.__mIssuanceOfDebt = issuanceOfDebt

    def set_mRepaymentOfDebt(self, repaymentOfDebt):
        self.__mRepaymentOfDebt = repaymentOfDebt

    def set_mRepurchaseOfCapitalStock(self, repurchaseOfCapitalStock):
        self.__mRepurchaseOfCapitalStock = repurchaseOfCapitalStock

    def set_mFreeCashFlow(self, freeCashFlow):
        self.__mFreeCashFlow = freeCashFlow
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {ClashFlow.__name__}\n"\
                f"{super().__str__()} \n"\
                f"#- __id: {self.__id}\n"\
                f"#- __mDate: {self.__mDate}\n"\
                f"#- __mQuarter: {self.__mQuarter}\n"\
                f"#- __mQuartersCashFlow: {self.__mQuartersCashFlow}\n"\
                f"#- __mOperatingCashFlow: {self.__mOperatingCashFlow}\n"\
                f"#- __mInvestingCashFlow: {self.__mInvestingCashFlow}\n"\
                f"#- __mFinancingCashFlow: {self.__mFinancingCashFlow}\n"\
                f"#- __mEndCashPosition: {self.__mEndCashPosition}\n"\
                "####################"