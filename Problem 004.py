# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:23:12 2018

@author: NathanLHall
"""

palindrome = []

for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        product = str(product)
        if product == product[::-1]:
            palindrome.append(int(product))

print(max(palindrome))