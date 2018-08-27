# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 17:00:53 2016

@author: WinQin
"""

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)


#Test
if __name__=='__main__':
    print(fact(1000))