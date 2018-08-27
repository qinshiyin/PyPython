#!/usr/bin/env python
# -*- coding:utf-8 -*-


import ssl
import time
import datetime as dt
from urllib import request


def get_token(url, seconds):
    """
    获取token值，如果系统响应超时，则返回空值字符串"None"；
    :param url:
    :param seconds:
    :return:获取的token值，如空则返回NULL；页面响应时长
    """
    if not url:
        return 'URL is null', -1
    try:
        ssl._create_default_https_context=ssl._create_unverified_context
        toc = time.process_time()
        response = request.urlopen(url, timeout=seconds)
        tic = time.process_time()
        page = str(response.read(), encoding='utf-8')
        if not page:
            return 'Null', -1
        if 'token' not in page:
            return 'Get nothing', -1
        return page.split(':')[1].split('"')[1], tic - toc
    except Exception as e:
        return e, seconds


def rep_token(url, token):
    """
    拼接新的URL，将token放入URL中返回新的URL
    :param url:旧的URL
    :param token:需要替换的token值
    :return:新的URL
    """
    if not url:
        return 'Null'
    if not token:
        return 'Null'
    if 'token=' in url:
        list_url = url.split('token=')
        list_url_2 = list_url[1].split('&')
        list_url_2[0] = token
        return list_url[0] + 'token=' + '&'.join(list_url_2)
    else:
        return 'Null'


def resp_time(url, seconds):
    """
    获取数据响应时间
    :param url:
    :param seconds:
    :return:
    """
    if not url:
        return -1
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        toc = time.process_time()
        response = request.urlopen(url, timeout=seconds)
        tic = time.process_time()
        page = str(response.read(), encoding='utf-8')
        if not page:
            return 'Null', -1
        else:
            return page, tic - toc
    except Exception as e:
        return e, seconds


def read_config(path):
    if not path:
        return []
    with open(path, 'rb') as f:
        str_lines = f.readlines()
    cfg = []
    begin = False
    tmp = {}
    for item in str_lines:
        line = item.decode('utf-8')
        if line[0] == '#':
            continue
        if len(line) < len('end'):
            continue
        if 'begin' in line:
            begin = True
            tmp.clear()
            continue
        if 'end' in line and begin:
            cfg.append(tmp.copy())
            begin = False

        if begin:
            ls = line.split('\n')[0].split('\r')[0].split('@')
            tmp[ls[0]] = ls[1]
    return cfg


def save_warning(warning, path):
    with open(path, 'w') as f:
        f.writelines(warning)


def run(beat_per_second):
    while True:
        warn_list = read_config('alarm.txt')
        warning = []
        for interface in warn_list:
            token, response_time = get_token(interface['token_url'], int(interface['token_wait_time']))
            if isinstance(token, Exception):
                error_str = '接口:' + interface['interface_name'] + ' 在' +\
                            dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S') \
                            + '无法获取token，错误代码为：' + str(token)\
                            + ', 接口失败等待时间为：' + str(response_time) + '秒。\n'
                warning.append(error_str)
            else:
                data_url = rep_token(interface['data_url'], token)
                page, response_time = resp_time(data_url, int(interface['data_wait_time']))
                if isinstance(page, Exception):
                    error_str = '接口:' + interface['interface_name'] + ' 在' +\
                            dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S') \
                            + '无法获取数据，错误代码为：' + str(page)\
                            + ', 接口失败等待时间为：' + str(response_time) + '秒。\n'
                    warning.append(error_str)
        save_warning(warning, 'warning.txt')
        time.sleep(beat_per_second)


# Test
if __name__ == '__main__':
    run(0)

