# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 11:05:46 2018

@author: NathanLHall
"""
import time
limit = 100

def sum_of_squares(number):
    total = (number * (number + 1) * (2 * number + 1)) // 6
    return total

def square_of_sums(number):
    total = ((1 + number) * number // 2) ** 2
    return total

def main(number):
    sumSquares = sum_of_squares(number)
    squareSums = square_of_sums(number)
    difference = squareSums - sumSquares
    return difference

start = time.time()
print(main(limit))
end = time.time()
print(end - start)