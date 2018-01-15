# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:06:57 2018

@author: NathanLHall
"""

adjacencyLength = 13

file = open("Problem 008.txt", 'r')
contents = file.readlines()
file.close()

number = []
maxProduct = 1

for line in contents:
    for i in line:
        if i != '\n':
            number.append(int(i))

for i in range(len(number) - (adjacencyLength - 1)):
    searchSpace = []
    product = 1
    for j in range(adjacencyLength):
        searchSpace.append(number[i + j])
    if 0 in searchSpace:
        continue
    for k in range(len(searchSpace)):
        product *= searchSpace[k]
    if product > maxProduct:
        maxProduct = product

print(maxProduct)