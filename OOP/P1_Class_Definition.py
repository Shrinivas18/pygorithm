# -*- coding: utf-8 -*-
"""P1-Class_Definition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a6NxIWKDa_dhI3ZbMRHR0DX5lh8WpwWF
"""

#In this program we will see how to define a class
class MyFirstClass():
    #Class Attributes
    var = 10

firstObject = MyFirstClass()
print(firstObject)      #Printing object's memory hex
print(firstObject.var)  #Accessing Class Attributes

secondObject = MyFirstClass()
print(secondObject)
print(secondObject.var)