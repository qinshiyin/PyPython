#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hearthit as hh

# url_1 = 'https://218.205.68.67:8000/dataex/api/auth?userId=hujingyue&pwd=shhenpzZU5w'
url_2 = 'https://218.205.68.67:8000/dataex/api/data_pr/tele_fac?token=nfnzg0ro&appKey=acfbc245c56390731b81c583d585b640&auth_code=1&bill_no=13575750022'
# url_1 = 'https://www.google.com.hk'
url_1 = 'https://218.205.68.67:8002/dataex/api/auth?userId=hujingyue&pwd=shhenpzZU5w'

(token,_) = hh.get_token(url_1, 50)
print(token)
if not isinstance(token, Exception):
    print(hh.rep_token(url_2, token))
