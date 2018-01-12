# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:34:51 2018

@author: NathanLHall
"""

import math

givenNumber = 600851475143
primes = []

def findFactors(number):
    divisor = 2
    factors = []
    while divisor <= math.floor(math.sqrt(number)):
        if number % divisor == 0:
            factors.append(divisor)
        divisor += 1
    return factors

# Find the factors of the given number
factorsFound = findFactors(givenNumber)

# Find if the factors themselves are prime
# The fast way of doing this is to check the factors against themselves.
for i in range(len(factorsFound)):
    count = 0
    for j in range(len(factorsFound)):
        if factorsFound[i] % factorsFound[j] == 0:
            count +=1
    if count == 1:
        primes.append(factorsFound[i])

print(max(primes))