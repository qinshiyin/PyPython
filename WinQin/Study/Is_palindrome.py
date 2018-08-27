# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 16:01:02 2016

@author: WinQin
"""

def is_palindrome(n):
    s=str(n)
    return s==s[::-1]

output = filter(is_palindrome, range(10000,20000))
print(list(output))