# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:03:54 2018

@author: NathanLHall
"""

def checkDivisibility(number, primes):
    for p in primes:
        if number % p == 0:
            return None
    return number

# Given a positive integer, the index = n, will find the nth prime number.
def primes_below(index):
    primes = [2,3]
    candidate = 5
    while primes[-1] < index:
        print(candidate)
        modCandidate = checkDivisibility(candidate, primes)
        if type(modCandidate) == int:
            primes.append(candidate)
        candidate += 2
    return primes

primes = primes_below(2000000)
print(sum(primes[0:-1]))