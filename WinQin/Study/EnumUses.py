# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:15:18 2016

@author: WinQin
"""

from enum import Enum

weekday=Enum('WeekDay',('Mon','Tue','Wed','Thu','Fri','Sat','Sun'))

for key,value in weekday.__members__.items():
    print(key,'=>',value.value)
