# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:51:22 2016

@author: WinQin
"""

import hashlib

db = {}

def get_md5(s):
    md5=hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    
def login(username, password):
    return db[username] == get_md5(password + username + 'the-Salt')


#Test
if __name__=='__main__':
    register('michael','123456')
    register('bob','abc999')
    register('alice','alice2008')
    print(login('michael','123456'))
    print(login('bob','abc999'))
    print(login('alice','alice2008'))