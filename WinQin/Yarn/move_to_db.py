#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import xml.dom.minidom as mdom
import datetime as dt


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
def load_tab_part(db_name, tb_name, partid, filehpath):
    """
    :执行SQL语句，关联表与后台存储文件之间的关系
    :param db_name: 数据库名称
    :param tb_name: 表名称
    :param partid: 分区路径
    :param filehpath: 文件路径
    :return: None
    """
    # os.popen('source ' + login)
    sql = r'beeline -e "use ' + db_name + r'; alter table ' + db_name + '.' + tb_name \
          + ' add partition(' + partid + ') location \'' + filehpath + '\';\"'
    # print(sql)
    os.popen(sql)
    return None


# 从XML中解析出SQL代码以及使用的总资源
def find_from_xml(xml_file_path):
    """
    : 从XML中解析出SQL代码以及使用的总资源
    :param xml_file_path:xml文件路径
    :return:SQL代码以及使用的总资源
    """
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


# 获取一天所有的job ID
def get_job_id(file_path):
    """
    :获取一天所有的job ID
    :param file_path:
    :return:
    """
    table = []
    with open(file_path,'r') as f:
        read_lines = f.readlines()
        for line in read_lines:
            job_id = line.split('|')[0]
            if job_id not in table:
                table.append(job_id)
    return table


# 下载xml文件到本地
def move_to_local(hdfs_path, local_path):
    """
    :下载xml文件到本地
    :param hdfs_path:
    :param local_path:
    :return:
    """
    os.popen('hadoop fs -copyToLocal ' + hdfs_path + ' ' + local_path)
    return None


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


def get_sql_etl(yesterday):
    """
    :获取SQL等信息
    :param yesterday
    :return:
    """
    table = [0, ]
    syesterday = yesterday.strftime('%Y%m%d')   # 字符串化
    # 年月日字符串化
    year = str(yesterday.year)
    if yesterday.month < 10:
        month = '0' + str(yesterday.month)
    else:
        month = str(yesterday.month)
    if yesterday.day < 10:
        day = '0' + str(yesterday.day)
    else:
        day = str(yesterday.day)
    # 当前路径
    parent_path = os.getcwd()
    # mapred 文件存储路径
    file_path = parent_path + '/' + syesterday + '/' + 'mapred_' + syesterday + '.txt'
    # job_id 列表
    job_tab = get_job_id(file_path)
    for job_id in job_tab:
        hdfs_path = '/mr-history/done/' + year + '/' + month + '/' + day + '/00' \
                    + job_id.split('_')[2][0:4] + '/' + job_id + '_conf.xml'
        local_path = parent_path + '/' + syesterday + '/' + 'xml/' + job_id + '.xml'
        for its in range(3):
            move_to_local(hdfs_path, local_path)
            if os.path.exists(local_path):
                sql, maps, reduces = find_from_xml(local_path)
                table[0] = table[0] + 1
                table.append(job_id)
                table.append(sql)
                table.append(maps)
                table.append(reduces)
                break
    return table


def run():
    """

    :return:
    """
    yest_day = dt.datetime.now() - dt.timedelta(days=1)     # 入库时间
    dele_day = dt.datetime.now() - dt.timedelta(days=4)     # 删除时间

    # 采集sql代码等信息
    sql_path = os.getcwd() + '/' + yest_day.strftime('%Y%m%d') + '/' + 'xml_' + yest_day.strftime('%Y%m%d') + '.txt'
    save_to_file(get_sql_etl(yest_day), sql_path, '|')

    # 数据入库
    db_name = 'default'
    tb_name = ['d_yarn_application_list', 'd_mapred_job_list', 'd_job_sql_etl']
    part_id = 'p_day=\'' + yest_day.strftime('%Y%m%d') + '\''
    file_path = '/user/hive/warehouse/' + tb_name[0] + '/' + 'p_day=' + yest_day.strftime('%Y%m%d')


