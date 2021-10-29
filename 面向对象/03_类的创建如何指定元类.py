import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np

print('------------------------------------')

"""
    python之面向对象
       创建类的过程: 先去找元类，找不到的话再去类的父类找元类，依次检索父类，如果在找不到的话，就从模块级别找，再找不到的话,就用type作为元类来创建类。     
"""


class Animal:
    pass


# 通过模块级别来指定元类(作用范围在整个模块)
# __metaclass__ = Animal


# 基类也叫做元类(__metaclass__ 表明元类是谁)
# metaclass 表示显示的声明本类的元类是谁
class Person(metaclass=ABCMeta):  # __metaclass__ 通过(metaclass=ABCMeta)来指定元类
    def __init__(self):
        pass

    def run(self):
        pass


# 如何指明元类
class Person1:
    # __metaclass__ 通过此方法来指定元类
    __metaclass__ = Animal
    pass
