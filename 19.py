# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 15:56:58 2015

@author: Sarthak Khanna
"""

import calendar
import time
start = time.time()
k = 0
for i in xrange(1901,2001):
    for j in xrange(1,13):
        
        if calendar.weekday(i,j,1)==6:
            print i,j
            k=k+1


elapsed = time.time()-start
print k,elapsed
            