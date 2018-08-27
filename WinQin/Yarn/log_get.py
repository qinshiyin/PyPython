#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import time


# 获取命令执行结果，将结果存储为一维数组的表，其中第一个数是记录条数
def get_table(cmd, user_list, collect_time):
    """
    :获取命令执行结果，将结果存储为一维数组的表，其中第一个数是记录条数
    :param cmd: 要执行的命令
    :param user_list: 要采集的租户列表
    :param collect_time: 采集开始时间
    :return: 采集结果，一维数组存储的表，第一个值是记录条数
    """
    table = [0, ]
    re_cmd = os.popen(cmd).readlines()
    for line in re_cmd[2:]:
        ll = line.replace(' ', '').replace('\n', '').split('\t')
        if len(ll) == 9 or len(ll) == 13:
            if ll[3] in user_list or ll[4] in user_list:
                table[0] = table[0] + 1
                for items in ll:
                    table.append(items)
                table.append(collect_time)
    return table


# 将table存储到path上的文件，每条记录以gap间隔
def save_to_file(table, path, gap='|'):
    """
    :将table存储到path上的文件，每条记录以gap间隔
    :param table: 要保存的表
    :param path: 存储文件路径
    :param gap: 每条记录之间的分隔符
    :return: None
    """
    nums = table[0]
    cols = (len(table) - 1) / nums
    with open(path, 'a') as f:
        for n in range(nums):
            for c in range(cols):
                f.write(table[1 + n * cols + c])
                if c < cols - 1:
                    f.write(gap)
            f.write('\r\n')
    return None


def run():
    """
    :执行
    :return: None
    """
    user_list = ['jc_sjwj', 'jc_dwfu', 'jc_bdcsj', 'jc_bdxctj', 'jc_mro', 'jc_bdcqs']
    collect_time = time.strftime('%Y%m%d%H%M%S')
    par_path = os.getcwd() + '/' + time.strftime('%Y%m%d') + '/'
    if not os.path.exists(par_path):
        os.popen('mkdir ' + par_path)
    path = par_path + 'yarn_' + time.strftime('%Y%m%d') + '.txt'
    save_to_file(get_table('yarn application -list', user_list, collect_time), path, '|')
    path = par_path + 'mapred_' + time.strftime('%Y%m%d') + '.txt'
    save_to_file(get_table('mapred job -list', user_list, collect_time), path, '|')
    return None


# Run
if __name__ == '__main__':
    run()
