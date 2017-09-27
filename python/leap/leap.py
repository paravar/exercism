def is_leap_year(year):
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        print("The year %s is a leap year!") % (str(year))
        return True
    else:
        print("The year %s is NOT a leap year.") % (str(year))
        return False
