# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 22:10:23 2014

@author: Sarthak Khanna
"""
x=[]
import math
def isprime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        for div in range(2,int(math.sqrt(num))):
            if num % div == 0:
                return False
        return True
    
for i in xrange(1,int(math.sqrt(600851475143))):
    if isprime(i) == True:
        x.append(i)


print x

