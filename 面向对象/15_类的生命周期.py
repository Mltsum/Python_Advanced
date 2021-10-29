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


# 监听对象生命周期的方法
#     __new__, __init__, __del__

class Person(object):
    # __new__ 定义之后，在构造对象时就不会默认new，而是调用__new__
    def __new__(cls, *args, **kwargs):
        print('新建一个对象，但是被拦截了')

    # 当对象初始化完成后，会自动调用__init__，并传入self
    def __init__(self):
        print('__init__')
        self.name = 'sz'

    def __del__(self):
        print('__del__')


p = Person()
print(p)
del p

print('------------------------------------')

global_var = 0


class Person1(object):
    element = 0
    def __init__(self):
        print('计数 + 1')
        global global_var
        # 对于模块中定义的变量。类中只能读取，而不能写入，因为解释器判定不了，程序员的意图是修改模块内变量还是向类中新增加属性
        global_var += 1

    def __del__(self):
        print('计数 - 1')
        global global_var
        # 对于模块中定义的变量。类中只能读取，而不能写入，因为解释器判定不了，程序员的意图是修改模块内变量还是向类中新增加属性
        # 解决办法是增加 global关键字
        global_var -= 1

    # 如果方法中想要操作类内的元素，则设置为类方法
    @classmethod
    def log(cls):
        print(f'我要打印类内的元素:{cls.element}')

    # 如果方法中，想要脱离对象而调用，则设置为静态方法
    @staticmethod
    def log():
        print('我要打印...')


p1 = Person1()
p1.log()
