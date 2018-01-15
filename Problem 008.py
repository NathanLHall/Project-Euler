# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:06:57 2018

@author: NathanLHall
"""

file = open("Problem 008.txt", 'r')
contents = file.readlines()
file.close()

number = []
maxProduct = 1

for line in contents:
    for i in line:
        if i != '\n':
            number.append(int(i))

index = 0

for index in range(len(number) - 12):
    searchSpace = []
    for i in range(0,13):
        searchSpace.append(number[index + i])
    if 0 in searchSpace:
        # --- CODE LATER ---
        # If 0 is one of the digits present, skip ahead to grab the first 13 digits
        # after it.  If 0 shows up in the middle, locate it and skip ahead to grab
        # the first 13 digits after that.
        continue
    product = 1
    for k in range(len(searchSpace)):
        product *= searchSpace[k]
    if product > maxProduct:
        maxProduct = product

print(maxProduct)    