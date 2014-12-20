# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 23:08:32 2014

@author: Sarthak Khanna
"""

def fib2(n): 
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
    
k = fib2(4000000)
print k 
c=0
for i in range(len(k)):
    if k[i]%2==0:
        c=c+k[i]
        
print c