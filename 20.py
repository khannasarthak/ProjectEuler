# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 15:51:37 2015

@author: Sarthak Khanna
"""

import math
k = 0
n = math.factorial(100)
while n >0:
    d = n%10
    k = k + d
    n = n/10
    
print k
    