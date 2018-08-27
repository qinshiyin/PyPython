# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:24:22 2016

@author: WinQin
"""

def primes():
    def _odd_iter():
        n=1
        while True:
            n=n+2
            yield n
        
    def _not_divisible(n):
        return lambda x:x%n>0
        
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)


#Test
if __name__=='__main__':
    for i in primes():
        if i <100:
            print(i,end=',')
        else:
            break
        