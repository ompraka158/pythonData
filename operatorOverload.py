# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 11:08:03 2018

@author: ompra
"""

class vector2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        print(type(other))
        return vector2d(self.x+other.x,self.y+other.y)
first = vector2d(10,11)
second= vector2d(12,13)
result = first + second
print(" x : %d, y= : %d"%(result.x,result.y))