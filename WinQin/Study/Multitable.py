# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:00:53 2016

@author: WinQin
"""

import functools

def log(text):
    def dacorator(func):
        @functools.wraps(func)
        def wraper(*args,**kw):
            print(text,'乘法表')
            return func(*args,**kw)
        return wraper
    return dacorator

@log('print')
def multitable(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(j,'×',i,'=',i*j,end='\t')
        print()
    return None


#Test
if __name__=='__main__':
    multitable(9)
    print(multitable.__name__)