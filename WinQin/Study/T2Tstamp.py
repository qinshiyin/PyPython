# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:36:51 2016

@author: WinQin
"""

import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str, tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz=re.match('([u|U][t|T][c|C])(\+|\-)(\d{1,2})(\:00)',tz_str)
    print(tz.groups())
    delta=0
    if tz.group(2)=='+':
        delta=int(tz.group(3))
    else:
        delta=-int(tz.group(3))
    dt_tz=dt.replace(tzinfo=timezone(timedelta(hours=delta)))
    print(dt_tz.timestamp(),delta)
    return dt_tz.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
#assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
#assert t2 == 1433121030.0, t2

print('Pass')