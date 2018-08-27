# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:18:59 2016

@author: WinQin
"""

from multiprocessing import Process
import os

def run(name):
    print("Run child process %s(%s)"%(name,os.getpid()))

if __name__=='__main__':
    print("Run parent process %s."%os.getpid())
    p=Process(target=run,args=("Test",))
    p.start()
    p.join()
    print("Parent process end.")
