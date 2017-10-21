# copied & pasted from someone elses code, Didn't do shit.
import datetime


def meetup_day(year, month, day_of_the_week, which):
    date = datetime.date(year, month, 1)
    one_day = datetime.timedelta(days=1)
    days = []
    while date.month == month:
        if date.strftime("%A") == day_of_the_week:
            days.append(date.day)
        date += one_day

    day = None
    if which[0].isdigit():
        try:
            index = int(which[0]) - 1
            day = days[index]
        except:
            raise ValueError
    elif which == "teenth":
        day = max(d for d in days if d >= 10 and d < 20)
    else:
        day = days[-1]

    meetup_date = datetime.date(year, month, day)
    return meetup_date
