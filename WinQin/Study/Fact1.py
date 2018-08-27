# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 17:12:26 2016

@author: WinQin
"""

'''
def fact1(n):
    def f(n,p):
        if n==1:
            return p
        return f(n-1,n*p)
    return f(n,1)
'''

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
    
#Test
if __name__=='__main__':
    print(fact(1000))