import json
import uuid
import time
from Resources.Constants import DataFilenames
from Networking.Networking import Networking
from Networking.API import API
from Networking.APIConstants import APIConstants
from Classes.Stock import Stock
from Classes.Cryptocurrency import Cryptocurrency
from Classes.Company import Company
from Classes.Exchange import Exchange
from Classes.ViewClasses.StockView import StockView
from Resources.Strings import Strings
from Utils.DateUtils import DateUtils
from Utils.TextUtils import TextUtils
from Environment import Environment
from datetime import datetime
import requests

class DataSynchronization(object):

#region - Public Methods
    def sync_all_stocks_and_symbols():
        stocks = []            
        try:
            symbols = DataSynchronization.__sync_get_all_stocks_symbols()
            cookie = DataSynchronization.__get_cookie_yahoo_finance_fake_request()
            crumb = DataSynchronization.__get_crumb_yahoo_finance(cookie)
            stocks = DataSynchronization.__sync_initial_all_stocks_data(symbols, crumb)
        except:
            return stocks
        return stocks

    def sync_single_stock_full_data(stock):
        stockView = StockView()
        DataSynchronization.__sync_single_get_fundamentals_series_stock_data(stockView, stock)
        DataSynchronization.__sync_chart(stock.get_sign(), APIConstants.VALUE_1D, APIConstants.VALUE_1M, stockView)

        cookie = DataSynchronization.__get_cookie_yahoo_finance_fake_request()
        crumb = DataSynchronization.__get_crumb_yahoo_finance(cookie)
        DataSynchronization.__sync_quote_of_stock(stock.get_sign(), crumb, stock)

        stockView.set_stock(stock)
        return stockView

    def sync_single_crypto_full_data(crypto):
        stockView = StockView()
        DataSynchronization.__sync_chart(crypto.get_sign(), APIConstants.VALUE_1D, APIConstants.VALUE_1M, stockView)

        # cookie = DataSynchronization.__get_cookie_yahoo_finance_fake_request()
        # crumb = DataSynchronization.__get_crumb_yahoo_finance(cookie)

        stockView.set_crypto(crypto)
        return stockView

    def sync_update_all_stocks(stocks):
        return DataSynchronization.__update_all_stocks_data(stocks)

    def sync_update_all_cryptos(cryptos):
        return DataSynchronization.__update_all_cryptos_data(cryptos)

    def sync_get_chart(symbol, rnge, interval):
        stockView = StockView()
        DataSynchronization.__sync_chart(symbol, rnge, interval, stockView)
        return stockView

    def sync_all_crypto():
        return DataSynchronization.__sync_get_all_cryptos()
#endregion

