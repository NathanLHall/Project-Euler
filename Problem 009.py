# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:25:40 2018

@author: NathanLHall
"""
n = 2
m = 1

def A(m,n):
    return n**2 - m**2

def B(m,n):
    return 2 * m * n

def C(m,n):
    return n**2 + m**2

a = A(m,n)
b = B(m,n)
c = C(m,n)

while a + b + c != 1000:
    if a + b + c < 1000:
        n += 1
        a = A(m,n)
        b = B(m,n)
        c = C(m,n)
    elif a + b + c > 1000:
        m += 1
        n = m + 1
        a = A(m,n)
        b = B(m,n)
        c = C(m,n)

print(a*b*c)