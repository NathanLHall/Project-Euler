# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 09:00:44 2018

@author: Omicron
"""

"""
To make the code simpler, I've added extra 0s around the perimeter.  This is help avoid writting
extra conditions for when trying to multiply near edges and don't have 4 terms.
"""
file = open("D:\Project Euler\Problem 011.txt", 'r')
contents = file.readlines()
file.close()

for i in range(len(contents)):
    contents[i] = contents[i].split(' ')
    for j in range(len(contents)):
        contents[i][j] = int(contents[i][j])

maxProduct = 0

for i in range(3, len(contents) - 3):
    for j in range(3, len(contents) - 3):
        product = 1
        for n in range(0, 4):
            # Product of right
            product *= contents[i][j + n]
        if product > maxProduct:
            maxProduct = product
        # Product of right/up
        product = 1
        for n in range(0, 4):
            product *= contents[i - n][j + n]
        if product > maxProduct:
            maxProduct = product
        # Product of up
        product = 1
        for n in range(0, 4):
            product *= contents[i - n][j]
        if product > maxProduct:
            maxProduct = product
        # Product of left/up
        product = 1
        for n in range(0, 4):
            product *= contents[i - n][j - n]
        if product > maxProduct:
            maxProduct = product
        # Product of left
        product = 1
        for n in range(0, 4):
            product *= contents[i][j - n]
        if product > maxProduct:
            maxProduct = product
        # Product of left down
        product = 1
        for n in range(0, 4):
            product *= contents[i + n][j - n]
        if product > maxProduct:
            maxProduct = product
        # Product of down
        product = 1
        for n in range(0, 4):
            product *= contents[i + n][j]
        if product > maxProduct:
            maxProduct = product
        # Prodcut of right/down
        product = 1
        for n in range(0, 4):
            product *= contents[i + n][j + n]
        if product > maxProduct:
            maxProduct = product

print(maxProduct)