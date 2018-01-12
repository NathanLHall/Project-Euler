# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:50:17 2018

@author: Omicron
"""

file = open("D:\Project Euler\Problem 013.txt", 'r')
contents = file.readlines()
file.close()

summation = 0
for i in range(0,len(contents)):
    summation += int(contents[i])

print(summation)