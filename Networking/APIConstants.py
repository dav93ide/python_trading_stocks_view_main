
class APIConstants(object):

#region - Headers
    HEADERS_APP_JSON_TEXT_PLAIN_MOZILLA_UBUNTU_FIREFOX = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0"
    }

    HEADER_SET_COOKIE = "Set-Cookie"
    HEADER_COOKIE = "Cookie"
#endregion

#region - API Range Values
    VALUE_1M = "1m"
    VALUE_5M = "5m"
    VALUE_1H = "1h"
    VALUE_1D = "1d"
    VALUE_5D = "5d"
    VALUE_1MO = "1mo"
    VALUE_3MO = "3mo"
    VALUE_6MO = "6mo"
    VALUE_1Y = "1y"
    VALUE_2Y = "2y"
    VALUE_5Y = "5y"
    VALUE_10Y = "10y"
    VALUE_YTD = "ytd"
    VALUE_MAX = "max"
#endregion

#region - API Fields
#region - URL_API_STOCKANALYSIS_GET_SYMBOLS - Json Fields
    FIELD_STATUS = "status"
    FIELD_DATA = "data"
    FIELD_S = "s"
    FIELD_N = "n"
#endregion

#region - URL_API_YAHOO_FINANCE_GET_STOCKS_DATA__FROM_SYMBOLS - Json Fields
    FIELD_SPARK = "spark"
    FIELD_RESULT = "result"
    FIELD_SYMBOL = "symbol"
    FIELD_RESPONSE = "response"
    FIELD_META = "meta"
    FIELD_LONG_NAME = "longName"
    FIELD_SHORT_NAME = "shortName"
    FIELD_CURRENCY = "currency"
    FIELD_EXCHANGE_NAME = "exchangeName"
    FIELD_FULL_EXCHANGE_NAME = "fullExchangeName"
    FIELD_HAS_PRE_POST_MARKET_DATA = "hasPrePostMarketData"
    FIELD_INSTRUMENT_TYPE = "instrumentType"
    FIELD_FIRST_TRADE_DATE = "firstTradeDate"
    FIELD_REGULAR_MARKET_PRICE = "regularMarketPrice"
    FIELD_FIFTY_TWO_WEEK_HIGH = "fiftyTwoWeekHigh"
    FIELD_FIFTY_TWO_WEEK_LOW = "fiftyTwoWeekLow"
    FIELD_REGULAR_MARKET_DAY_HIGH = "regularMarketDayHigh"
    FIELD_REGULAR_MARKET_DAY_LOW = "regularMarketDayLow"
    FIELD_REGULAR_MARKET_VOLUME = "regularMarketVolume"
    FIELD_PREVIOUS_CLOSE = "previousClose"
#endregion

#region - URL_API_YAHOO_FINANCE_GET_STOCKS_DATA__FROM_SYMBOLS - Json Fields
    FIELD_TIMESERIES = "timeseries"
    FIELD_AS_OF_DATE = "asOfDate"
    FIELD_RAW = "raw"
    FIELD_FMT = "fmt"
    FIELD_REPORTED_VALUE = "reportedValue"


    FIELD_QUARTERLY_MARKET_CAP = "quarterlyMarketCap"
    FIELD_TRAILING_MARKET_CAP = "trailingMarketCap"
    FIELD_QUARTERLY_ENTERPRISE_VALUE = "quarterlyEnterpriseValue"
    FIELD_TRAILING_ENTERPRISE_VALUE = "trailingEnterpriseValue"
    FIELD_QUARTERLY_PE_RATIO = "quarterlyPeRatio"
    FIELD_TRALING_PE_RATIO = "trailingPeRatio"
    FIELD_QUARTERLY_FORWARD_PE_RATIO = "quarterlyForwardPeRatio"
    FIELD_TRALING_FORWARD_PE_RATIO = "trailingForwardPeRatio"
    FIELD_QUARTERLY_PEG_RATIO = "quarterlyPegRatio"
    FIELD_TRAILING_PEG_RATIO = "trailingPegRatio"
    FIELD_QUARTERLY_PS_RATIO = "quarterlyPsRatio"
    FIELD_TRALING_PS_RATIO = "trailingPsRatio"
    FIELD_QUARTERLY_PB_RATIO = "quarterlyPbRatio"
    FIELD_TRAILING_PB_RATIO = "trailingPbRatio"
    FIELD_QUARTERLY_ENTERPRISES_VALUE_REVENUE_RATIO = "quarterlyEnterprisesValueRevenueRatio"
    FIELD_TRAILING_ENTERPRISES_VALUE_REVENUE_RATIO = "trailingEnterprisesValueRevenueRatio"
    FIELD_QUARTERLY_ENTERPRISES_VALUE_EBITDA_RATIO = "quarterlyEnterprisesValueEBITDARatio"
    FIELD_QUARTERLY_TRAILING_ENTERPRESISES_VALUE_EBITDA_RATIO = "trailingEnterprisesValueEBITDARatio"
    FIELD_REPORTED_VALUE = "reportedValue"
