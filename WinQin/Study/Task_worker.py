#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time,sys,queue
from  multiprocessing.managers import BaseManager

#闯将类似的QueueManager
class QueueManager(BaseManager):
    pass

#由于这个QueueManger只从网上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器，也就是运行task_master的机器
server_addr='127.0.0.1'
print('Connect to server %s...'%server_addr)
#端口和验证码设置与task_master一致
manager=QueueManager(address=(server_addr,5000),authkey=b'abc')
#从网络连接
manager.connect()
#获取Queue的对象
task=manager.get_task_queue()
result=manager.get_result_queue()
#从Task队列获取任务，并把结果写入result队列
for x in range(10):
    try:
        n=task.get(timeout=1)
        print('run task %d * %d...'%(n,n))
        r='%d * %d = %d'%(n,n,n**2)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
#处理结束
print('worker exit.')