from Networking.API import API
from Networking import APIConstants
import requests
from requests_html import HTMLSession

class Networking(object):

#region - Download Methods
    def download_request_yahoo_finance_get_cookie(headers):
        return requests.get(API.URL_API_YAHOO_FINANCE_QUERY2, headers = headers)

    def download_get_crumb_yahoo_finance(headers):
        hdrs = headers
        if "User-Agent" in hdrs:
            del hdrs["User-Agent"]
        session = HTMLSession()
        r = session.get(API.URL_API_YAHOO_FINANCE_GET_CRUMB, headers = hdrs)
        return r.content.decode("utf-8")

    def download_gov_all_stock_symbols(headers):
        session = HTMLSession()
        r = session.get(API.URL_API_GOV_GET_SYMBOLS, headers = headers)
        return r.content.decode("utf-8")

    def download_all_stock_analysis_symbols(headers):
        session = HTMLSession()
        r = session.get(API.URL_API_STOCKANALYSIS_GET_SYMBOLS, headers = headers)
        return r.content.decode("utf-8")

    def download_stocks_data_from_symbols(symbols, headers):
        session = HTMLSession()
        r = session.get(API.URL_API_YAHOO_FINANCE_GET_STOCKS_DATA_FROM_SYMBOLS.format(symbols = symbols), headers = headers)
        return r.content.decode("utf-8")

    def download_fundamentals_timeseries_stock_data(symbol, startTime, endTime, fields, headers):
        session = HTMLSession()
        r = session.get(API.URL_API_YAHOO_FINANCE_GET_FUNDAMENTALS_SERIES_STOCK_DATA.format(symbol = symbol, periodStart = startTime, periodEnd = endTime, type = fields), headers = headers)
        return r.content.decode("utf-8")

    def download_quote_of_stock(symbols, crumb, headers):
        try:
            session = HTMLSession()
            r = session.get(API.URL_API_YAHOO_FINANCE_QUOTE.format(symbols = symbols, crumb = crumb), headers = headers)
            return r.content.decode("utf-8")
        except:
            return None

    def download_chart(symbol, rangee, interval, headers):
        session = HTMLSession()
        r = session.get(API.URL_API_YAHOO_FINANCE_GET_CHART.format(symbol = symbol, range = rangee, interval = interval), headers = headers)
        return r.content.decode("utf-8")

    def download_cryptocurrencies(start, headers):
        session = HTMLSession()
        r = session.get(API.URL_API_YAHOO_FINANCE_SCREENER_CRYPTOCURRENCIES.format(start = str(start)), headers = headers)
        return r.content.decode("utf-8")
#endregion