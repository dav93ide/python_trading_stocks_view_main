from Classes.BaseClasses.BaseClass import BaseClass

class IncomeStatement(BaseClass):

    __id = None
    __mDate = None
    __mQuarter = None
    __mQuartersStatement: "IncomeStatement" = None
    __mTotalRevenue = None
    __mCreditLossesProvision = None
    __mNonInterestExpense = None
    __mSpecialIncomeCharges = None
    __mPretaxIncome = None
    __mTaxProvision = None
    __mBasicEPS = None
    __mDilutedEPS = None
    __mBasicAvgShares = None
    __mDilutedAvgShares = None
    __mNormalizedIncome = None
    __mTotalMarketInvestments = None
    __mTotalUnusualItems = None
    __mTaxRateForCalcs = None
    __mTaxEffectOfUnusualItems = None

#region - Getter Methods
    def get_id(self):
	    return self.__id

    def get_date(self):
        return self.__mDate

    def get_quarter(self):
        return self.__mQuarter

    def get_quarters_statement(self):
        return self.__mQuartersStatement

    def get_total_revenue(self):
        return self.__mTotalRevenue

    def get_credit_losses_provision(self):
        return self.__mCreditLossesProvision

    def get_non_interest_expense(self):
        return self.__mNonInterestExpense

    def get_special_income_charges(self):
        return self.__mSpecialIncomeCharges

    def get_pretax_income(self):
        return self.__mPretaxIncome

    def get_tax_provision(self):
        return self.__mTaxProvision

    def get_basic_eps(self):
        return self.__mBasicEPS

    def get_diluted_eps(self):
        return self.__mDilutedEPS

    def get_basic_avg_shares(self):
        return self.__mBasicAvgShares

    def get_diluted_avg_shares(self):
        return self.__mDilutedAvgShares

    def get_normalized_income(self):
        return self.__mNormalizedIncome

    def get_total_market_investments(self):
        return self.__mTotalMarketInvestments

    def get_total_unusual_items(self):
        return self.__mTotalUnusualItems

    def get_tax_rate_for_calcs(self):
        return self.__mTaxRateForCalcs

    def get_tax_effect_of_unusual_items(self):
        return self.__mTaxEffectOfUnusualItems
#endregion

#region - Setter Methods
    def set_id(self, id):
	    self.__id = id

    def set_date(self, date):
        self.__mDate = date

    def set_quarter(self, quarter):
        self.__mQuarter = quarter

    def set_quarters_statement(self, quartersStatement):
        self.__mQuartersStatement = quartersStatement

    def set_mTotalRevenue(self, totalRevenue):
        self.__mTotalRevenue = totalRevenue

    def set_mCreditLossesProvision(self, creditLossesProvision):
        self.__mCreditLossesProvision = creditLossesProvision

    def set_mNonInterestExpense(self, nonInterestExpense):
        self.__mNonInterestExpense = nonInterestExpense

    def set_mSpecialIncomeCharges(self, specialIncomeCharges):
        self.__mSpecialIncomeCharges = specialIncomeCharges

    def set_mPretaxIncome(self, pretaxIncome):
        self.__mPretaxIncome = pretaxIncome

    def set_mTaxProvision(self, taxProvision):
        self.__mTaxProvision = taxProvision

    def set_mBasicEPS(self, basicEPS):
        self.__mBasicEPS = basicEPS

    def set_mDilutedEPS(self, dilutedEPS):
        self.__mDilutedEPS = dilutedEPS

    def set_mBasicAvgShares(self, basicAvgShares):
        self.__mBasicAvgShares = basicAvgShares

    def set_mDilutedAvgShares(self, dilutedAvgShares):
        self.__mDilutedAvgShares = dilutedAvgShares

    def set_mNormalizedIncome(self, normalizedIncome):
        self.__mNormalizedIncome = normalizedIncome

    def set_mTotalMarketInvestments(self, totalMarketInvestments):
        self.__mTotalMarketInvestments = totalMarketInvestments

    def set_mTotalUnusualItems(self, totalUnusualItems):
        self.__mTotalUnusualItems = totalUnusualItems

    def set_mTaxRateForCalcs(self, taxRateForCalcs):
        self.__mTaxRateForCalcs = taxRateForCalcs

    def set_mTaxEffectOfUnusualItems(self, taxEffectOfUnusualItems):
        self.__mTaxEffectOfUnusualItems = taxEffectOfUnusualItems
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {IncomeStatement.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __id: {self.__id}\n"\
                f"#- __mDate: {self.__mDate}\n"\
                f"#- __mQuarter: {self.__mQuarter}\n"\
                f"#- __mQuartersStatement: {self.__mQuartersStatement}\n"\
                f"#- __mTotalRevenue: {self.__mTotalRevenue}\n"\
                f"#- __mCreditLossesProvision: {self.__mCreditLossesProvision}\n"\
                f"#- __mNonInterestExpense: {self.__mNonInterestExpense}\n"\
                f"#- __mSpecialIncomeCharges: {self.__mSpecialIncomeCharges}\n"\
                f"#- __mPretaxIncome: {self.__mPretaxIncome}\n"\
                f"#- __mTaxProvision: {self.__mTaxProvision}\n"\
                f"#- __mBasicEPS: {self.__mBasicEPS}\n"\
                f"#- __mDilutedEPS: {self.__mDilutedEPS}\n"\
                f"#- __mBasicAvgShares: {self.__mBasicAvgShares}\n"\
                f"#- __mDilutedAvgShares: {self.__mDilutedAvgShares}\n"\
                f"#- __mNormalizedIncome: {self.__mNormalizedIncome}\n"\
                f"#- __mTotalMarketInvestments: {self.__mTotalMarketInvestments}\n"\
                f"#- __mTotalUnusualItems: {self.__mTotalUnusualItems}\n"\
                f"#- __mTaxRateForCalcs: {self.__mTaxRateForCalcs}\n"\
                f"#- __mTaxEffectOfUnusualItems: {self.__mTaxEffectOfUnusualItems}\n"\
                "####################"