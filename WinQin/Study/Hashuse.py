# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:34:24 2016

@author: WinQin
"""

import hashlib

def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

db={
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

ids={
    'michael': '123456',
    'bob': 'abc999',
    'alice': 'alice2008'
}

def login(user, password):
    return calc_md5(password)==db[user]


#Test
if __name__=='__main__':
    print(login('michael','123456'))
    print(login('bob','abc999'))
    print(login('alice','alice2008'))

