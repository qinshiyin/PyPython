#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import time
import xml.dom.minidom as mdom
import datetime


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


# 执行Hadoop命令移动文件到HDFS上
def move_to_hdfs(lpath, hpath):
    """
    :执行Hadoop命令移动文件到HDFS上
    :param lpath: 要移动的文件路径
    :param hpath: 目标文件路径
    :return: None
    """
    cmd = 'hadoop fs -copyFromLocal ' + lpath + ' ' + hpath
    os.popen(cmd)
    return None


# 给Hive表后台添加分区
def add_tab_part(hpath):
    """
    :给Hive表后台添加分区
    :param hpath: Hive表要添加的存储分区路径
    :return: None
    """
    cmd = 'hadoop fs -mkdir ' + hpath
    os.popen(cmd)
    return None


# 执行SQL语句，关联表与后台存储文件之间的关系
def load_tab_part(login, db_name, tb_name, partid, filehpath):
    """
    :执行SQL语句，关联表与后台存储文件之间的关系
    :param login: 认证文件路径
    :param db_name: 数据库名称
    :param tb_name: 表名称
    :param partid: 分区路径
    :param filehpath: 文件路径
    :return: None
    """
    os.popen('source ' + login)
    sql = r'beeline -e "use ' + db_name + r'; alter table ' + db_name + '.' + tb_name \
          + ' add partition(' + partid + ') location \'' + filehpath + '\';\"'
    # print(sql)
    os.popen(sql)
    return None


def run():
    """
    :执行
    :return: None
    """
    user_list = ['jc_sjwj', 'jc_dwfu', 'jc_bdcsj', 'jc_bdxctj', 'jc_mro','jc_bdcqs']

    while True:
        collect_time = time.strftime('%Y%m%d%H%M%S')
        to_hive_time = time.strftime('%H%M')
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        yesterday_time = yesterday.strftime('%Y%m%d')
        yesterday_year = yesterday.strftime('%Y')
        yesterday_month = yesterday.strftime('%m')
        yesterday_day = yesterday.strftime('%d')
        path = '/app/bdcqs/huangwei/yarnapplicationlog/yarn_' + time.strftime('%Y%m%d') + '.txt'

        save_to_file(get_table('yarn application -list', user_list, collect_time), path, '|')

        path = '/app/bdcqs/huangwei/yarnmaplistlog/mapred_' + time.strftime('%Y%m%d') + '.txt'
        save_to_file(get_table('mapred job -list', user_list, collect_time), path, '|')
        print(to_hive_time+'--'+yesterday_time+'--'+yesterday_year+
              '--'+yesterday_month+'--'+yesterday_day)
        if to_hive_time == '1520':
            add_tab_part('/jc_bdcqs/bdcqs_hive_db/d_yarn_application_list/p_day=' + yesterday_time)
            move_to_hdfs('/app/bdcqs/huangwei/yarnapplicationlog/yarn_' + yesterday_time + '.txt',
                         '/jc_bdcqs/bdcqs_hive_db/d_yarn_application_list/p_day='+yesterday_time)
            load_tab_part('bdcqs_hive_db','d_yarn_application_list', yesterday_time,
                          '/jc_bdcqs/bdcqs_hive_db/d_yarn_application_list/p_day=' + yesterday_time)

            add_tab_part('/jc_bdcqs/bdcqs_hive_db/d_yarn_mapred_job_list/p_day=' + yesterday_time)
            move_to_hdfs('/app/bdcqs/huangwei/yarnmaplistlog/mapred_' + yesterday_time + '.txt',
                         '/jc_bdcqs/bdcqs_hive_db/d_yarn_mapred_job_list/p_day=' + yesterday_time)

            load_tab_part('bdcqs_hive_db', 'd_yarn_mapred_job_list', yesterday_time,
                          '/jc_bdcqs/bdcqs_hive_db/d_yarn_mapred_job_list/p_day=' + yesterday_time)

        time.sleep(60)
    return None


def get_job_id(filehpath,user_list,collect_time):
    table = [0, ]
    contents =''
    job_id =''
    dir_job_id=''
    re_file = os.open(filehpath).readlines()
    for line in re_file:
        dir_file = line.split('_')[2]
        job_id =line.split('_')[0]+'_'+line.split('_')[1]+'_'+line.split('_')[2]
        dir_job_id=job_id+','+dir_file+','+collect_time
        print(contents+'contents'+dir_file+'dir_file'+job_id+'job_id')
        table[0] = table[0] + 1
        table.append(dir_job_id)
    return table


def get_comp_xmlfile(jobid, year, month, day):
    cmd = 'hadoop fs -'


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


if __name__ == '__main__':
        run()




