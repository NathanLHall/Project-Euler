# -*- coding: utf-8 -*-
"""
@author: NathanLHall
"""

# https://projecteuler.net/problem=13

file = open("D:\Project Euler\Problem 013.txt", 'r')
contents = file.readlines()
file.close()

summation = 0
for i in range(0,len(contents)):
    summation += int(contents[i])

print(summation)
