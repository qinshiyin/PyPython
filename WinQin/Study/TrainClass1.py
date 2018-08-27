# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 10:20:04 2016

@author: WinQin
"""

class People(object):
    ''''''
    __slots__=('name','age')
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def print_info(self):
        print('My name is %s, I\'m %d years old.'%(self.name,self.age))


class Student(People):
    ''''''
    __slots__=('grade','classes')
    def __init__(self,name,age,grade,classes):
        People.__init__(self,name,age)
        self.grade=grade
        self.classes=classes
    def print_info(self):
        print('My name is %s, I\'m %d years old. I am in grade %d class %d'%
        (self.name,self.age,self.grade,self.classes))
    

#Test
if __name__=='__main__':
    p=People('Bob',12)
    p.print_info()
    s=Student('Jonh',12,6,8)
    s.print_info()