#!/usr/bin/env python
# -*- coding:utf-8 -*-


import aiohttp
import asyncio
import datetime as dt
from urllib import request
import ssl
url_1 = 'https://218.205.68.67:8000/dataex/api/auth?userId=hujingyue&pwd=shhenpzZU5w'

async def get_status(url):
    try:
        ssl._create_default_https_context=ssl._create_unverified_context
        async with aiohttp.ClientSession() as session:
            async with session.request('OPEN', url=url_1) as resp:
                # print(resp.status)
                print(await resp.text())
    except Exception as e:
        print(dt.datetime.strftime(dt.datetime.now(),'%Y-%m-%d %H:%M:%S ') + str(e))

tasks = []
for i in range(1):
    tasks.append(asyncio.ensure_future(get_status(url_1)))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
