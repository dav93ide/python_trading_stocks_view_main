from Resources.Constants import Regex
import logging
import re

class RegexUtils(object):

    def check_email_format(email):
        res = re.findall(Regex.REGEX_CHECK_EMAIL, email)
        check = res and len(res) > 0 and len(res[0]) == 3
        return check

    def substitution_regex(regex, sub, string):
        return re.sub(regex, sub, string)