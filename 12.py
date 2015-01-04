# -*- coding: utf-8 -*-
"""
Created on Fri Jan 02 22:39:01 2015

@author: Sarthak Khanna
"""
from __future__ import division
import math

x = []
k = 0
for i in range(76500000,76600000):
    k = k+i
    x.append(int(k))

   
print x  
    
    
for i in x:
    z=0
    for j in range(1,int(math.ceil(math.sqrt(i)))):
        if i%j==0:
            
            z=z+1
    print z+1
    if (z+1)>500:
        print i
            