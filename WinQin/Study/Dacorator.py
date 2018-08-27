# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:53:33 2016

@author: WinQin
"""
import functools
import datetime as dt

def log(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wraper(*args,**kw):
            try:
                print(text)
                print('begin call time:',dt.datetime.now())
                print('function name:',func.__name__)
                return func(*args,**kw)
            finally:
                print('end call time:',dt.datetime.now())
        return wraper
    return decorator

@log('execute')
def say(name):
    print('Hello! I\'m glad to see you! ',name)
    
#Test
if __name__=='__main__':
    say('Bob')