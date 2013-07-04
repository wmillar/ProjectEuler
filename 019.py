'''
You are given the following information, but you may prefer
to do some research for yourself.

-1 Jan 1900 was a Monday.
-Thirty days has September,
 April, June and November.
 All the rest have thirty-one,
 Saving February alone,
 Which has twenty-eight, rain or shine.
 And on leap years, twenty-nine.
-A leap year occurs on any year evenly divisible by 4,
 but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def isLeapYear(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return False
        return True
    return False


def nextWeek(day, month):
    day += 7
    if day > months[month]:
        day -= months[month]
        month += 1
    return day, month


def countYear(day, month, year):
    count = 0 if day != 1 else 1
    months[2] = 29 if isLeapYear(year) else 28
    while month <= 12:
        day, month = nextWeek(day, month)
        if day == 1:
            count += 1
    if day == 1:
        count -= 1
    return day, 1, year + 1, count
    

count = 0
months = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# first Sunday of Jan 1900 is on the 7th
day, month, year, yearCount = countYear(7, 1, 1900)
while year < 2001:
    day, month, year, yearCount = countYear(day, month, year)
    count += yearCount
print count
