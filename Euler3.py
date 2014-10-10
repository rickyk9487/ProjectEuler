""" Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
Answer: 6857
"""
n, i, prime_factors = 600851475143, 3, []
# know n is not even, so start at 3 to see if it's a factor
while n != 1:
    if n % i == 0:
        prime_factors.append(i)
        # keep track of all prime factors
        n = n/i
    else:
        # increment factors through all odd numbers
        i += 2
        
print prime_factors[-1] 
# only print the last prime factor