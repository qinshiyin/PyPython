# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 14:41:51 2016

@author: WinQin
"""
__author__='QSY'

import sys

def test():
    args=sys.argv
    print(args)
    if len(args)==1:
        print('Hello World!')
    elif len(args)==2:
        print('Hello %s!'%args[0])
    else:
        print('Too many arguments')

#Test
if __name__=='__main__':
    test()