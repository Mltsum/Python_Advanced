import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np
import pydoc

print('------------------------------------')

"""
    python之面向对象
        类的内建函数 - item 操作 : 以字典的使用方式来操作类   
"""


class Person:
    def __init__(self):
        self.cache = {}

    # 向类中增加属性时，通过操作类，以字典的使用方式来增加属性
    def __setitem__(self, key, value):
        print(f'setitem:{key}, {value}')
        self.cache[key] = value

    def __getitem__(self, item):
        print(f'getitem:{item}')
        return self.cache[item]

    def __delitem__(self, key):
        print(f'delitem')
        del self.cache[key]


# 使用类可以用字典的形式来操作类了
p = Person()
p['name'] = 'mashuai'   # 增
n = p['name']           # 获取
del p['name']           # 删

print(p['name'])    # KeyError: 'name'

