# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:10:04 2016

@author: WinQin
"""

import math

def quadratic(a,b,c):
    if a==0:
        return -c/b
    delta=b*b-4*a*c
    if delta<0:
        return None
    if delta==0:
        return -b/(2*a)
    if delta>0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return (x1,x2)
    
#Test
if __name__=='__main__':
    print(quadratic(2, 3, 1))
    print(quadratic(1, 3, -4))