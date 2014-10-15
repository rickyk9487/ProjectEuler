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
Ricky Kwok, rickyk9487@gmail.com, 2014-10-14
"""

import numpy as np

N, num, len_prime_list, sieve_ind = 10001, 5, 2, 1
prime_list = [2,3]
# suffices to check primes up to the square root of number k
sieve_primes = prime_list[0:sieve_ind+1]

while len_prime_list < N:
    sieve_num = np.ceil(np.sqrt(num))
    for i in range(sieve_ind, len(prime_list)):
        # finds index of sieve number, largest integer greater than sqrt of k
        if prime_list[i] >= sieve_num:
            sieve_ind = i
            break
            
    if prime_list[sieve_ind] not in sieve_primes: 
        # adds to sieve primes if sieve_num includes a new prime
        sieve_primes.append(prime_list[sieve_ind])
        
    list_num = num * np.ones(len(sieve_primes)) # checks divisibility by vector
    remainders = list_num % sieve_primes        # of primes up to sieve_num.
    
    if 0 not in remainders:                    # new prime condition
        prime_list.append(num)
        len_prime_list += 1
        
    num += 2
print prime_list[-1]