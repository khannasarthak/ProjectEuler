# -*- coding: utf-8 -*-
"""
Created on Fri Jan 02 23:34:56 2015

@author: Sarthak Khanna
"""
y=[]
x = []
for n in range(1,1000000):
    y.append(int(n))
    print n
    k=0
    while n!=1:
    
        if n%2==0:
            n = n/2
            k = k+1
                
            print n
        elif n%2==1:
            n = 3*n+1
            k = k +1
            print n
    x.append(int(k)+1)
print x
k = max(x)   
print k     
p= x.index(k)
print y[p]