from Classes import City, IncomeStatement, BalanceSheet, CashFlow
from Resources.Constants import Constants, Sector
from Classes.BaseClasses.BaseClass import BaseClass

class Company(BaseClass):

    __mName = None
    __mShortName = None
    __mSectors: Sector = None
    __mYearBorn = None
    __mCity: City = None
    __mAddress = None
    __mWebsiteUrl = None
    __mNumEmployees = None
    __mEnterpriseValue = None
    __mRevenue = None
    __mQuarterlyRevenueGrowth = None
    __mGrossProfit = None
    __mEBITDA = None
    __mNetIncome = None
    __mQuarterlyEarningsGrowth = None
    __mIncomeStatements: IncomeStatement = None
    __mBalanceSheets: BalanceSheet = None
    __mCashFlows: CashFlow = None

    def __init__(self, id):
        super().__init__(id)

#region - Getter Methods
    def get_name(self):
        return self.__mName

    def get_short_name(self):
        return self.__mShortName

    def get_sectors(self):
        return self.__mSectors

    def get_year_born(self):
        return self.__mYearBorn

    def get_city(self):
        return self.__mCity

    def get_address(self):
        return self.__mAddress

    def get_website_url(self):
        return self.__mWebsiteUrl

    def get_num_employees(self):
        return self.__mNumEmployees

    def get_enterprise_value(self):
        return self.__mEnterpriseValue

    def get_revenue(self):
        return self.__mRevenue

    def get_quarterly_revenue_growth(self):
        return self.__mQuarterlyRevenueGrowth

    def get_gross_profit(self):
        return self.__mGrossProfit

    def get_ebitda(self):
        return self.__mEBITDA

    def get_net_income(self):
        return self.__mNetIncome

    def get_quarterly_earnings_growth(self):
        return self.__mQuarterlyEarningsGrowth

    def get_income_statements(self):
        return self.__mIncomeStatements

    def get_balance_sheets(self):
        return self.__mBalanceSheets

    def get_cash_flows(self):
        return self.__mCashFlows
#endregion

#region - Setter Methods
    def set_name(self, name):
        self.__mName = name

    def set_short_name(self, name):
        self.__mShortName = name

    def set_sectors(self, sectors):
        self.__mSectors = sectors

    def set_year_born(self, yearBorn):
        self.__mYearBorn = yearBorn

    def set_city(self, city):
        self.__mCity = city

    def set_address(self, address):
        self.__mAddress = address

    def set_website_url(self, websiteUrl):
        self.__mWebsiteUrl = websiteUrl

    def set_num_employees(self, numEmployees):
        self.__mNumEmployees = numEmployees

    def set_enterprise_value(self, enterpriseValue):
        self.__mEnterpriseValue = enterpriseValue

    def set_revenue(self, revenue):
        self.__mRevenue = revenue

    def set_quarterly_revenue_growth(self, quarterlyRevenueGrowth):
        self.__mQuarterlyRevenueGrowth = quarterlyRevenueGrowth

    def set_gross_profit(self, grossProfit):
        self.__mGrossProfit = grossProfit

    def set_ebitda(self, ebitda):
        self.__mEBITDA = ebitda

    def set_net_income(self, netIncome):
        self.__mNetIncome = netIncome

    def set_quarterly_earnings_growth(self, quarterlyEarningsGrowth):
        self.__mQuarterlyEarningsGrowth = quarterlyEarningsGrowth

    def set_income_statements(self, incomeStatemtents):
        self.__mIncomeStatements = incomeStatemtents

    def set_balance_sheets(self, balanceSheets):
        self.__mBalanceSheets = balanceSheets

    def set_cash_flows(self, cashFlows):
        self.__mCashFlows = cashFlows
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Company.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mName: {self.__mName}\n"\
                f"#- __mShortName: {self.__mShortName}\n"\
                f"#- __mSectors: {self.__mSectors}\n"\
                f"#- __mYearBorn: {self.__mYearBorn}\n"\
                f"#- __mCity: {self.__mCity}\n"\
                f"#- __mAddress: {self.__mAddress}\n"\
                f"#- __mWebsiteUrl: {self.__mWebsiteUrl}\n"\
                f"#- __mEnterpriseValue: {self.__mEnterpriseValue}\n"\
                f"#- __mRevenue: {self.__mRevenue}\n"\
                f"#- __mQuarterlyRevenueGrowth: {self.__mQuarterlyRevenueGrowth}\n"\
                f"#- __mGrossProfit: {self.__mGrossProfit}\n"\
                f"#- __mEBITDA: {self.__mEBITDA}\n"\
                f"#- __mNetIncome: {self.__mNetIncome}\n"\
                f"#- __mQuarterlyEarningsGrowth: {self.__mQuarterlyEarningsGrowth}\n"\
                f"#- __mIncomeStatements: {self.__mIncomeStatements}\n"\
                f"#- __mBalanceSheets: {self.__mBalanceSheets}\n"\
                f"#- __mCashFlows: {self.__mCashFlows}\n"\
                "####################"
