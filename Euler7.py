# -*- coding: utf-8 -*-
"""
10001st prime
Problem 7
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

Remark: By the prime number theorem, the solution x, should approximately solve

10001 = x/log(x), log = natural logarithm.

Solving this transcendental equation by hand gives x ~ 116684. The code below
uses the Sieve of Eratosthenes to check if a number is prime. 

Answer: 104743
Ricky Kwok, rickyk9487@gmail.com, 2014-10-20
"""

def sieve(n, limit=125000):
    if limit % 2 != 0: limit += 1
    primes = [True] * limit
    primes[0:2] = [None] * 2
    count = 0 # how many primes have we found?
    for ind,val in enumerate(primes):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes[ind*2::ind] = [False] * (((limit - 1)/ind) - 1)
            count += 1
        if count == n: return ind
    return False
 
prime = sieve(10001)
 
print prime