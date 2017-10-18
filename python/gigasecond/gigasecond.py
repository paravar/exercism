import datetime


def add_gigasecond(datetime_var):
    return datetime_var + datetime.timedelta(seconds=10 ** 9)
