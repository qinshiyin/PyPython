# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:57:27 2016

@author: WinQin
"""

from functools import reduce

def prod(L):
    def fn(x,y):
        return x*y
    return int(reduce(fn,L))


#Test
if __name__=='__main__':
    L=list(range(1,11))
    print(prod(L))
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))