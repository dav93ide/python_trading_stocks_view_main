from datetime import datetime
import time
from dateutil.relativedelta import relativedelta

class DateUtils(object):

    def convert_date_to_unix(datestr, dateFormat):
        oDatetime = datetime.strptime(datestr, dateFormat)
        return oDatetime.timestamp()

    def convert_date_to_unix_date_format_standard(datestr):
        oDatetime = datetime.strptime(datestr, '%d/%m/%Y %H:%M:%S')
        return oDatetime.timestamp()

    def convert_date_to_unix_date_format_dash_ymdHMs(datestr):
        oDatetime = datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S')
        return oDatetime.timestamp()

    def get_current_date_unix_time():
        date = datetime.now()
        return datetime.timestamp(date)

    def get_current_date():
        return datetime.today().replace(microsecond=0)

    def get_current_now():
        return datetime.now().replace(microsecond=0)

    def get_diff_date_days(date, days):
        return date.replace(microsecond=0) - timedelta(days = days)

    def get_diff_date_years(date, years):
        return date - relativedelta(years = years)