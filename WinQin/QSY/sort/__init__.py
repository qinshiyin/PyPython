#!usr/bin/env python
# -*- coding:utf-8 -*-

# Lib import
import numpy as np

def insert(L):
    '''插入法排序'''
    shape=L.shape
    if len(shape)==0:
        count=0
    else:
        count=1
    for i in shape:
        count*=i
    for i in range(0,count):


    return L

def shell(L):
    pass

def bubble(L):
    pass


#Test
L=np.random.random((3,4))
print(L)