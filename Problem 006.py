# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 11:05:46 2018

@author: NathanLHall
"""

limit = 100

def sum_of_squares(number):
    total = 0
    for i in range(1, number + 1):
        square = i ** 2
        total += square
    return total

def square_of_sums(number):
    total = 0
    for i in range(1, number + 1):
        total += i
    total = total ** 2
    return total

def main(number):
    sumSquares = sum_of_squares(number)
    squareSums = square_of_sums(number)
    difference = squareSums - sumSquares
    return difference

print(main(limit))