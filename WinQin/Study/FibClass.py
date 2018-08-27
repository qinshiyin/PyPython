# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:18:54 2016

@author: WinQin
"""

class FibClass(object):

    # ----------------------------------------------------------------------
    def  __init__(self,length):
        """"""
        self.__a,self.__b=0,1
        if length<0:
            self.__length=0
        else:
            self.__length=length
    
    # ----------------------------------------------------------------------
    def  __len__(self):
        """"""
        return self.__length
        
    # ----------------------------------------------------------------------
    def  __iter__(self):
        """"""
        return self
    
    # ----------------------------------------------------------------------
    def  __next__(self):
        """"""
        self.__a,self.__b=self.__b,self.__a+self.__b
        if self.__a>10000:
            raise StopIteration()
        return self.__a
    
    # ----------------------------------------------------------------------
    def  __getitem__(self,n):
        """"""
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            if stop is None:
                stop=self.__len__()
            a, b = 0, 1
            cnt=0
            L = []
            for x in range(stop):
                a, b = b, a + b
                if x >= start:
                    L.append(a)
                cnt+=1
            return L
        
#Test
if __name__=='__main__':
    Fib=FibClass(200)
    for n in Fib:
        print(n)
    
    for n in range(200):
        print(Fib[n])
    
    print(Fib[:])





















