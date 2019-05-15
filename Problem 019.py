# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 07:21:16 2018

@author: NathanLHall
"""
import datetime

def main(sartYear, endYear):
    count = 0
    # Cycle through desired years
    for year in range(startYear, endYear + 1):
        # Cycle through each month
        for j in range(1, 13):
            # If month follows a 31 day month
            dayIndex = datetime.date(year, j, 1).weekday()
            if dayIndex == 6:
                count += 1
    return count

if __name__ == "__main__":
    startYear = 1901
    endYear = 2000
    count = main(startYear, endYear)
    print(count)
