# -*- coding: utf-8 -*-
"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Math solution:
In an N-by-N grid, moves consist of D = down and R = right. Realize that there
must be a total of 2N moves to go from the top left corner to the bottom right.
There must be N down and N right moves. We can describe each path uniquely by
a combination of D's and R's each appearing N times in a 2N-gram. The answer is
simply the number of such 2N-grams. For N = 2, the possible combinations are

RRDD, RDRD, RDDR, DDRR, DRDR, DRRD.

These are uniquely determined by just considering the locations of D's in a 
4-gram. The total number is 4C2 (4 choose 2). For general N, the same argument
holds and the answer is 2N C 2 (2N choose N).

Answer: 137846528820
Ricky Kwok, rickyk9487@gmail.com, 2014-10-24
"""

import scipy.misc

print scipy.misc.comb(40,20)