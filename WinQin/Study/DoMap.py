# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:14:58 2016

@author: WinQin
"""

def fun(x):
    return x**2


l=list(range(1,10))
p=map(fun,l)


for i in p:
    print(i)
    