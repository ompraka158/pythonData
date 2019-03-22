# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 10:50:12 2018

@author: ompra
"""

from tkinter import *
root=Tk()
label=Label(root,text="I am a label Widget",bg="red",fg="white")
def x():
    print("Hello")
button=Button(root, text="I am a button", command = x)
label.pack()
button.pack()
print(type(label))
print(type(button))
root.mainloop()