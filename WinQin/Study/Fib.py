# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:31:40 2016

@author: WinQin
"""

def Fib(N):
    n,a,b=0,0,1
    while n<N:
        yield b
        #print(b)
        a,b=b,a+b
        n=n+1
    return 'Done'


#Test
if __name__=='__main__':
    a=Fib(10)
    while True:
        try:
            i=next(a)
            print(i)
        except StopIteration as e:
            print(e.value)
            break