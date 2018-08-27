#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import time
import xml.dom.minidom as mdom
import datetime


def get_table(cmd, user_list, collect_time):
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


def save_to_file(table, path):
    nums = table[0]
    cols = (len(table) - 1) / nums
    with open(path, 'a') as f:
        for n in range(nums):
            for c in range(cols):
                f.write(table[1 + n * cols + c])
                if c < cols - 1:
                    f.write('|')
            f.write('\r\n')


def find_from_xml(xml_file_path):
    sql = ''
    maps = 0
    reduces = 0
    doc = mdom.parse(xml_file_path)
    root = doc.documentElement
    properties = root.getElementsByTagName('property')
    for proper in properties:
        name_node = proper.getElementsByTagName('name')
        if name_node[0].childNodes[0].nodeValue == 'hive.query.string':
            value_node = proper.getElementsByTagName('value')
            sql = value_node[0].childNodes[0].nodeValue
        if name_node[0].childNodes[0].nodeValue == 'mapreduce.job.maps':
            value_node = proper.getElementsByTagName('value')
            maps = value_node[0].childNodes[0].nodeValue
        if name_node[0].childNodes[0].nodeValue == 'mapreduce.job.reduces':
            value_node = proper.getElementsByTagName('value')
            reduces = value_node[0].childNodes[0].nodeValue

    return sql, maps, reduces


def move_to_hdfs(lpath, hpath):
    cmd = 'hadoop fs -copyFromLocal ' + lpath + ' ' + hpath
    os.popen(cmd)


def add_tab_part(hpath):
    cmd = 'hadoop fs -mkdir '+hpath
    os.popen(cmd)


def run():
    user_list = ['jc_sjwj', 'jc_dwfu', 'jc_bdcsj', 'jc_bdxctj', 'jc_mro', 'jc_bdcqs']

    while True:
        collect_time = time.strftime('%Y%m%d%H%M%S')
        to_hive_time = time.strftime('%H%M')

        path = '/app/bdcqs/huangwei/yarnapplicationlog/yarn_' + time.strftime('%Y%m%d') + '.txt'
        save_to_file(get_table('yarn application -list', user_list,collect_time), path)

        path = '/app/bdcqs/huangwei/yarnmaplistlog/mapred_' + time.strftime('%Y%m%d') + '.txt'
        save_to_file(get_table('mapred job -list', user_list, collect_time), path)

        if to_hive_time == '1035':
            print(to_hive_time)
            today = datetime.date.today()
            yesterday = today - datetime.timedelta(days=1)
            yesterday_time = yesterday.strftime('%Y%m%d')
            add_tab_part('jc_bdcqs/bdcqs_hive_db/d_yarn_application_list/p_day=' + yesterday_time)
            move_to_hdfs('/app/bdcqs/huangwei/yarnapplicationlog/yarn_' + yesterday_time + '.txt',
                         'jc_bdcqs/bdcqs_hive_db/d_yarn_application_list/p_day='+yesterday_time)

        time.sleep(60)


# Test
if __name__ == '__main__':
    run()

