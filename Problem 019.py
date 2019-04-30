# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 07:21:16 2018

@author: NathanLHall
"""

startYear = 1901
endYear = 2000

January = 6
February = 2
March = 2
April = 5
May = 0
June = 3
July = 5
August = 1
September = 4
October = 6
November = 2
December = 4

months = [January, February, March, April, May, June, July, August, September, October,\
          November, December]

monthString = ["January", "February", "March", "April", "May", "June", "July", "August",\
               "September", "October", "November", "December"]

def getTimespan(startYear, endYear):
    timespan = startYear
    for i in range(endYear - startYear + 1):
        timespan.append(startYear + i)
    return timespan

def getCenturyCode(year):
    year %= 400
    if (year // 100) % 4 == 0:
        centuryCode = 0
    elif (year // 100) % 4 == 1:
        centuryCode = 5
    elif (year // 100) % 4 == 2:
        centuryCode = 3
    elif (year // 100) % 4 == 3:
        centuryCode = 1
    return centuryCode

def getYearCode(year):
    year %= 400
    leapCode = ((year % 100) // 4) % 7
    yearCode = (year % 4) + leapCode
    return yearCode

def main(startYear, endYear):
    centuryCode = getCenturyCode(startYear)
    yearCode = getYearCode(startYear)
    result = (centuryCode + yearCode + January + 1) % 7
    print("Century Code =", centuryCode)
    print("Year Code =", yearCode)
    print("January =", January)
    return result

result = main(2000, 2001)
print(result)