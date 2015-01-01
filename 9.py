# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 00:04:44 2014

@author: Sarthak Khanna
"""
import math
print "hello"

k = 1
for m in range(50):
    for n in range(50):
        a = k*(m**2-n**2)
        b=k*2*m*n
        c= k*(m**2+n**2)
        if a+b+c == 1000:
            print a,b,c
            print a*b*c


        
        