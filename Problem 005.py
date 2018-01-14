# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:37:28 2018

@author: NathanLHall
"""

limit = 20
minFactors = []

def factor(number):
    factors = []
    m = 2
    while number > 1:
        while number % m == 0:
            factors.append(m)
            number //= m
        m = m + 1
    return factors

def main(number):
    for i in range(2,number + 1):
        factors = factor(i)
        for j in range(len(factors)):
            while factors.count(factors[j]) > minFactors.count(factors[j]):
                minFactors.append(factors[j])
    minMultiple = 1
    for k in range(len(minFactors)):
        minMultiple *= minFactors[k]
    return minMultiple

minMultiple = main(limit)
print(minMultiple)