from enum import Enum

class Strings(object):

    STR_MAIN_FRAME = "Main Frame"
    STR_TRADING_STOCKS_VIEW = "Trading Stocks View"

#region - Strings Menu
    STR_MAIN_MENU = "Main Menu"
    STR_MENU_STOCKS = "Stocks"

#region - Strings Menu Stocks
    STR_MENU_STOCKS_VIEW = "View Stocks"
#endregion  
#endregion

    STR_INITIAL_SYNCHRONIZATION = "Initial Synchronization"
    STR_SAVE = "Save"
    STR_RESET_ALL = "Reset All"
    STR_ABORT = "Abort"
    STR_CONFIRM = "Confirm"

    STR_SEARCH = "Search"
    STR_NAME = "Name"
    STR_TYPE = "Type"
    STR_USERNAME = "Username"
    STR_PASSWORD = "Password"
    STR_PASSWORD_CHECK = "Password Check"
    STR_EMAIL = "Email"
    STR_PERCENTAGE_CAPITAL = "%"
    STR_TOT_CAPITAL = "Tot $"
    STR_USER_CAPITAL = "User Capital"
    
    STR_NAME_TRADING_STRATEGY = "Name Trading Strategy"
    STR_TRADING_STRATEGY_DATA = "Trading Strategy Data"

    STR_MAX_DAY_CHANGE = "Max Day Change"
    STR_MIN_DAY_CHANGE = "Min Day Change"
    STR_MAX_MARKET_CAP = "Max Market Cap"
    STR_MIN_MARKET_CAP = "Min Market Cap"
    STR_MAX_DAY_RANGE = "Max Day Range"
    STR_MIN_DAY_RANGE = "Min Day Range"
    STR_MAX_WEEK_RANGE = "Max Week Range"
    STR_MIN_WEEK_RANGE = "Min Week Range"
    STR_MAX_MONTH_RANGE = "Max Month Range"
    STR_MIN_MONTH_RANGE = "Min Month Range"
    STR_MAX_YEAR_RANGE = "Max Year Range"
    STR_MIN_YEAR_RANGE = "Min Year Range"
    STR_MAX_DAY_VOLUME = "Max Daily Volume"
    STR_MIN_DAY_VOLUME = "Min Daily Volume"
    STR_MAX_COMPANY_VALUE = "Max Company Value"
    STR_MIN_COMPANY_VALUE = "Min Company Value"
    STR_MAX_RATIO_COMPANY_VALUE_MARKET_CAP = "Max Ratio CV/MC"
    STR_MIN_RATIO_COMPANY_VALUE_MARKET_CAP = "Min Ratio CV/MC"
    STR_MAX_BETA = "Max BETA"
    STR_MIN_BETA = "Min BETA"
    STR_MAX_RATIO_PE = "Max Ratio PE"
    STR_MIN_RATIO_PE = "Min Ratio PE"
    STR_MAX_EPS = "Max EPS"
    STR_MIN_EPS = "Min EPS"
    STR_MAX_YEAR_TARGET = "Max Year Target"
    STR_MIN_YEAR_TARGET = "Min Year Target"
    STR_MAX_TRAILING_PE = "Max Trailing PE"
    STR_MIN_TRAILING_PE = "Min Trailing PE"
    STR_MAX_FORWARD_PE = "Max Forward PE"
    STR_MIN_FORWARD_PE = "Min Forward PE"
    STR_MAX_PEG_RATIO = "Max PEG Ratio"
    STR_MIN_PEG_RATIO = "Min PEG Ratio"
    STR_MAX_PRICE_SALES = "Max Price Sales"
    STR_MIN_PRICE_SALES = "Min Price Sales"
    STR_MAX_PRICE_BOOK = "Max Price Book"
    STR_MIN_PRICE_BOOK = "Min Price Book"
    STR_MAX_COMPANY_VALUE_REVENUE = "Max CV/RV"
    STR_MIN_COMPANY_VALUE_REVENUE = "Min CV/RV"
    STR_MAX_COMPANY_VALUE_EBITDA = "Max CV/EBITDA"
    STR_MIN_COMPANY_VALUE_EBITDA = "Min CV/EBITDA"

    STR_NAME_NEW_BOT = "Name New Bot"
    STR_TRADING_STRATEGY_TYPE = "Trading Strategy Type"
    STR_TRADING_STRATEGY = "Trading Strategy"

    STR_ERROR = "Error"
    STR_SUCCESS = "Success"

    STR_1D = "1 Day"
    STR_1D_VALUES = "1 Day Values"
    STR_1D_VOLUME = "1 Day Volume"
    STR_5D_VALUES = "5 Days Values"
    STR_5D_VOLUME = "5 Days Volume"
    STR_1MO_VALUES = "1 Month Values"
    STR_1MO_VOLUME = "1 Month Volume"
    STR_3MO_VALUES = "3 Month Values"
    STR_3MO_VOLUME = "3 Month Volume"
    STR_6MO_VALUES = "6 Month Values"
    STR_6MO_VOLUME = "6 Month Volume"
    STR_1Y_VALUES = "1 Year Values"
    STR_1Y_VOLUME = "1 Year Volume"
    STR_2Y_VALUES = "2 Year Values"
    STR_2Y_VOLUME = "2 Year Volume"
    STR_5Y_VALUES = "5 Year Values"
    STR_5Y_VOLUME = "5 Year Volume"
    STR_10Y_VALUES = "10 Year Values"
    STR_10Y_VOLUME = "10 Year Volume"
    STR_YTD_VALUES = "YTD Values"
    STR_YTD_VOLUME = "YTD Volume"
    STR_MAX_VALUES = "Max Values"
    STR_MAX_VOLUME = "Max Volume"
    STR_FIELD_MARKET_CAP = "Market Cap:"
    STR_FIELD_ENTERPRISE_VALUE = "Enterprise value:"
    STR_FIELD_DAY_MAX = "Day Max:"
    STR_FIELD_DAY_MIN = "Day Min:"
    STR_FIELD_ASK = "Ask:"
    STR_FIELD_BID = "Bid:"
    STR_FIELD_SHARES_OUTSTANDING = "Shares Outstanding:"
    STR_FIELD_52_WEEKS_MAX = "52 Weeks Max:"
    STR_FIELD_52_WEEKS_MIN = "52 Weeks Min:"
    STR_FIELD_52_WEEKS_PERC_CHANGE = "52 Weeks Change %:"
    STR_FIELD_VOLUME = "Volume:"
    STR_FIELD_VOLUME_10_DAYS = "Volume 10 Days:"
    STR_FIELD_VOLUME_3_MONTHS = "Volume 3 Months:"
    STR_FIELD_TRAILING_PRICE_EARNINGS = "Trailing Price Earnings:"
    STR_FIELD_FORWARD_PRICE_EARNINGS = "Forward Price Earnings:"
    STR_FIELD_PE_RATIO = "P/E Ratio:"
    STR_FIELD_PEG_RATIO = "PEG Ratio:"
    STR_FIELD_PB_RATIO = "PB Ratio:"
    STR_FIELD_PRICE_TO_BOOK = "Price to Book:"
    STR_FIELD_BOOK_VALUE_PER_SHARE = "Book Value per Share:"
    STR_FIELD_DIVIDEND_DATE = "Dividend Date:"
    STR_FIELD_ANNUAL_DIVIDEND_RATE = "Annual Dividend Rate:"
    STR_FIELD_ANNUAL_DIVIDEND_YELD = "Annual Dividend Yeld:"
    STR_FIELD_RATIO_ENTERPRISE_VALUE_REVENUE = "Enterprise Value / Revenue:"
    STR_FIELD_RATIO_ENTERPRISE_VALUE_EBITDA = "Enterprise Value / EBITDA:"
    STR_DOWNLOAD_DATA = "Download Data"
    STR_FIELD_PRE_MARKET = "Pre Market: $"
    STR_FIELD_POST_MARKET = "Post Market: $"
    STR_FIFTY_WEEKS_STOCK_DATA = "50 Weeks Stock Data"
    STR_STOCK_DATA = "Stock Data"
    STR_DIVIDEND_DATA = "Dividend Data"
    STR_UNDEFINED = "Undefined"

    STR_SPECIFICS_BOT = "Specifics of the BOT:"
    STR_DATA_MAKING_BOT = [
        "Max Day Change: {}",
        "Max Day Change: {}",
        "Max Market Cap: {}",
        "Max Market Cap: {}",
        "Max Day Range: {}",
        "Max Day Range: {}",
        "Max Week Range: {}",
        "Max Week Range: {}",
        "Max Month Range: {}",
        "Max Month Range: {}",
        "Max Year Range: {}",
        "Max Year Range: {}",
        "Max Day Volume: {}",
        "Max Day Volume: {}",
        "Max Company Value: {}",
        "Max Company Value: {}",
        "Max Ratio Company Value Market Cap: {}",
        "Max Ratio Company Value Market Cap: {}",
        "Max Beta: {}",
        "Max Beta: {}",
        "Max Ratio P E: {}",
        "Max Ratio P E: {}",
        "Max E P S: {}",
        "Max E P S: {}",
        "Max Year Target: {}",
        "Max Year Target: {}",
        "Max Trailing P E: {}",
        "Max Trailing P E: {}",
        "Max Forward P E: {}",
        "Max Forward P E: {}",
        "Max Peg Ratio: {}",
        "Max Peg Ratio: {}",
        "Max Price Sales: {}",
        "Max Price Sales: {}",
        "Max Price Book: {}",
        "Max Price Book: {}",
        "Max Company Value Revenue: {}",
        "Max Company Value Revenue: {}",
        "Max Company Value Ebitda: {}",
        "Max Company Value Ebitda: {}"
    ]

