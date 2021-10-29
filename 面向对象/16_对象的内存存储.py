import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np
import pydoc
import collections.abc

print('------------------------------------')

"""
    python之面向对象
        声明周期
"""


# python中所有的数据类型都是对象。 这点和C++不同，C++每一个特定的数据类型都有其固定长度的内存地址。
# 根据不同的数据类型开辟内存空间，并返回内存空间地址。

class Person(object):
    pass


# 判断两个对象是否是同一个的方法就是对比它的id(即内存地址)
p = Person()
# 对象信息及内存地址
print(p)  # <__main__.Person object at 0x7fa860193910>

# Person对象的地址
print(hex(id(p)))  # 0x7fb484a93910


# 容器对象存储的其他对象，仅仅是其他对象的引用，并非其他对象本身。


