import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np
import pydoc

print('------------------------------------')

"""
    python之面向对象
        
"""


# 经典类: 没有继承object (python2 版本定义类时，默认不继承object)
# 新式类: 继承了object (python3 版本定义类时，默认继承object)
class Person(object):   # 因此尽可能的显示的继承object，这样就可以兼容python3和python2
    def __init__(self):
        self.__age = 18


# 判断类是新式类还是经典类
print(Person.__base__)  # <class 'object'>

# 新式类的基类
# object


print('------------------------------------')


class Person1(object):

    # 增加一个实例，或者修改属性时，会调用这个方法
    def __setattr__(self, key, value):
        print(key, value)

    pass


p1 = Person1()
p1.age = 18

print(p1.age)
