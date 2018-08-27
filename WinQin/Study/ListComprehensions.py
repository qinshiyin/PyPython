# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:26:42 2016

@author: WinQin
"""

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[item.lower() for item in L1 if isinstance(item,str)]
print(L2)