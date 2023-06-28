# -*- coding: utf-8 -*-
"""P5-First_Program_Using_OOP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a6NxIWKDa_dhI3ZbMRHR0DX5lh8WpwWF
"""

#In this assignment we would see the use of OOP

class MaxSizeList(object):
    def __init__(self, value):
        self.myList = []
        self.value = value

    def push(self, String):
        try:
            String = str(String)
            self.myList.append(String)
        except ValueError:
            print('You can only push strings!')

    def getList(self):
        print(self.myList[-self.value:])

if __name__ == '__main__':
    a = MaxSizeList(3)
    b = MaxSizeList(1)

    a.push('Hey')
    a.push('Hello')
    a.push('Hi')
    a.push('Let\'s')
    a.push('Go')

    b.push('Hey')
    b.push('Hello')
    b.push('Hi')
    b.push('Let\'s')
    b.push('Go')

    a.getList()
    b.getList()