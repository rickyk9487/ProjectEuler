# -*- coding: utf-8 -*-
"""
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then 
a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Answer: 31626
Ricky Kwok, rickyk9487@gmail.com, 2014-12-30
"""
import time
import numpy as np

def getSumDivisors(n):
    sumDiv = 1
    sqrtn = int(np.ceil(np.sqrt(n)))
    for k in xrange(2, sqrtn):
        if n % k == 0:
            sumDiv += k + n/k
            
    return sumDiv
    
def findAmicablePair(N):
    amicDict = {}
    for a in xrange(N):
        b = getSumDivisors(a)
        amic = getSumDivisors(b)
        if a == amic and a!= b:
            amicDict[a] = b

    return amicDict

def main():
    print "Sum of Amicable numbers under 10000 is", sum(findAmicablePair(10000).keys())

if __name__ == "__main__":
    start = time.time()
    main()
    elapsed = time.time() - start
    print "Found in %.2f seconds" %elapsed