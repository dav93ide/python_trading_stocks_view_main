import logging, wx
from enum import Enum, IntEnum

class PlatformType(IntEnum):
    ETORO = 0
    WEBULL = 1
    INTERACTIVE_BROKERS = 2
    PLUS_500 = 3
    ROBINHOOD = 4

    def get_all_names():
        names = []
        for t in PlatformType.__members__:
            names.append(t)
        return names

class InvestmentType(IntEnum):
    LONG = 1
    SHORT = -1

class Sector(IntEnum):
    TECHNOLOGY = 0
    HEALTHCARE = 1
    COMMUNICATION_SERVICES = 2
    IT_SERVICES = 3
    
class AssetType(IntEnum):
    COMPANY = 0
    ETF = 1
    CRYPTO = 2
    INDEX = 3
    COMMODITY = 4
    CURRENCY = 5

class ResourceType(IntEnum):
    GOLD = 0
    OIL = 1
    NATGAS = 2
    SILVER = 3
    PLATINUM = 4

class TradingStrategyType(IntEnum):
    TRADING_STRATEGY = 0
    DIVIDEND_STRATEGY = 1
    COPY_TRADER_STRATEGY = 2

    def get_all_names():
        names = []
        for t in TradingStrategyType.__members__:
            names.append(t)
        return names

class Constants():
    DISPLAY_SIZE_MAIN_FRAME = (1000, 500)
    DISPLAY_SIZE_SEARCH_STOCKS_FRAME = (1000, 1000)

    CHOICE_EMPTY_INDEX = -1


class Sizes():
    INPUT_TEXT_SIZE_PLATFORM_DATA_PANEL = (250, 50)

    INPUT_TEXT_SIZE_NEW_TRADING_BOT_PANEL = (150, 40)
    SPACER_TRADING_BOT_PANEL_GRID = 25

    SELECTION_SIZE_TRADING_STRATEGY_TYPE_NEW_BOT = (-1, 50)
    SELECTION_SIZE_TRADING_STRATEGY_NEW_BOT = (-1, 50)

class Colors():
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    COLOR_PLATFORM_BACKGROUND_GREY = (50, 50, 50)
    COLOR_USER_CAPITAL = (0, 153, 0)

class Regex():
    REGEX_CHECK_EMAIL = "(.*)\@(gmail|libero|yahoo).(it|com|org)"
    REGEX_GET_SUBSTITUTION_PLACEHOLDER_STRING = "{(.*)}"

class Directories():
    DIR_STORED_DATA = "Stored_Data"

class DataFilenames():
    FILENAME_CONFIGURATION_DATA = "Configuration.dat"
    FILENAME_MAIN_USER_DATA = "MainUserData.dat"
    FILENAME_PLATFORM_DATA_LIST = "PlatformData.dat" 
    FILENAME_INVESTOR_DATA_LIST = "Investors.dat"
    FILENAME_TRADING_STRATEGIES = "TradingStrategies.dat"
    FILENAME_STOCK_SYMBOLS = "StockSymbols.dat"
    FILENAME_STOCK_DATA = "StockData.dat"
    FILENAME_COMPANIES = "Companies.dat"
    FILENAME_EXCHANGES = "Exchanges.dat"
    FILENAME_CURRENCIES = "Currencies.dat"
    
class Icons():
    ICON_SEARCH = "Icons/search.png"