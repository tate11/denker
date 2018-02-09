
from datetime import datetime, timedelta, date
from workalendar.america import Mexico


def sub_business_days(from_date):
    holydaysmex = Mexico()
    current_date = from_date
    weekday = current_date.weekday()
    while weekday >= 5 or not holydaysmex.is_working_day(current_date):
        current_date -= timedelta(days=1)
        weekday = current_date.weekday()
    return current_date
