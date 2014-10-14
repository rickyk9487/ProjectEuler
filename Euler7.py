# -*- coding: utf-8 -*-
"""
10001st prime
Problem 7
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

Remark: By the prime number theorem, the solution x, should solve

10001 = x/log(x), log = natural logarithm.

Solving this transcendental equation by hand gives x ~ 116684.

Answer: 104743
Ricky Kwok, rickyk9487@gmail.com, 2014-10-14
"""

import numpy as np

def is_prime(k, prime_list, sieve_ind):
    """ Uses Sieve of Eratosthenes to check if a number k is prime. """
    sieve_num = np.ceil(np.sqrt(k))
    for i in range(sieve_ind, len(prime_list)):
        # finds index of sieve number, largest integer greater than sqrt of k
        if prime_list[i] < sieve_num:
            pass
        else:
            sieve_ind = i
            break
    
    sieve_primes = prime_list[0:sieve_ind+1]
    list_k = k * np.ones(len(sieve_primes))
    remainders = list_k % sieve_primes
    if 0 not in remainders:
        prime_list.append(k)
    return prime_list, sieve_ind

def main():
    N = 10001
    prime_list = [2,3]
    k = prime_list[-1] + 2
    sieve_ind = 1
    while len(prime_list) < N:
        prime_list, sieve_ind = is_prime(k, prime_list, sieve_ind)
        k += 2
    print prime_list[-1]
    
if __name__ == "__main__":
    main()