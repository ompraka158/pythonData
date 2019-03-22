# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 09:40:01 2018

@author: ompra
"""

class Vehicle:
    NoPlate=''
    def __init__(self):
        print("Object created")
    def setValues(self,No):
        self.NoPlate=No
    def show(self):
        print("Registerd on "+self.NoPlate)
def main():
    a=Vehicle()
    a.setValues("BR01CG4201")
    a.show()
if __name__=="__main__":
    main()