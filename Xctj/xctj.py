#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import datetime as dt

def get_ls_list(path):
    ls_list = []
    ls = os.popen('hadoop fs -ls ' + path).readlines()
    temp = {}
    for lss in ls[1:]:
        l = lss.split(' ')[-3:]
        ct_time = dt.datetime.strptime(l[0] + ' ' + l[1],'%Y-%m-%d %H:%M')
        tb_name = l[3].split('\n')[0].split('/')[-1]
        temp['ct_time'] = ct_time
        temp['tb_name'] = tb_name
        ls_list.append(temp.copy())
        temp.clear()
    return ls_list

def read_white_list(path):
    with open(path, 'r') as f:
        return f.readlines()

