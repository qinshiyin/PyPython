#!/usr/bin/env python

import os

path = input('Pleas input the parent path:')
ld = []
try:
    ld = os.listdir(path)
except FileNotFoundError as e:
    print(e.strerror)
finally:
    print(ld)
