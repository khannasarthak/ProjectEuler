# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 23:52:32 2014

@author: Sarthak Khanna
"""

k = 0

for i in range(1000):
    if i%3==0 or i%5==0:
        k = k+i
        
print k