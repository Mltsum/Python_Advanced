import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np
import pydoc

print('------------------------------------')

"""
    python之面向对象
        类的内建函数 -  自定义比较类对象的方式？  
"""


# 10 > 2， 在python中其实是int类的比较

class Person(object):
    def __init__(self, age, height):
        self.age = age
        self.height = height

    # == != > >= < <=
    # 重载操作符(相等和不想等)
    def __eq__(self, other):
        print('__eq__')
        return self.age == other.age

    def __ne__(self, other):
        print('__ne__')
        return self.height != other.height

    def __gt__(self, other):
        print('__gt__')

    def __ge__(self, other):
        print('__ge__')

    def __lt__(self, other):
        print('__lt__')

    def __le__(self, other):
        print('__le__')


a1 = Person(18, 180)    # 计算两个实例方法
a2 = Person(11, 190)

# 相当于a1 = self,  a2 = other
print(a1 != a2)  # TypeError: '>' not supported between instances of 'A' and 'A'
