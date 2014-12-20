# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 22:27:50 2014

@author: Sarthak Khanna
"""
x=[]
for i in range(900,999):
    for j in range(800,999):
        if str((i*j))==str(i*j)[::-1]:
            x.append(i*j)
            
print max(x)