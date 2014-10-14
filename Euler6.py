# -*- coding: utf-8 -*-
"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.

Math Solution:
Open the parentheses in a square of a sum (1+2+...+n)^2 and you get

sum_{i=1}^n i^2 + 2*sum_{j=1}^n sum_{i=1}^{j-1} j*i. # use this formula in code



We want to subtract off the first sum, so we're left with a double sum. Use
known identities for sum of squares and cubes to get 

2*sum_{j=1}^n sum_{i=1}^{j-1} j*i = 2*sum_{j=1}^n j [(j-1)j]/2
= sum_{j=1}^n j^3 - j^2 = [n(n+1)/2]^2 - [n(n+1)(2n+1)/6]
= n(n+1)/2 [n(n+1)/2 - (2n+1)/3].

For n = 100 the above formula equals 5050*4893 = 25164150

As a side ntoe, the answer is roughly (1/4)n^4 because of the sum of cubes.

Comparing to the estimate, |(1/4)100^4 - 25164150|/25164150 ~ 0.6523% error

Ricky Kwok, rickyk9487@gmail.com, 2014-10-13 
"""

sum, n = 0, 100
for k in range(1,n+1):
    for j in range(1, k):
        sum += j*k
print 2*sum
