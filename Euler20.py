# -*- coding: utf-8 -*-
"""
Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Answer: 648
Ricky Kwok, rickyk9487@gmail.com, 2014-10-26
"""
import time
import math

def sum_digits(n):
    sum = 0
    while n > 1:
        sum += n % 10
        n = n/10
    return sum
    
def main():
    n = math.factorial(100)
    return sum_digits(n)

start = time.time()    
print main()
end = time.time()
print end-start