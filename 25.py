# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:04:06 2015

@author: Sarthak Khanna
"""
import time
start = time.time()

def fib(n):
    a = 1
    b = 0
    while n > 1:
        a, b = a+b, a
        n = n - 1
    return a
 

  
for i in range(1000,7000):    
    n = fib(i)
    n = str(n)
    
    if len(n)==1000:        
        print (i)
        break
        
end = time.time()-start
print (end)        
    


    