#region - Private Methods
#region - Initial Stock Sync Methods
    def __sync_get_all_stocks_symbols():
        j = json.loads(Networking.download_all_stock_analysis_symbols(APIConstants.HEADERS_ONE))
        symbols = []
        if j[APIConstants.FIELD_STATUS] == 200:
            for d in j[APIConstants.FIELD_DATA][APIConstants.FIELD_DATA]:
                if d[APIConstants.FIELD_S] not in symbols:
                    symbols.append(d[APIConstants.FIELD_S])

        # jj = json.loads(Networking.download_gov_all_stock_symbols(APIConstants.HEADERS_ONE))
        # if jj:
        #     for i in range(0, 100000):
        #         if str(i) in jj.keys():
        #             if jj[str(i)]["ticker"] not in symbols:
        #                 symbols.append(jj[str(i)]["ticker"])
        #         else:
        #             break

        return symbols

        
    def __sync_initial_all_stocks_data(symbols, crumb):
        arrStocks = []

        for i in range(0, len(symbols), 500):
            DataSynchronization.__sync_initial_stocks_data(crumb, symbols[i:i+500], arrStocks)

        
        if len(symbols) % 500 != 0:
            DataSynchronization.__sync_initial_stocks_data(crumb, symbols[-(len(symbols) % 500):], arrStocks)

        return arrStocks

    def __sync_initial_stocks_data(crumb, symbols, arrStocks):
        jj = json.loads(Networking.download_quote_of_stock(",".join(symbols), crumb, APIConstants.HEADERS_ONE))

        if jj is not None:
            for j in jj[APIConstants.FIELD_QUOTE_RESPONSE][APIConstants.FIELD_RESULT]:
                
                company = Company(uuid.uuid4())
                stock = Stock(uuid.uuid4())
                exchange = Exchange(uuid.uuid4())

                if APIConstants.FIELD_LONG_NAME not in j and APIConstants.FIELD_SHORT_NAME not in j:
                    continue

                if APIConstants.FIELD_LONG_NAME in j:                    
                    company.set_name(j[APIConstants.FIELD_LONG_NAME])
                
                if APIConstants.FIELD_SHORT_NAME in j:
                    company.set_short_name(j[APIConstants.FIELD_SHORT_NAME])
                    stock.set_name(j[APIConstants.FIELD_SHORT_NAME])

                if company.get_name() is not None and company.get_short_name() is None:
                    company.set_short_name(company.get_name())
                    stock.set_name(company.get_name())
                elif company.get_name() is None and company.get_short_name() is not None:
                    company.set_name(company.get_short_name())

                stock.set_company(company)

                stock.set_sign(j[APIConstants.FIELD_SYMBOL])

                if APIConstants.FIELD_CURRENCY in j:
                    exchange.set_currency(j[APIConstants.FIELD_CURRENCY])
                elif APIConstants.FIELD_FINANCIAL_CURRENCY in j:
                    exchange.set_currency(j[APIConstants.FIELD_FINANCIAL_CURRENCY])
                
                if APIConstants.FIELD_EXCHANGE in j:
                    exchange.set_name(j[APIConstants.FIELD_EXCHANGE])

                if APIConstants.FIELD_FULL_EXCHANGE_NAME in j:
                    exchange.set_full_name(j[APIConstants.FIELD_FULL_EXCHANGE_NAME])

                stock.set_exchange(exchange)

                if APIConstants.FIELD_PRE_MARKET_CHANGE_PERCENT in j:
                    stock.set_pre_market_change_percent(j[APIConstants.FIELD_PRE_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_PRE_MARKET_PRICE in j:
                    stock.set_pre_market_price(j[APIConstants.FIELD_PRE_MARKET_PRICE])
                else:
                    stock.set_pre_market_price(None)

                if APIConstants.FIELD_HAS_PRE_POST_MARKET_DATA in j:
                    stock.set_has_pre_post_market_data(j[APIConstants.FIELD_HAS_PRE_POST_MARKET_DATA])
                
                if APIConstants.FIELD_FIRST_TRADE_DATE_MILLISECONDS in j:
                    stock.set_first_trade_date(j[APIConstants.FIELD_FIRST_TRADE_DATE_MILLISECONDS])

                if APIConstants.FIELD_DISPLAY_NAME in j:
                    stock.set_name(j[APIConstants.FIELD_DISPLAY_NAME])

                if APIConstants.FIELD_REGULAR_MARKET_PRICE in j:
                    stock.set_price(j[APIConstants.FIELD_REGULAR_MARKET_PRICE])

                if APIConstants.FIELD_REGULAR_MARKET_DAY_HIGH in j:
                    stock.set_day_max(j[APIConstants.FIELD_REGULAR_MARKET_DAY_HIGH])

                if APIConstants.FIELD_REGULAR_MARKET_DAY_LOW in j:
                    stock.set_day_min(j[APIConstants.FIELD_REGULAR_MARKET_DAY_LOW])

                if APIConstants.FIELD_REGULAR_MARKET_VOLUME in j:
                    stock.set_volume(j[APIConstants.FIELD_REGULAR_MARKET_VOLUME])

                if APIConstants.FIELD_REGULAR_MARKET_PREVIOUS_CLOSE in j:
                    stock.set_price_previous_close(j[APIConstants.FIELD_REGULAR_MARKET_PREVIOUS_CLOSE])

                if APIConstants.FIELD_ASK in j:
                    stock.set_ask(j[APIConstants.FIELD_ASK])

                if APIConstants.FIELD_ASK_SIZE in j:
                    stock.set_ask_size(j[APIConstants.FIELD_ASK_SIZE])

                if APIConstants.FIELD_BID in j:
                    stock.set_bid(j[APIConstants.FIELD_BID])

                if APIConstants.FIELD_BID_SIZE in j:
                    stock.set_bid_size(j[APIConstants.FIELD_BID_SIZE])
                    
                if APIConstants.FIELD_AVG_DAILY_VOLUME_TEN_DAYS in j:
                    stock.set_avg_volume_ten_days(j[APIConstants.FIELD_AVG_DAILY_VOLUME_TEN_DAYS])

                if APIConstants.FIELD_AVG_DAILY_VOLUME_THREE_MONTH in j:
                    stock.set_avg_volume_three_months(j[APIConstants.FIELD_AVG_DAILY_VOLUME_THREE_MONTH])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_RANGE in j:
                    stock.set_fifty_two_weeks_range(j[APIConstants.FIELD_FIFTY_TWO_WEEK_RANGE])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH in j:
                    stock.set_fifty_two_weeks_high(j[APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_LOW in j:
                    stock.set_fifty_two_weeks_low(j[APIConstants.FIELD_FIFTY_TWO_WEEK_LOW])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT in j:
                    stock.set_fifty_two_weeks_perc_change(j[APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT])

                if APIConstants.FIELD_SHARES_OUTSTANDING in j:
                    stock.set_shares_outstanding(j[APIConstants.FIELD_SHARES_OUTSTANDING])

                if APIConstants.FIELD_PRICE_TO_BOOK in j:
                    stock.set_price_to_book(j[APIConstants.FIELD_PRICE_TO_BOOK])

                if APIConstants.FIELD_MARKET_CAP in j:
                    stock.set_market_cap(j[APIConstants.FIELD_MARKET_CAP])

                if APIConstants.FIELD_AVERAGE_ANALYST_RATING in j:
                    stock.set_average_analyst_rating(j[APIConstants.FIELD_AVERAGE_ANALYST_RATING])

                if APIConstants.FIELD_REGULAR_MARKET_CHANGE_PERCENT in j:
                    stock.set_market_change_percent(j[APIConstants.FIELD_REGULAR_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_POST_MARKET_CHANGE_PERCENT in j:
                    stock.set_post_market_change_percent(j[APIConstants.FIELD_POST_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_POST_MARKET_TIME in j:
                    stock.set_post_market_time(j[APIConstants.FIELD_POST_MARKET_TIME])

                if APIConstants.FIELD_POST_MARKET_PRICE in j:
                    stock.set_post_market_price(j[APIConstants.FIELD_POST_MARKET_PRICE])
                else:
                    stock.set_post_market_price(None)

                if APIConstants.FIELD_EARNINGS_TIMESTAMP in j:
                    stock.set_earnings_timestamp(j[APIConstants.FIELD_EARNINGS_TIMESTAMP])

                if APIConstants.FIELD_BOOK_VALUE in j:
                    stock.set_book_value_per_share(j[APIConstants.FIELD_BOOK_VALUE])

                if APIConstants.FIELD_EPS_TRAILING_TWELVE_MONTHS in j:
                    stock.set_eps_trailing_twelve_months(j[APIConstants.FIELD_EPS_TRAILING_TWELVE_MONTHS])

                if APIConstants.FIELD_EPS_FORWARD in j:
                    stock.set_eps_forward(j[APIConstants.FIELD_EPS_FORWARD])

                if APIConstants.FIELD_EPS_CURRENT_YEAR in j:
                    stock.set_eps_current_year(j[APIConstants.FIELD_EPS_CURRENT_YEAR])

                if APIConstants.FIELD_PRICE_EPS_CURRENT_YEAR in j:
                    stock.set_price_eps_current_year_ratio(j[APIConstants.FIELD_PRICE_EPS_CURRENT_YEAR])

                if APIConstants.FIELD_FORWARD_PE in j:
                    stock.set_forward_price_earnings(j[APIConstants.FIELD_FORWARD_PE])

                if APIConstants.FIELD_TRAILING_PE in j:
                    stock.set_trailing_price_earnings(j[APIConstants.FIELD_TRAILING_PE])

                if APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_RATE in j:
                    stock.set_trailing_annual_dividend_rate(j[APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_RATE])

                if APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_YELD in j:
                    stock.set_trailing_annual_dividend_yeld(j[APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_YELD])

                if APIConstants.FIELD_DIVIDEND_DATE in j:
                    stock.set_dividend_date(j[APIConstants.FIELD_DIVIDEND_DATE])

                if APIConstants.FIELD_DIVIDEND_RATE in j:
                    stock.set_dividend_rate(j[APIConstants.FIELD_DIVIDEND_RATE])

                arrStocks.append(stock)
#endregion

#region - Single Stock Sync Methods
    def __sync_single_get_fundamentals_series_stock_data(stockView, stock):
        j = json.loads(Networking.download_fundamentals_timeseries_stock_data(stock.get_sign(), 
            TextUtils.remove_point_and_before_point(str(DateUtils.convert_date_to_unix_date_format_dash_ymdHMs(str(DateUtils.get_diff_date_years(DateUtils.get_current_date(), 1))))),
            TextUtils.remove_point_and_before_point(str(DateUtils.get_current_date_unix_time())), 
            ",".join(APIConstants.FIELDS_API_GET_FUNDAMENTALS_SERIES_STOCK), APIConstants.HEADERS_ONE))

        for jj in j[APIConstants.FIELD_TIMESERIES][APIConstants.FIELD_RESULT]:
            for attr in APIConstants.FIELDS_API_GET_FUNDAMENTALS_SERIES_STOCK:
                if attr in jj:
                    match attr:
                        case APIConstants.FIELD_QUARTERLY_MARKET_CAP:
                            stockView.set_quarterly_market_cap(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_TRAILING_MARKET_CAP:
                            stockView.set_trailing_market_cap(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_QUARTERLY_ENTERPRISE_VALUE:
                            stockView.set_quarterly_enterprise_value(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_TRAILING_ENTERPRISE_VALUE:
                            stockView.set_trailing_enterprise_value(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))
                            try:
                                stock.set_enterprise_value(jj[attr][len(jj[attr]) - 1][APIConstants.FIELD_REPORTED_VALUE][APIConstants.FIELD_RAW])
                            except:
                                Environment().get_logger().error(DataSynchronization.__name__ + " - " + Strings.STR_ERROR_JSON)

                        case APIConstants.FIELD_QUARTERLY_PE_RATIO:
                            stockView.set_quarterly_pe_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_TRALING_PE_RATIO:
                            stockView.set_trailing_pe_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))
                            try:
                                stock.set_pe_ratio(jj[attr][len(jj[attr]) - 1][APIConstants.FIELD_REPORTED_VALUE][APIConstants.FIELD_RAW])
                            except:
                                Environment().get_logger().error(DataSynchronization.__name__ + " - " + Strings.STR_ERROR_JSON)

                        case APIConstants.FIELD_QUARTERLY_FORWARD_PE_RATIO:
                            stockView.set_quarterly_forward_pe_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_TRALING_FORWARD_PE_RATIO:
                            stockView.set_trailing_forward_pe_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_QUARTERLY_PEG_RATIO:
                            stockView.set_quarterly_peg_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_TRAILING_PEG_RATIO:
                            stockView.set_trailing_peg_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))
                            try:
                                stock.set_peg_ratio(jj[attr][len(jj[attr]) - 1][APIConstants.FIELD_REPORTED_VALUE][APIConstants.FIELD_RAW])
                            except:
                                Environment().get_logger().error(DataSynchronization.__name__ + " - " + Strings.STR_ERROR_JSON)

                        case APIConstants.FIELD_QUARTERLY_PS_RATIO:
                            stockView.set_quarterly_ps_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_TRALING_PS_RATIO:
                            stockView.set_trailing_pe_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_QUARTERLY_PB_RATIO:
                            stockView.set_quarterly_pb_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_TRAILING_PB_RATIO:
                            stockView.set_trailing_pb_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))
                            try:
                                stock.set_pb_ratio(jj[attr][len(jj[attr]) - 1][APIConstants.FIELD_REPORTED_VALUE][APIConstants.FIELD_RAW])
                            except:
                                Environment().get_logger().error(DataSynchronization.__name__ + " - " + Strings.STR_ERROR_JSON)

                        case APIConstants.FIELD_QUARTERLY_ENTERPRISES_VALUE_REVENUE_RATIO:
                            stockView.set_quarterly_enterprises_value_revenue_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_TRAILING_ENTERPRISES_VALUE_REVENUE_RATIO:
                            stockView.set_trailing_enterprises_value_revenue_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))
                            try:
                                stock.set_enterprises_value_revenue_ratio(jj[attr][len(jj[attr]) - 1][APIConstants.FIELD_REPORTED_VALUE][APIConstants.FIELD_RAW])
                            except:
                                Environment().get_logger().error(DataSynchronization.__name__ + " - " + Strings.STR_ERROR_JSON)

                        case APIConstants.FIELD_QUARTERLY_ENTERPRISES_VALUE_EBITDA_RATIO:
                            stockView.set_quarterly_enterprises_value_ebitda_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))

                        case APIConstants.FIELD_QUARTERLY_TRAILING_ENTERPRESISES_VALUE_EBITDA_RATIO:
                            stockView.set_trailing_enterprises_value_ebitda_ratio(DataSynchronization.__init_and_elaborate_value_dictionary_single_stock_full_data(jj[attr]))
                            try:
                                stock.set_enterprises_value_ebitda_ratio(jj[attr][len(jj[attr]) - 1][APIConstants.FIELD_REPORTED_VALUE][APIConstants.FIELD_RAW])
                            except:
                                Environment().get_logger().error(DataSynchronization.__name__ + " - " + Strings.STR_ERROR_JSON)

    def __sync_chart(symbol, rnge, interval, stockView):
        jj = json.loads(Networking.download_chart(symbol, rnge, interval, APIConstants.HEADERS_ONE))

        for j in jj[APIConstants.FIELD_CHART][APIConstants.FIELD_RESULT]:
            timestamps = []

            if APIConstants.FIELD_TIMESTAMP in j:
                for t in j[APIConstants.FIELD_TIMESTAMP]:
                    if rnge == APIConstants.VALUE_1D:
                        timestamps.append(datetime.utcfromtimestamp(t).strftime('%H:%M:%S'))
                    else:
                        timestamps.append(datetime.utcfromtimestamp(t).strftime('%d/%m/%Y %H:%M:%S'))

            stockView.set_timestamps(timestamps)
            
            for n in j[APIConstants.FIELD_INDICATORS][APIConstants.FIELD_QUOTE]:
                if APIConstants.FIELD_VOLUME in n:
                    stockView.set_volumes(n[APIConstants.FIELD_VOLUME])
                
                if APIConstants.FIELD_CLOSE in n:
                    stockView.set_closes(n[APIConstants.FIELD_CLOSE])

                if APIConstants.FIELD_OPEN in n:
                    stockView.set_opens(n[APIConstants.FIELD_OPEN])

    def __init_and_elaborate_value_dictionary_single_stock_full_data(jj):
        dicti = {}
        for e in jj:
            if e is not None:
                dicti[e[APIConstants.FIELD_AS_OF_DATE]] = {}
                dicti[e[APIConstants.FIELD_AS_OF_DATE]][APIConstants.FIELD_RAW] = e[APIConstants.FIELD_REPORTED_VALUE][APIConstants.FIELD_RAW]
                dicti[e[APIConstants.FIELD_AS_OF_DATE]][APIConstants.FIELD_FMT] = e[APIConstants.FIELD_REPORTED_VALUE][APIConstants.FIELD_FMT]
        return dicti

    def __get_cookie_yahoo_finance_fake_request():
        res = Networking.download_request_yahoo_finance_get_cookie(APIConstants.HEADERS_ONE)
        return res.headers[APIConstants.HEADER_SET_COOKIE][0:res.headers[APIConstants.HEADER_SET_COOKIE].index(";")]

    def __get_crumb_yahoo_finance(cookie):
        headers = APIConstants.HEADERS_ONE
        headers[APIConstants.HEADER_COOKIE] = cookie
        crumb = Networking.download_get_crumb_yahoo_finance(headers)
        return crumb

    def __sync_quote_of_stock(symbol, crumb, stock):
        jj = json.loads(Networking.download_quote_of_stock(symbol, crumb, APIConstants.HEADERS_ONE))
        
        if jj is not None:
            for j in jj[APIConstants.FIELD_QUOTE_RESPONSE][APIConstants.FIELD_RESULT]:
                
                if APIConstants.FIELD_DISPLAY_NAME in j:
                    stock.set_name(j[APIConstants.FIELD_DISPLAY_NAME])

                stock.set_price(j[APIConstants.FIELD_REGULAR_MARKET_PRICE])
                stock.set_day_max(j[APIConstants.FIELD_REGULAR_MARKET_DAY_HIGH])
                stock.set_day_min(j[APIConstants.FIELD_REGULAR_MARKET_DAY_LOW])
                stock.set_volume(j[APIConstants.FIELD_REGULAR_MARKET_VOLUME])
                stock.set_price_previous_close(j[APIConstants.FIELD_REGULAR_MARKET_PREVIOUS_CLOSE])

                if APIConstants.FIELD_ASK in j:
                    stock.set_ask(j[APIConstants.FIELD_ASK])
                    
                if APIConstants.FIELD_ASK_SIZE in j:
                    stock.set_ask_size(j[APIConstants.FIELD_ASK_SIZE])

                if APIConstants.FIELD_BID in j:
                    stock.set_bid(j[APIConstants.FIELD_BID])

                if APIConstants.FIELD_BID_SIZE in j:
                    stock.set_bid_size(j[APIConstants.FIELD_BID_SIZE])
                    
                if APIConstants.FIELD_AVG_DAILY_VOLUME_TEN_DAYS in j:
                    stock.set_avg_volume_ten_days(j[APIConstants.FIELD_AVG_DAILY_VOLUME_TEN_DAYS])

                if APIConstants.FIELD_AVG_DAILY_VOLUME_THREE_MONTH in j:
                    stock.set_avg_volume_three_months(j[APIConstants.FIELD_AVG_DAILY_VOLUME_THREE_MONTH])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_RANGE in j:
                    stock.set_fifty_two_weeks_range(j[APIConstants.FIELD_FIFTY_TWO_WEEK_RANGE])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH in j:
                    stock.set_fifty_two_weeks_high(j[APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_LOW in j:
                    stock.set_fifty_two_weeks_low(j[APIConstants.FIELD_FIFTY_TWO_WEEK_LOW])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT in j:
                    stock.set_fifty_two_weeks_perc_change(j[APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT])

                if APIConstants.FIELD_SHARES_OUTSTANDING in j:
                    stock.set_shares_outstanding(j[APIConstants.FIELD_SHARES_OUTSTANDING])

                if APIConstants.FIELD_PRICE_TO_BOOK in j:
                    stock.set_price_to_book(j[APIConstants.FIELD_PRICE_TO_BOOK])

                stock.set_market_cap(j[APIConstants.FIELD_MARKET_CAP])

                if APIConstants.FIELD_AVERAGE_ANALYST_RATING in j:
                    stock.set_average_analyst_rating(j[APIConstants.FIELD_AVERAGE_ANALYST_RATING])

                stock.set_market_change_percent(j[APIConstants.FIELD_REGULAR_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_PRE_MARKET_PRICE in j:
                    stock.set_pre_market_price(j[APIConstants.FIELD_PRE_MARKET_PRICE])
                else:
                    stock.set_pre_market_price(None)

                if APIConstants.FIELD_PRE_MARKET_CHANGE_PERCENT in j:
                    stock.set_pre_market_change_percent(j[APIConstants.FIELD_PRE_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_POST_MARKET_CHANGE_PERCENT in j:
                    stock.set_post_market_change_percent(j[APIConstants.FIELD_POST_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_POST_MARKET_TIME in j:
                    stock.set_post_market_time(j[APIConstants.FIELD_POST_MARKET_TIME])
                
                if APIConstants.FIELD_POST_MARKET_PRICE in j:
                    stock.set_post_market_price(j[APIConstants.FIELD_POST_MARKET_PRICE])
                else:
                    stock.set_post_market_price(None)

                if APIConstants.FIELD_EARNINGS_TIMESTAMP in j:
                    stock.set_earnings_timestamp(j[APIConstants.FIELD_EARNINGS_TIMESTAMP])

                stock.set_book_value_per_share(j[APIConstants.FIELD_BOOK_VALUE])

                if APIConstants.FIELD_EPS_TRAILING_TWELVE_MONTHS in j:
                    stock.set_eps_trailing_twelve_months(j[APIConstants.FIELD_EPS_TRAILING_TWELVE_MONTHS])

                if APIConstants.FIELD_EPS_FORWARD in j:
                    stock.set_eps_forward(j[APIConstants.FIELD_EPS_FORWARD])

                if APIConstants.FIELD_EPS_CURRENT_YEAR in j:
                    stock.set_eps_current_year(j[APIConstants.FIELD_EPS_CURRENT_YEAR])

                if APIConstants.FIELD_PRICE_EPS_CURRENT_YEAR in j:
                    stock.set_price_eps_current_year_ratio(j[APIConstants.FIELD_PRICE_EPS_CURRENT_YEAR])

                if APIConstants.FIELD_FORWARD_PE in j:
                    stock.set_forward_price_earnings(j[APIConstants.FIELD_FORWARD_PE])

                if APIConstants.FIELD_TRAILING_PE in j:
                    stock.set_trailing_price_earnings(j[APIConstants.FIELD_TRAILING_PE])

                stock.set_trailing_annual_dividend_rate(j[APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_RATE])
                stock.set_trailing_annual_dividend_yeld(j[APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_YELD])

                if APIConstants.FIELD_DIVIDEND_DATE in j:
                    stock.set_dividend_date(j[APIConstants.FIELD_DIVIDEND_DATE])

                if APIConstants.FIELD_DIVIDEND_RATE in j:
                    stock.set_dividend_rate(j[APIConstants.FIELD_DIVIDEND_RATE])
#endregion

#region - Sync All Stocks Data Methods
    def __update_all_stocks_data(stocks):        
        cookie = DataSynchronization.__get_cookie_yahoo_finance_fake_request()
        crumb = DataSynchronization.__get_crumb_yahoo_finance(cookie)

        for i in range(0, len(stocks), 500):
            DataSynchronization.__update_stock_data(crumb, stocks[i:i+500])

        if len(stocks) > 500 and len(stocks) % 500 != 0:
            DataSynchronization.__update_stock_data(crumb, stocks[-(len(stocks) % 500):])

        return stocks

    def __update_stock_data(crumb, stocks):
        symbols = []
        for s in stocks:
            if s is not None:
                symbols.append(s.get_sign())

        jj = json.loads(Networking.download_quote_of_stock(",".join(symbols), crumb, APIConstants.HEADERS_ONE))

        if jj is not None:
            for i in range(0, len(jj[APIConstants.FIELD_QUOTE_RESPONSE][APIConstants.FIELD_RESULT])):
                stock = stocks[i]

                j = jj[APIConstants.FIELD_QUOTE_RESPONSE][APIConstants.FIELD_RESULT][i]

                if APIConstants.FIELD_PRE_MARKET_PRICE in j:
                    stock.set_pre_market_price(j[APIConstants.FIELD_PRE_MARKET_PRICE])
                else:
                    stock.set_pre_market_price(None)

                if APIConstants.FIELD_HAS_PRE_POST_MARKET_DATA in j:
                    stock.set_has_pre_post_market_data(j[APIConstants.FIELD_HAS_PRE_POST_MARKET_DATA])

                if APIConstants.FIELD_REGULAR_MARKET_PRICE in j:
                    stock.set_price(j[APIConstants.FIELD_REGULAR_MARKET_PRICE])

                if APIConstants.FIELD_REGULAR_MARKET_DAY_HIGH in j:
                    stock.set_day_max(j[APIConstants.FIELD_REGULAR_MARKET_DAY_HIGH])

                if APIConstants.FIELD_REGULAR_MARKET_DAY_LOW in j:
                    stock.set_day_min(j[APIConstants.FIELD_REGULAR_MARKET_DAY_LOW])

                if APIConstants.FIELD_REGULAR_MARKET_VOLUME in j:
                    stock.set_volume(j[APIConstants.FIELD_REGULAR_MARKET_VOLUME])

                if APIConstants.FIELD_REGULAR_MARKET_PREVIOUS_CLOSE in j:
                    stock.set_price_previous_close(j[APIConstants.FIELD_REGULAR_MARKET_PREVIOUS_CLOSE])

                if APIConstants.FIELD_ASK in j:
                    stock.set_ask(j[APIConstants.FIELD_ASK])

                if APIConstants.FIELD_ASK_SIZE in j:
                    stock.set_ask_size(j[APIConstants.FIELD_ASK_SIZE])

                if APIConstants.FIELD_BID in j:
                    stock.set_bid(j[APIConstants.FIELD_BID])

                if APIConstants.FIELD_BID_SIZE in j:
                    stock.set_bid_size(j[APIConstants.FIELD_BID_SIZE])
                    
                if APIConstants.FIELD_PRE_MARKET_CHANGE_PERCENT in j:
                    stock.set_pre_market_change_percent(j[APIConstants.FIELD_PRE_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_AVG_DAILY_VOLUME_TEN_DAYS in j:
                    stock.set_avg_volume_ten_days(j[APIConstants.FIELD_AVG_DAILY_VOLUME_TEN_DAYS])

                if APIConstants.FIELD_AVG_DAILY_VOLUME_THREE_MONTH in j:
                    stock.set_avg_volume_three_months(j[APIConstants.FIELD_AVG_DAILY_VOLUME_THREE_MONTH])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_RANGE in j:
                    stock.set_fifty_two_weeks_range(j[APIConstants.FIELD_FIFTY_TWO_WEEK_RANGE])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH in j:
                    stock.set_fifty_two_weeks_high(j[APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_LOW in j:
                    stock.set_fifty_two_weeks_low(j[APIConstants.FIELD_FIFTY_TWO_WEEK_LOW])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT in j:
                    stock.set_fifty_two_weeks_perc_change(j[APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT])

                if APIConstants.FIELD_SHARES_OUTSTANDING in j:
                    stock.set_shares_outstanding(j[APIConstants.FIELD_SHARES_OUTSTANDING])

                if APIConstants.FIELD_PRICE_TO_BOOK in j:
                    stock.set_price_to_book(j[APIConstants.FIELD_PRICE_TO_BOOK])

                if APIConstants.FIELD_MARKET_CAP in j:
                    stock.set_market_cap(j[APIConstants.FIELD_MARKET_CAP])

                if APIConstants.FIELD_AVERAGE_ANALYST_RATING in j:
                    stock.set_average_analyst_rating(j[APIConstants.FIELD_AVERAGE_ANALYST_RATING])

                if APIConstants.FIELD_REGULAR_MARKET_CHANGE_PERCENT in j:
                    stock.set_market_change_percent(j[APIConstants.FIELD_REGULAR_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_POST_MARKET_CHANGE_PERCENT in j:
                    stock.set_post_market_change_percent(j[APIConstants.FIELD_POST_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_POST_MARKET_TIME in j:
                    stock.set_post_market_time(j[APIConstants.FIELD_POST_MARKET_TIME])

                if APIConstants.FIELD_POST_MARKET_PRICE in j:
                    stock.set_post_market_price(j[APIConstants.FIELD_POST_MARKET_PRICE])
                else:
                    stock.set_post_market_price(None)

                if APIConstants.FIELD_EARNINGS_TIMESTAMP in j:
                    stock.set_earnings_timestamp(j[APIConstants.FIELD_EARNINGS_TIMESTAMP])

                if APIConstants.FIELD_BOOK_VALUE in j:
                    stock.set_book_value_per_share(j[APIConstants.FIELD_BOOK_VALUE])

                if APIConstants.FIELD_EPS_TRAILING_TWELVE_MONTHS in j:
                    stock.set_eps_trailing_twelve_months(j[APIConstants.FIELD_EPS_TRAILING_TWELVE_MONTHS])

                if APIConstants.FIELD_EPS_FORWARD in j:
                    stock.set_eps_forward(j[APIConstants.FIELD_EPS_FORWARD])

                if APIConstants.FIELD_EPS_CURRENT_YEAR in j:
                    stock.set_eps_current_year(j[APIConstants.FIELD_EPS_CURRENT_YEAR])

                if APIConstants.FIELD_PRICE_EPS_CURRENT_YEAR in j:
                    stock.set_price_eps_current_year_ratio(j[APIConstants.FIELD_PRICE_EPS_CURRENT_YEAR])

                if APIConstants.FIELD_FORWARD_PE in j:
                    stock.set_forward_price_earnings(j[APIConstants.FIELD_FORWARD_PE])

                if APIConstants.FIELD_TRAILING_PE in j:
                    stock.set_trailing_price_earnings(j[APIConstants.FIELD_TRAILING_PE])

                if APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_RATE in j:
                    stock.set_trailing_annual_dividend_rate(j[APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_RATE])

                if APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_YELD in j:
                    stock.set_trailing_annual_dividend_yeld(j[APIConstants.FIELD_TRAILING_ANNUAL_DIVIDEND_YELD])

                if APIConstants.FIELD_DIVIDEND_DATE in j:
                    stock.set_dividend_date(j[APIConstants.FIELD_DIVIDEND_DATE])

                if APIConstants.FIELD_DIVIDEND_RATE in j:
                    stock.set_dividend_rate(j[APIConstants.FIELD_DIVIDEND_RATE])

#endregion

#region - Update Cryptos Methods
    def __sync_get_all_cryptos():
        cryptos = []
        total = 250
        start = 0
        while True:
            jj = json.loads(Networking.download_cryptocurrencies(start, APIConstants.HEADERS_ONE))

            if jj is not None:
                total = int(jj[APIConstants.FIELD_FINANCE][APIConstants.FIELD_RESULT][0][APIConstants.FIELD_TOTAL])
                for i in range(0, len(jj[APIConstants.FIELD_FINANCE][APIConstants.FIELD_RESULT][0][APIConstants.FIELD_QUOTES])):
                    j = jj[APIConstants.FIELD_FINANCE][APIConstants.FIELD_RESULT][0][APIConstants.FIELD_QUOTES][i]
                    
                    crypto = Cryptocurrency(uuid.uuid4())
                    exchange = Exchange(uuid.uuid4())

                    exchange.set_full_name(j[APIConstants.FIELD_FULL_EXCHANGE_NAME])
                    crypto.set_exchange(exchange)
                    crypto.set_sign(j[APIConstants.FIELD_SYMBOL])

                    if APIConstants.FIELD_COIN_IMAGE_URL in j:
                        crypto.set_image_url(j[APIConstants.FIELD_COIN_IMAGE_URL])

                    if APIConstants.FIELD_REGULAR_MARKET_CHANGE_PERCENT in j:
                        crypto.set_market_change_percent(j[APIConstants.FIELD_REGULAR_MARKET_CHANGE_PERCENT][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_FIFTY_TWO_WEEK_LOW_CHANGE_PERCENT in j:
                        crypto.set_fifty_two_week_low_change_percent(j[APIConstants.FIELD_FIFTY_TWO_WEEK_LOW_CHANGE_PERCENT][APIConstants.FIELD_FMT])

                    if APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH_CHANGE_PERCENT in j:
                        crypto.set_fifty_two_week_high_change_percent(j[APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH_CHANGE_PERCENT][APIConstants.FIELD_FMT])

                    if APIConstants.FIELD_FIFTY_TWO_WEEK_LOW_CHANGE in j:
                        crypto.set_fifty_two_week_low_change(j[APIConstants.FIELD_FIFTY_TWO_WEEK_LOW_CHANGE][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH_CHANGE in j:
                        crypto.set_fifty_two_week_high_change(j[APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH_CHANGE][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_FIFTY_TWO_WEEK_LOW in j:
                        crypto.set_fifty_two_weeks_low(j[APIConstants.FIELD_FIFTY_TWO_WEEK_LOW][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH in j:
                        crypto.set_fifty_two_weeks_high(j[APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT in j:
                        crypto.set_fifty_two_weeks_perc_change(j[APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_CIRCULATING_SUPPLY in j:
                        crypto.set_circulating_supply(j[APIConstants.FIELD_CIRCULATING_SUPPLY][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_REGULAR_MARKET_DAY_RANGE in j:
                        crypto.set_regular_market_day_range(j[APIConstants.FIELD_REGULAR_MARKET_DAY_RANGE][APIConstants.FIELD_FMT])

                    if APIConstants.FIELD_REGULAR_MARKET_PRICE in j:
                        crypto.set_price(j[APIConstants.FIELD_REGULAR_MARKET_PRICE][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_REGULAR_MARKET_VOLUME in j:
                        crypto.set_volume(j[APIConstants.FIELD_REGULAR_MARKET_VOLUME][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_VOLUME_24H in j:
                        crypto.set_volume_twenty_four_hours(j[APIConstants.FIELD_VOLUME_24H][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_VOLUME_ALL_CURRENCIES in j:
                        crypto.set_volume_all_currencies(j[APIConstants.FIELD_VOLUME_ALL_CURRENCIES][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_MARKET_CAP in j:
                        crypto.set_market_cap(j[APIConstants.FIELD_MARKET_CAP][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_REGULAR_MARKET_DAY_HIGH in j:
                        crypto.set_day_max(j[APIConstants.FIELD_REGULAR_MARKET_DAY_HIGH][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_REGULAR_MARKET_DAY_LOW in j:
                        crypto.set_day_min(j[APIConstants.FIELD_REGULAR_MARKET_DAY_LOW][APIConstants.FIELD_RAW])

                    if APIConstants.FIELD_LONG_NAME in j:
                        crypto.set_name(j[APIConstants.FIELD_LONG_NAME])

                    cryptos.append(crypto)

            if start >= total:
                break
            elif start + 250 >= total:
                start += total % 250
            else:
                start += 250

        return cryptos

    def __update_all_cryptos_data(cryptos):        
        cookie = DataSynchronization.__get_cookie_yahoo_finance_fake_request()
        crumb = DataSynchronization.__get_crumb_yahoo_finance(cookie)

        for i in range(0, len(cryptos), 250):
            DataSynchronization.__update_crypto_data(crumb, cryptos[i:i+500])

        if len(cryptos) > 250 and len(cryptos) % 250 != 0:
            DataSynchronization.__update_crypto_data(crumb, cryptos[-(len(cryptos) % 500):])

        return cryptos

    def __update_crypto_data(crumb, cryptos):
        symbols = []
        for s in cryptos:
            if s is not None:
                symbols.append(s.get_sign())

        jj = json.loads(Networking.download_quote_of_stock(",".join(symbols), crumb, APIConstants.HEADERS_ONE))

        if jj is not None:
            for i in range(0, len(jj[APIConstants.FIELD_QUOTE_RESPONSE][APIConstants.FIELD_RESULT])):
                crypto = cryptos[i]

                j = jj[APIConstants.FIELD_QUOTE_RESPONSE][APIConstants.FIELD_RESULT][i]

                if APIConstants.FIELD_COIN_IMAGE_URL in j:
                    crypto.set_image_url(j[APIConstants.FIELD_COIN_IMAGE_URL])

                if APIConstants.FIELD_REGULAR_MARKET_CHANGE_PERCENT in j:
                    crypto.set_market_change_percent(j[APIConstants.FIELD_REGULAR_MARKET_CHANGE_PERCENT])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_LOW_CHANGE_PERCENT in j:
                    crypto.set_fifty_two_week_low_change_percent(j[APIConstants.FIELD_FIFTY_TWO_WEEK_LOW_CHANGE_PERCENT])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH_CHANGE_PERCENT in j:
                    crypto.set_fifty_two_week_high_change_percent(j[APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH_CHANGE_PERCENT])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_LOW_CHANGE in j:
                    crypto.set_fifty_two_week_low_change(j[APIConstants.FIELD_FIFTY_TWO_WEEK_LOW_CHANGE])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH_CHANGE in j:
                    crypto.set_fifty_two_week_high_change(j[APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH_CHANGE])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_LOW in j:
                    crypto.set_fifty_two_weeks_low(j[APIConstants.FIELD_FIFTY_TWO_WEEK_LOW])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH in j:
                    crypto.set_fifty_two_weeks_high(j[APIConstants.FIELD_FIFTY_TWO_WEEK_HIGH])

                if APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT in j:
                    crypto.set_fifty_two_weeks_perc_change(j[APIConstants.FIELD_FIFTY_TWO_WEEK_CHANGE_PERCENT])

                if APIConstants.FIELD_CIRCULATING_SUPPLY in j:
                    crypto.set_circulating_supply(j[APIConstants.FIELD_CIRCULATING_SUPPLY])

                if APIConstants.FIELD_REGULAR_MARKET_DAY_RANGE in j:
                    crypto.set_regular_market_day_range(j[APIConstants.FIELD_REGULAR_MARKET_DAY_RANGE])

                if APIConstants.FIELD_REGULAR_MARKET_PRICE in j:
                    crypto.set_price(j[APIConstants.FIELD_REGULAR_MARKET_PRICE])

                if APIConstants.FIELD_REGULAR_MARKET_VOLUME in j:
                    crypto.set_volume(j[APIConstants.FIELD_REGULAR_MARKET_VOLUME])

                if APIConstants.FIELD_VOLUME_24H in j:
                    crypto.set_volume_twenty_four_hours(j[APIConstants.FIELD_VOLUME_24H])

                if APIConstants.FIELD_VOLUME_ALL_CURRENCIES in j:
                    crypto.set_volume_all_currencies(j[APIConstants.FIELD_VOLUME_ALL_CURRENCIES])

                if APIConstants.FIELD_MARKET_CAP in j:
                    crypto.set_market_cap(j[APIConstants.FIELD_MARKET_CAP])

                if APIConstants.FIELD_REGULAR_MARKET_DAY_HIGH in j:
                    crypto.set_day_max(j[APIConstants.FIELD_REGULAR_MARKET_DAY_HIGH])

                if APIConstants.FIELD_REGULAR_MARKET_DAY_LOW in j:
                    crypto.set_day_min(j[APIConstants.FIELD_REGULAR_MARKET_DAY_LOW])

                if APIConstants.FIELD_LONG_NAME in j:
                    crypto.set_name(j[APIConstants.FIELD_LONG_NAME])

                

#endregion
#endregion