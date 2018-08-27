# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 22:49:01 2016

@author: WinQin
"""

#import time as tm
import numpy as np
import matplotlib.pyplot as plt

x=np.random.randint(10,size=(10,10))
plt.plot(x.reshape((100,)))
plt.show()
