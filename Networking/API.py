class API(object):
    
#region - API
    URL_API_GOV_GET_SYMBOLS = "https://www.sec.gov/files/company_tickers.json"
    URL_API_STOCKANALYSIS_GET_SYMBOLS = "https://api.stockanalysis.com/api/screener/s/f?m=s&s=asc&c=s,n&i=stocks"
    URL_API_STOCKANALYSIS_GET_SYMBOLS_AND_STOCKS_INFO = "https://api.stockanalysis.com/api/screener/s/f?m=s&s=asc&c=s,n,industry,exchange,marketCap,price,volume&i=stocks"

    URL_API_YAHOO_FINANCE_QUERY2 = "https://query2.finance.yahoo.com/"
    URL_API_YAHOO_FINANCE_GET_CRUMB = "https://query2.finance.yahoo.com/v1/test/getcrumb"
    URL_API_YAHOO_FINANCE_GET_STOCKS_DATA_FROM_SYMBOLS = "https://query1.finance.yahoo.com/v7/finance/spark?symbols={symbols}&range=1d&interval=1d"     # Max 20 Symbols
    URL_API_YAHOO_FINANCE_GET_FUNDAMENTALS_SERIES_STOCK_DATA = "https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{symbol}?merge=false&padTimeSeries=true&period1={periodStart}&period2={periodEnd}&type={type}&lang=en-US&region=US"
    URL_API_YAHOO_FINANCE_SEARCH = "https://query2.finance.yahoo.com/v1/finance/search?q={symbol}"
    URL_API_YAHOO_FINANCE_LIST_OF_CURRENCIES = "https://query2.finance.yahoo.com/v1/finance/currencies"
    URL_API_YAHOO_FINANCE_GET_CHART = "https://query2.finance.yahoo.com/v8/finance/chart/{symbol}?range={range}&interval={interval}"
    URL_API_YAHOO_FINANCE_QUOTE = "https://query2.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols={symbols}&crumb={crumb}"
    URL_API_YAHOO_FINANCE_GET_QUOTE_SUMMARY = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?crumb={crumb}&modules={modules}"
    URL_API_YAHOO_OPTIONS = "https://query2.finance.yahoo.com/v7/finance/options/{symbol}?crumb={crumb}"
#endregion



# MODULES QUOTE SUMMARY
#
# assetProfile,incomeStatementHistory,incomeStatementHistoryQuarterly,balanceSheetHistory,balanceSheetHistoryQuarterly,cashFlowStatementHistory,cashFlowStatementHistoryQuarterly,defaultKeyStatistics,financialData,calendarEvents,secFilings,recommendationTrend,upgradeDowngradeHistory,institutionOwnership,fundOwnership,majorDirectHolders,majorHoldersBreakdown,insiderTransactions,insiderHolders,netSharePurchaseActivity,earnings,earningsHistory,earningsTrend,industryTrend,indexTrend,sectorTrend
#
#