""" Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
Answer: 486847
"""
import numpy as np

n, i = 600851475143, 3
# The given integer to factor is not even
prime_factors = []
while i <= np.sqrt(n)+1:
    if n % i == 0:
        prime_factors.append(i)
    i += 2
    
print prime_factors[-1] 