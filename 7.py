# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 23:19:57 2014

@author: Sarthak Khanna
"""
x=[]
def isprime(num):
    if num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
            
c = 0


for i in range(1,1000000):
    if isprime(i) == True:
        x.append(i)
        c=c+1
        print c
        if c>10001:
            break
        

print x[len(x)-1]
    

    


