# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 10:57:58 2016

@author: WinQin
"""

class Screen(object):
    ''''''
    def __init__(self,width=1280,height=720):
        self.__width=width
        self.__height=height
        self.__resolution=self.__width*self.__height
    
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,width):
        self.__width=width
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,height):
        self.__height=height
    
    @property
    def resolution(self):
        return self.width*self.height

#Test
if __name__=='__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print(s.resolution)

