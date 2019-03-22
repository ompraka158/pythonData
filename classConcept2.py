# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 09:52:28 2018

@author: ompra
"""

class Employee:
    empCount=0 #variable which will hold number of objects
   
    def __init__(self,name,salary):
        self.salary=salary
        self.name=name
        Employee.empCount+=1 #Class reference used so the value is incremented for all the objects
    def displayCount(self):
        print("Total Employee : %d" %Employee.empCount)
    def displayEmployee(self):
        print("Name : %s, Salary= %d" %(self.name,self.salary))
a=Employee("Ankur",10000)
b=Employee("Rajesh",12000)
a.displayCount()
a.displayEmployee()
b.displayEmployee()