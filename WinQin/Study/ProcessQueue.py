# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:04:00 2016

@author: WinQin
"""

from multiprocessing import Process,Queue
import os
import time
import random

#Write to queue
def write(queue):
    print('Process to write: %s.'%os.getpid())
    for value in ['A','B','B','D','E','F']:
        print('Put %s to queue...'%value)
        queue.put(value)
        time.sleep(random.random())

#Read from queue
def read(queue):
    print('Procee to read: %s.'%os.getpid())
    while True:
        value=queue.get(True)
        print('Get %s from queue.'%value)
        #time.sleep(random.random()*5)

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
