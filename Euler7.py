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
Ricky Kwok, rickyk9487@gmail.com, 2014-10-15
"""

import numpy as np
import time

start = time.time()
N, num, len_prime_list, sieve_ind = 10001, 5, 2, 1
prime_list = np.zeros(N)
sieve_primes = np.zeros(500) 
# sieve_primes keeps a list of primes up to square root N
# 500 is much larger than sqrt(116684) ~ 342
prime_list[0:2] = 2,3
sieve_primes[0:2] = prime_list[0:2]
# suffices to check primes up to the square root of number k

while len_prime_list < N:
    """ Iterates through odd integers checking for primality 
        using Sieve of Eratosthenes. """
    sieve_num = np.ceil(np.sqrt(num))
    # smallest integer larger than the square root of num
    for i in range(sieve_ind, len_prime_list):
        # finds index of the prime number larger than sieve_num
        if prime_list[i] >= sieve_num:
            sieve_ind = i
            break
            
    if prime_list[sieve_ind] > sieve_primes[-1]: 
        # adds to sieve primes if sieve_num produces a new prime
        sieve_primes[sieve_ind] = prime_list[sieve_ind]
    
    found_prime = True 
    # flag for new prime
    for p in sieve_primes[0:sieve_ind+1]:
        # tests if num is divisible by any primes up to sieve_num
        if num % p == 0:
            found_prime = False
            break

    if found_prime:
        """ no flag means num does not divide any of sieve primes
            iter means it reached all sieve primes."""
        prime_list[len_prime_list] = num
        len_prime_list += 1

    num += 2
    
print int(prime_list[-1])
end = time.time()
print end - start