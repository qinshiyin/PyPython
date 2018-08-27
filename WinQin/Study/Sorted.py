# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 16:17:11 2016

@author: WinQin
"""

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()
    
print(sorted(L,key=by_name))