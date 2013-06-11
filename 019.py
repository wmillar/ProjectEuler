"""
You are given the following information, but you may prefer
to do some research for yourself.

>1 Jan 1900 was a Monday.
>Thirty days has September,
 April, June and November.
 All the rest have thirty-one,
 Saving February alone,
 Which has twenty-eight, rain or shine.
 And on leap years, twenty-nine.
>A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
def nextDayOfWeek(tempCurrentDayOfWeek):
    i = 0
    while i < 7:
        if tempCurrentDayOfWeek == day[-1]:
            return day[0]
        if tempCurrentDayOfWeek == day[i]:
            return day[i+1]
        i += 1
    return False
def nextDay(tempCurrentDayOfWeek, tempCurrentMonth, tempCurrentDay, tempCurrentYear):
# generates new day of the week
    i = 0
    while i < 7:
        if tempCurrentDayOfWeek == day[-1]:
            newDayOfWeek = day[0]
            break
        if tempCurrentDayOfWeek == day[i]:
            newDayOfWeek = day[i+1]
            break
        i += 1

# generates new month and day
    if checkLeap(tempCurrentYear):
        if tempCurrentDay == monthL[tempCurrentMonth]:
            if tempCurrentMonth == 12:
                   newMonth = 1
                   newDay = 1
                   newYear = tempCurrentYear + 1
            else:
                newMonth = tempCurrentMonth + 1
                newDay = 1
                newYear = tempCurrentYear
        else:
            newMonth = tempCurrentMonth
            newDay = tempCurrentDay + 1
            newYear = tempCurrentYear
 #       print "The year %s is a leap year." % newYear
    else:
        if tempCurrentDay == month[tempCurrentMonth]:
            if tempCurrentMonth == 12:
                newMonth = 1
                newDay = 1
                newYear = tempCurrentYear + 1
            else:
                newMonth = tempCurrentMonth + 1
                newDay = 1
                newYear = tempCurrentYear
        else:
            newMonth = tempCurrentMonth
            newDay = tempCurrentDay + 1
            newYear = tempCurrentYear
    
    return (newDayOfWeek,newMonth,newDay,newYear)

        
def checkLeap(tempCurrentYear):
    if tempCurrentYear % 400 == 0:
        return True
    elif tempCurrentYear % 100 == 0:
        return False
    elif tempCurrentYear % 4 == 0:
        return True
    else:
        return False

# month index = month(0 = Jan)
# month index value = totals days of the month
month = (None,31,28,31,30,31,30,31,31,30,31,30,31)
# leap year
monthL = (None,31,29,31,30,31,30,31,31,30,31,30,31)
#
day = ('Mon','Tues','Wed','Thur','Fri','Sat','Sun')
year = 1901

# beginning date
# format: day of the week, month, day, year
current = (day[1],1,1,1901)

# end date, stops right when it reaches this date
# format: month, day, year
end = (1,1,2001)
sundays = 0

while 1:
#    print "Current date:", current
    if current[1] == end[0] and current[2] == end[1] and current[3] == end[2]:
        break
    if current[2] == 1:
        if current[0] == day[-1]:
            sundays += 1
#    print "Number of Sundays found: %s" % sundays
    current = nextDay(current[0],current[1],current[2],current[3])
print sundays
