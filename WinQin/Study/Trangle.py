# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:43:33 2016

@author: WinQin
"""

def Trangle(N):
    a,b=0,[1]
    while a<N:
        yield b
        b=[1]+[b[i]+b[i+1] for i in range(len(b)-1)]+[1]
        a=a+1


#Test
if __name__=='__main__':
    a=Trangle(15)
    for i in a:
        print(i)
        