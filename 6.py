# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 23:10:54 2014

@author: Sarthak Khanna
"""
o1=0
o2=0
c=0
for i in range(101):
    o1=i*i+o1


for i in range(101):
    c = c+i
print c
o2=c*c

print o2-o1