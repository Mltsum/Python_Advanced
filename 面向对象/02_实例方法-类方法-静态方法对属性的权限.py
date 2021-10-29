import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np

print('------------------------------------')

"""
    python之面向对象
        
"""


# 属性是区分类属性和实例属性的
class Person:
    cls_ele = None  # 类属性

    # 可以拿到类和实例, 如实例方法，能拿到实例self和类cls，因此实例属性和类属性都可以访问
    def shilifangfa(self):
        print(self.cls_ele)
        print(self.instance_ele)

    # 类方法智能访问类属性，不能访问实例属性，如类方法，只能拿到cls或者Person，因此只能访问类属性
    @classmethod
    def leifangfa(cls):
        print(cls.cls_ele)

    # 能否访问属性取决于该种类的方法, 能否拿到对应的类或者兑现。 如静态方法，就只能拿到Person， 因此只能访问类属性
    @staticmethod
    def jingtaifangfa():
        print(Person.cls_ele)

p = Person()
p.instance_ele = None  # 实例属性

# 对象可以访问类属性和实例属性， 但是类不能访问对象属性
print(Person.cls_ele)
print(p.cls_ele)
print(p.instance_ele)

print('------------------------------------')

# 不同函数种类的访问权限
p.shilifangfa()     # 可以拿到类和实例
print('----------')
Person.leifangfa()
print('----------')
p.jingtaifangfa()