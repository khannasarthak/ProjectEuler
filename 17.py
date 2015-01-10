# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 14:44:05 2015

@author: Sarthak Khanna
"""

S = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
D = [0,3,6,6,5,5,5,7,6,6]
H = 7
T = 8
total = 0
for i in range(1,1001):
    o = i%10
    t = (i%100-o)/10
    h = (i%1000-(t*10+o))/100
    if h!=0:
        total = total + S[h] + H
        if o !=0 or t != 0:
            total = total + 3
    if t == 0 or t == 1:
        total = total + S[t*10 + o]
    else:
        total = total + D[t] + S[o]

total = total + T + 3 # 'one Thousand'
print total
    
        