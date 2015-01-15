# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 17:17:39 2015

@author: Sarthak Khanna
"""
import time
import itertools
start = time.time()
x= (sorted(list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))))
end = time.time()-start
print (x[999999],end)