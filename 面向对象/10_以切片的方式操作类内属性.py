import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np
import pydoc

print('------------------------------------')

"""
    python之面向对象
        类的内建函数 -  对对象进行切片操作？  
"""


class Person:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 6, 7]

    def __setitem__(self, key, value):
        print(key, value)
        print(key.start)
        print(key.stop)
        print(key.step)
        print(value)
        if isinstance(key, slice):
            self.items[key] = value
        else:
            print('类型错误')

    def __getitem__(self, item):
        print('getitem', item)

    def __delitem__(self, key):
        print('delitem', key)


p = Person()
p[0:4:2] = ['a', 'b']  # slice(0, 4, 2) [1, 2]

print(p.items)  # 可以不声明用户方法的前提下，修改类内的数据。

# 切片
# slice

# 索引
# p[0:4:3]

# 删除
# del p[0:4:2]
