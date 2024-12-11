from functools import singledispatch

CHAR_FLOAT_POINT = "."
CHAR_MINUS = "-"

class NumberUtils(object):

    @singledispatch
    def get_num_digits_value(num):
        pass

    @get_num_digits_value.register(int)
    def _(num):
        return len(str(abs(num)))

    @get_num_digits_value.register(float)
    def _(num):
        return len(str(abs(num)).replace('.', ''))

    def check_is_int_or_float(value):
        return type(value) in (int, float)

    def check_input_key_only_numeric_value(value, strng):
        return value.isnumeric() or (value == CHAR_FLOAT_POINT and not CHAR_FLOAT_POINT in strng and len(strng) > 0) or (value == CHAR_MINUS and not CHAR_MINUS in strng and len(strng) == 0)

    def safe_round(value, roundd):
        if value is None:
            return 0
        else:
            return round(value, roundd)