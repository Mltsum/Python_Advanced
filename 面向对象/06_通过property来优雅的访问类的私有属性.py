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


# 当与系统内置关键字区分时，在名字后增加下划线， 比如 class_

# 只读属性，如何设置呢？ 方法为设置私有，然后通过方法控制读写权限

class Person(object):       # 继承来自object
    def __init__(self):
        self.__age = 18

    @property  # 主要作用是以使用属性的方式来使用这个方法 (将属性的删，改，查关联到一个方法中)
    def age(self):
        return self.__age


p = Person()
print(p.age)  # 增加了@property 后, 就可以以调用属性的方式来调用方法。

# 增加了@property 后, 当赋值时，就会报错 AttributeError: can't set attribute, 达到了只读的效果
# p.age = 100
