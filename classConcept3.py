# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 10:12:09 2018

@author: ompra
"""

class Record:
    def setData(self,name,age):
        self.name=name
        self.age=age
    def getData(self):
        print("Name : %s, Age : %d"%(self.name,self.age))
a=Record
a.setData(a, "Ankur",22)
a.getData(a)