#region - Error Strings
    STR_ERROR_JSON = "Json Error"
#endregion

#region - Messages Question Strings
    STR_MSG_QUESTION_RESET_ALL_PARAMS_ON_VIEW = "Resettare tutti i paremetri inseriti?\nL'operazione e' irreversibile.\n\nContinuare?"
#endregion

#region - Error Messages Strings
    STR_MSG_ERROR_MISSING_VALUES = "Valore mancante per i campi:\n%s"
    STR_MSG_ERROR_WRONG_EMAIL_FORMAT = "Formato Email non valido." 
    STR_MSG_ERROR_DIFFERENT_PASSWORDS = "Le Password inserite non corrispondono." 
    STR_MSG_ERROR_VALUE = "Valore Inserito Non Valido." 
    STR_MSG_ERROR_USERNAME_PLATFORM_ALREADY_PRESENT = "Username e Piattaforma Gia` Presenti"
    STR_MSG_ERROR_INSERTED_CAPITAL_TOO_HIGH = "Capitale inserito troppo alto."
    STR_MSG_ERROR_NO_NAME_INSERTED = "Necessario Inserire Un Nome Per Continuare."
    STR_MSG_ERROR_NAME_ALREADY_PRESENT = "Nome Gia` Presente."
#endregion

#region - Success Messages Strings 
    STR_MSG_SUCCESS_INSERT_DATA = "Dati Inseriti Con Successo!"
#endregion

#region - Dialog Title Strings
    STR_DIALOG_TITLE_QUESTION_RESET_ALL_PARAMS = "Reset All Params?"
#endregion

#region - ProgressDialog Strings
    STR_PD_INITIAL_DOWNLOAD_SYMBOLS = "Initial Download Symbols."
    STR_PD_INITIAL_DOWNLOAD_STOCK_DATA = "Initial Download Stock Data."
#endregion