# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 17:21:36 2016

@author: WinQin
"""

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)

#Test
if __name__=='__main__':
    move(4, 'A', 'B', 'C')