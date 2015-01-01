# -*- coding: utf-8 -*-
"""
Created on Thu Jan 01 21:40:25 2015

@author: Sarthak Khanna
"""
import math   
p=2
n = 2000000
k = math.sqrt(n)

k = math.ceil(k)
o = 0
while p < n:
        for i in range(2, p):
                if p%i == 0:
                        p=p+1 
        print p
        o=o+p
        p=p+1
print "Done"
print o
    