# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:02:49 2016

@author: WinQin
"""

class Student(object):
    ''''''
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    
    def __str__(self):
        return 'My name is %s, I\'m %d years old!'%(self.__name,self.__age)
    
    __repr__=__str__
#    def __repr__(self):
        #return 'My name is %s, I\'m %d years old!'%(self.__name,self.__age)
    
    def __call__(self):
        print('My name is %s, I\'m %d years old!'%(self.__name,self.__age))
        

#Test
if __name__=='__main__':
    s=Student('Qsy',28)
    print(s)
    
    s()