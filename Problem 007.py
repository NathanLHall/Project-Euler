# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 11:19:07 2018

@author: NathanLHall
"""

# Given an integer > 1, this will return the given integer if it is prime.
# If it is not prime, it will return None.
def checkDivisibility(number, primes):
    for p in primes:
        if number % p == 0:
            return None
    return number

# Given a positive integer, the index = n, will find the nth prime number.
def nth_prime(index):
    primes = [2,3]
    candidate = 5
    while len(primes) < index:
        modCandidate = checkDivisibility(candidate, primes)
        if type(modCandidate) == int:
            primes.append(candidate)
        candidate += 2
    return primes

primes = nth_prime(10001)
print(primes[-1])