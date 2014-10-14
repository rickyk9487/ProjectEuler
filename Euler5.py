# -*- coding: utf-8 -*-
"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

Math solution:
The idea is to prime-factorize all numbers from 1 through 20.
By the fundamental theorem of arithmetic, the solution is uniquely expressed
as a product of prime powers. Collect the maximum of each prime power to be 
assured that the product is divisible by the smaller prime powers. For example, 
the highest prime powerof two occurs in 16 = 2^4. The answer should be divisible
by 16. 

20! 
= 1*2*3*4*5*6*7*8*9*10*
  *11*12*13*14*15*16*17*18*19*20
= (2)(3)(2^2)(5)(2*3)(7)(2^3)(3^2)(2*5)
  *(11)(2^2 * 3)(13)(2*7)(3*5)(2^4)(17)(2*3^2)(19)(2^2 * 5)

collect maxima of each prime power among parentheses:
(2^4)(3^2)(5)(7)(11)(13)(17)(19) which computes to

Answer: 232 792 560
which is equal to 
(24)*2*3*5*7*11*13*17*19.
"""
import numpy as np

# answer must be divisible by all primes less than 21, so use that as increment
increm = 1.0*np.prod([2,3,5,7,11,13,17,19])

# array of remainders after dividing by 1:20
remainders = increm/range(1,21) % 1    
step = increm
while sum(remainders) > 0:
    step += increm
    remainders = step/range(1,21) % 1

print step