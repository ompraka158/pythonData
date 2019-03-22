# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 10:30:05 2018

@author: ompra
"""
class B:
    def show(self):
        super().show()
        print("Second Class")
class A:
    _a=0 # can be private to this class using double underscore else it is protected
    def show(self):
        print("First Class")

class C(B,A):
    def show(self):
        super().show()
        print("Third Class")
a=C()
a.show()
print(a._a)