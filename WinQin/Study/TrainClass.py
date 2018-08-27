# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:29:27 2016

@author: WinQin
"""

class People:
    ''''''
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_data(self):
        print("我叫 %s ,今年 %d 岁了,上 %d 年级" % (self.name,self.age,self.grade))

class Student(People):

    def __init__(self,name,age,grade,like):
        People.__init__(self,name,age,grade)
        self.like = like

    def print_data(self):
        print("我叫 %s ,今年 %d 岁了,上 %d 年级,我喜欢 %s" % (self.name,self.age,self.grade,self.like))



class Tolal():

    def __init__(self,name,say):
        self.name = name
        self.say = say

    def print_data(self):
        print("我叫 %s ,今天我为大家演讲的是 %s" % (self.name,self.say))

class Sample(Tolal,Student):

    def __init__(self,name,age,grade,like,say):
        Student.__init__(self,name,age,grade,like)
        Tolal.__init__(self,name,say)


s = People("Jack",12,5)
s.print_data()

x = Student("Jack",12,5,"Python")
x.print_data()

a = Sample("JAck",12,5,"Python","Python")
a.print_data()