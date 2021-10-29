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
        封装 - 继承 - 多态
"""


# 设置抽象类(主要作用是方式抽象类被实例化)
class Animal(metaclass=ABCMeta):

    # 设置抽象类
    @abstractmethod
    def func(self):
        pass

    pass


class Person(object):
    pass


# 多继承
class Mashuai(Animal, Person):
    pass


# 打印类的基类
print(Mashuai.__bases__)  # 打印基础类

# bool的基类
print(bool.__bases__)  # (<class 'int'>,)

# 多态: python是动态语言，关注的对象的使用，而不是数据的类型。
