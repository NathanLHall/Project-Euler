# -*- coding: utf-8 -*-
"""
@author: NathanLHall
"""

# https://projecteuler.net/problem=14

Collatz = 0
maxCount = 0
collatz = 1

def even(n):
    return n/2

def odd(n):
    return 3 * n + 1

million = 1000000
while collatz < million:
    count = 1
    n = collatz
    while n != 1:
        if n % 2 == 0:
            count += 1
            n = even(n)
        elif n % 2 == 1:
            n = odd(n)
            count += 1
    if maxCount < count:
        maxCount = count
        Collatz = collatz
    collatz += 1

print("Number:", Collatz)
print("Count:", count)