#endregion

#region - URL_API_YAHOO_FINANCE_GET_FUNDAMENTALS_SERIES_STOCK - Request Fields
    FIELDS_API_GET_FUNDAMENTALS_SERIES_STOCK = [
        FIELD_QUARTERLY_MARKET_CAP,
        FIELD_TRAILING_MARKET_CAP,
        FIELD_QUARTERLY_ENTERPRISE_VALUE,
        FIELD_TRAILING_ENTERPRISE_VALUE,
        FIELD_QUARTERLY_PE_RATIO,
        FIELD_TRALING_PE_RATIO,
        FIELD_QUARTERLY_FORWARD_PE_RATIO,
        FIELD_TRALING_FORWARD_PE_RATIO,
        FIELD_QUARTERLY_PEG_RATIO,
        FIELD_TRAILING_PEG_RATIO,
        FIELD_QUARTERLY_PS_RATIO,
        FIELD_TRALING_PS_RATIO,
        FIELD_QUARTERLY_PB_RATIO,
        FIELD_TRAILING_PB_RATIO,
        FIELD_QUARTERLY_ENTERPRISES_VALUE_REVENUE_RATIO,
        FIELD_TRAILING_ENTERPRISES_VALUE_REVENUE_RATIO,
        FIELD_QUARTERLY_ENTERPRISES_VALUE_EBITDA_RATIO,
        FIELD_QUARTERLY_TRAILING_ENTERPRESISES_VALUE_EBITDA_RATIO
    ]
#endregion

#region - URL_API_YAHOO_FINANCE_GET_QUOTE_SUMMARY - Json Fields
    FIELD_QUOTE_RESPONSE = "quoteResponse"
    FIELD_ASK = "ask"
    FIELD_ASK_SIZE = "askSize"
    FIELD_BID = "bid"
    FIELD_BID_SIZE = "bidSize"
    FIELD_AVG_DAILY_VOLUME_TEN_DAYS = "averageDailyVolume10Day"
    FIELD_AVG_DAILY_VOLUME_THREE_MONTH = "averageDailyVolume3Month"
    FIELD_FIFTY_TWO_WEEK_RANGE = "fiftyTwoWeekRange"
    FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT = "fiftyTwoWeekChangePercent"
    FIELD_SHARES_OUTSTANDING = "sharesOutstanding"
    FIELD_PRICE_TO_BOOK = "priceToBook"
    FIELD_MARKET_CAP = "marketCap"
    FIELD_FORWARD_PE = "forwardPE"
    FIELD_TRAILING_PE = "trailingPE"
    FIELD_TRAILING_ANNUAL_DIVIDEND_RATE = "trailingAnnualDividendRate"
    FIELD_TRAILING_ANNUAL_DIVIDEND_YELD = "trailingAnnualDividendYield"
    FIELD_DIVIDEND_DATE = "dividendDate"
    FIELD_DIVIDEND_RATE = "dividendRate"
    FIELD_REGULAR_MARKET_PREVIOUS_CLOSE = "regularMarketPreviousClose"
    FIELD_DISPLAY_NAME = "displayName"
    FIELD_AVERAGE_ANALYST_RATING = "averageAnalystRating"
    FIELD_REGULAR_MARKET_CHANGE_PERCENT = "regularMarketChangePercent"
    FIELD_POST_MARKET_CHANGE_PERCENT = "postMarketChangePercent"
    FIELD_POST_MARKET_TIME = "postMarketTime"
    FIELD_POST_MARKET_PRICE = "postMarketPrice"
    FIELD_POST_MARKET_CHANGE = "postMarketChange"
    FIELD_EARNINGS_TIMESTAMP = "earningsTimestamp"
    FIELD_EPS_TRAILING_TWELVE_MONTHS = "epsTrailingTwelveMonths"
    FIELD_EPS_FORWARD = "epsForward"
    FIELD_EPS_CURRENT_YEAR = "epsCurrentYear"
    FIELD_PRICE_EPS_CURRENT_YEAR = "priceEpsCurrentYear"
    FIELD_BOOK_VALUE = "bookValue"
    FIELD_EXCHANGE = "exchange"
    FIELD_FIRST_TRADE_DATE_MILLISECONDS = "firstTradeDateMilliseconds"
    FIELD_FINANCIAL_CURRENCY = "financialCurrency"
    FIELD_PRE_MARKET_PRICE = "preMarketPrice"
#endregion

#region - URL_API_YAHOO_FINANCE_GET_CHART - Json Fields
    FIELD_CHART = "chart"
    FIELD_TIMESTAMP = "timestamp"
    FIELD_INDICATORS = "indicators"
    FIELD_QUOTE = "quote"
    FIELD_VOLUME = "volume"
    FIELD_CLOSE = "close"
    FIELD_OPEN = "open"
#endregion