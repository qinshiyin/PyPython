# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:17:10 2016

@author: WinQin
"""

import math

def calc(*numbers):
    sum=0
    for n in numbers:
        sum+=math.pow(n,2)
    return sum

#Test
if __name__=='__main__':
    a=list((1,3,5,7))
    b=(1,3,5,7)
    print(calc(*a))
    print(calc(*b))