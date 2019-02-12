def error_name(x):
    return x


def error_type(a):
    a = str(a)
    return a/2


def error_syntax(k):
    return isinstance(k, list)

import datetime
def error_attribute():
    return datetime.date.quarter('01.01.12')
