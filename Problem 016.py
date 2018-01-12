# -*- coding: utf-8 -*-
"""
@author: NathanLHall
"""

# https://projecteuler.net/problem=16

power = 2 ** 1000
power = str(power)
digits = []

for i in range(len(power)):
    digits.append(power[i])

result = 0
for i in range(len(digits)):
    result += int(digits[i])

print(result)
