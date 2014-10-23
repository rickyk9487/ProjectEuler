# -*- coding: utf-8 -*-
"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Answer: 837799, length 525, runs in ~20s
Ricky Kwok, rickyk9487@gmail.com, 2014-10-23
"""
import time
#import collections

class Collatz(object):
            
    def __init__(self,  N):
        """ Populates a dictionary of easy to calculate Collatz numbers. """
        collatz_dict = {}
        for i in range(1,22):
            # computes powers of 2 up to 1mil as keys and their lengths as values
            collatz_dict[2**(i-1)] = i
        self.dict = collatz_dict
        self.N = N
        self.max_int, self.max_chain = max(self.dict.items(), key = lambda t: t[1])
        return
        
    def collatz_length(self, n, count):
        """ If n is in the dictionary of known collatz numbers, returns value. 
            If not, recursively iterates n and keeps track of counts. """
        if n in self.dict:
            return count + self.dict[n]
        elif n % 2 == 0:
            return self.collatz_length(n/2, count+1)
        else:
            return self.collatz_length(3*n+1, count+1)
        
    def populate_dict(self):
        """ Computes Collatz chain lengths in decreasing numbers starting with
            N-1. Keeps track of the maximum by always comparing to the current
            maximum and updates if a new max is found. """
        for k in range(self.N-1,0,-1):
            self.dict[k] = self.collatz_length(k, 0)
            if self.dict[k] > self.max_chain:
                self.max_int, self.max_chain = k, self.dict[k]
        return self.dict
    
    def longest(self):
        return self.max_int, self.max_chain
    
def main():
    N = 10**6
    collatz = Collatz(N)
    collatz.populate_dict()
    max_collatz = collatz.longest()
    answer = """For numbers below one million, the starting number %d has the 
longest Collatz chain of %d.""" %(max_collatz)
    return answer

if __name__ == "__main__":
    start = time.time()
    print main()
    end = time.time()
    print end-start