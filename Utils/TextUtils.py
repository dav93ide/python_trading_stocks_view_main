
TRILLION = 1000000000000
BILLION = 1000000000
MILLION = 1000000
THOUSAND = 1000

class TextUtils(object):

    def remove_point_and_before_point(txt):
        return txt[:txt.find(".")]

    def convert_number_to_millions_form(value):
        if value / TRILLION > 0.1:
            return str(round(value / TRILLION, 2)) + " T."
        elif value / BILLION > 0.1:
            return str(round(value / BILLION, 2)) + " B."
        elif value / MILLION > 0.1:
            return str(round(value / MILLION, 2)) + " m."
        else:
            return str(round(value / THOUSAND, 2)) + " k."
