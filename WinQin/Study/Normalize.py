# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:46:51 2016

@author: WinQin
"""

def normalize(s):
    def fn(name):
        return name[0].upper()+name[1:].lower()
    return list(map(fn,s))    


#Test
if __name__=='__main__':
    L1=['adam', 'LISA', 'barT']
    L2=normalize(L1)
    print(L2)