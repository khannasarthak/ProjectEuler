# -*- coding: utf-8 -*-
"""
Created on Sun Jan 04 03:04:16 2015

@author: Sarthak Khanna
"""

import time
 
def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]
 
start = time.time()
n = route_num(20)
elapsed = (time.time() - start)
print "%s found in %s seconds" % (n,elapsed)



""" Not My solution, couldn't do it without recursion,
need to study maths
"""