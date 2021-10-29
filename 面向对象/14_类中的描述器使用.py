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
        类的内建函数 -  描述器 :  指的是属性指向了一个描述器对象，描述器对象实现了三个方法: __set__, __get__, __delete__
        如果想操作描述器，解释器能识别描述器并自动转换调用描述器的方法
"""


class Descriptor(object):
    # 描述器构建方式3
    # 如果外界想要赋值，则会自动转化到描述器中，进行规则检查
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass

    def __delete__(self, instance):
        pass


class Person(object):
    name = 'sz'

    def __init__(self):
        self.__age = 10  # 私有属性

    # 描述器构建方式2
    @property
    def age(self):
        return self.__age

    # 传统设置__age的方法
    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    # 描述器构建方式1
    # 构建描述器， 构建完成后才能用描述器的特性
    # age = property(fset=age, fget=age, fdel=age)

    age1 = Descriptor()


help(Person)
# class Person(builtins.object)
#     |  Methods defined here:
#     |
#     |  __init__(self)
#     |      Initialize self.  See help(type(self)) for accurate signature.
#         |
#     |  ----------------------------------------------------------------------
#     |  Data descriptors defined here:
#     |
#     |  __dict__
#     |      dictionary for instance variables (if defined)
#     |
#     |  __weakref__
#     |      list of weak references to the object (if defined)
#     |
#     |  age
#     |
#     |  age1
#     |
#     |  ----------------------------------------------------------------------
#     |  Data and other attributes defined here:
# :
# |
# :
# |  name = 'sz'
# :
