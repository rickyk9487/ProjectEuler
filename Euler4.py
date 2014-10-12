# -*- coding: utf-8 -*-
"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers 
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
Answer: 580085
Ricky Kwok, rickyk9487@gmail.com, 2014-10-12
"""

j, flag = 999, True
while j >= 100 and flag:
    # indexes j from 999 down to 100
    k = j
    
    while k >= 100 and flag:
        # product of k and j from j until k is 100
        string = str(j*k)
        
        if string == string[::-1]:
            # python way of checking the product is a palindrome
            print j*k, j, k
            flag = False
            # stopping criterion to break the while loops
            
        k -= 1
        
    j -= 1
