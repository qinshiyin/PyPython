# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:07:16 2016

@author: WinQin
"""

from functools import reduce

def str2float(s):
    def char2num(s):
        d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return d[s]
    def fn(x,y):
        return x*10+y
    s1,s2=s.split('.')
    return reduce(fn,map(char2num,s1))+reduce(fn,map(char2num,s2))/10**len(s2)
    
#Test
if __name__=='__main__':
    print('str2float(\'123.456\') =', str2float('123.456'))