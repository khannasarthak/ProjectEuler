# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 16:59:10 2015

@author: Sarthak Khanna
"""

import time
start = time.time()
x = []
def fact(n):
    n=int(n)
    global x
    k = 0
    t=0
    global f
    for i in range(1,int(n)):
        if int(n)%i==0:
            #print i
            k=k+i
    for j in range(1,k):
        if int(k)%j==0:
            #print j
            t=t+j
    print (n,k)
    if(n==t and n!=k):
        x.append(n)
        x.append(k)
        
        



for o in range(1,10000):
    fact(o)
    print (x)
e = start-time.time()
print (x,e)
  
          
        
            
                
                

