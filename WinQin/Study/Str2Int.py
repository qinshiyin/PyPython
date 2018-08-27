# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:29:27 2016

@author: WinQin
"""

from functools import reduce

def str2int(string):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return d[s]
    return reduce(fn,map(char2num,string))

#Test
if __name__=='__main__':
    print(str2int('12109284735268237545'))