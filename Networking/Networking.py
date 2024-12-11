from Networking.API import API
from Networking import APIConstants
import requests

class Networking(object):

#region - Download Methods
    def download_request_yahoo_finance_get_cookie(headers):
        return requests.get(API.URL_API_YAHOO_FINANCE_QUERY2, headers = headers)

    def download_get_crumb_yahoo_finance(headers):
        return requests.get(API.URL_API_YAHOO_FINANCE_GET_CRUMB, headers = headers).text

    def download_all_stock_symbols(headers):
        return requests.get(API.URL_API_STOCKANALYSIS_GET_SYMBOLS, headers = headers).text

    def download_stocks_data_from_symbols(symbols, headers):
        return requests.get(API.URL_API_YAHOO_FINANCE_GET_STOCKS_DATA_FROM_SYMBOLS.format(symbols = symbols), headers = headers).text

    def download_fundamentals_timeseries_stock_data(symbol, startTime, endTime, fields, headers):
        return requests.get(API.URL_API_YAHOO_FINANCE_GET_FUNDAMENTALS_SERIES_STOCK_DATA.format(symbol = symbol, periodStart = startTime, periodEnd = endTime, type = fields), headers = headers).text

    def download_quote_of_stock(symbols, crumb, headers):
        try:
            return requests.get(API.URL_API_YAHOO_FINANCE_QUOTE.format(symbols = symbols, crumb = crumb), headers = headers).text
        except:
            return None

    def download_chart(symbol, rangee, interval, headers):
        return requests.get(API.URL_API_YAHOO_FINANCE_GET_CHART.format(symbol = symbol, range = rangee, interval = interval), headers = headers).text
#endregion