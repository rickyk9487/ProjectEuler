"""
Power digit sum
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Answer: 1366
Ricky Kwok, rickyk9487@gmail.com
"""

digits_sum, n = 0, 2 ** 1000

while n > 0:
    digits_sum += n % 10
    n = n/10
print digits_sum