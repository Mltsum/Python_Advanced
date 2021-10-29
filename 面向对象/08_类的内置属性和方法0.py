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


# 系统内置的属性

class Person(object):
    """
    这是一个人相关的类
    """
    age = 19

    def __init__(self):
        self.name = 'sz'

    def running(self):
        print('running...')


# 获取类成员
print(Person.__dict__)

# 获取类的基类，python支持多重继承，获取的结果是一个元祖
print(Person.__base__)

# 获取类说明
print(Person.__doc__)

# 获取类名称
print(Person.__name__)

# 获取类所在的模块
print(Person.__module__)  # __main__ 主模块

p = Person()
print(p.__class__)  # <class '__main__.Person'>

print('------------------------------------')


# 关于私有方法

class Person1(object):
    __age = 18

    def __run(self):  # 方法私有只需要在方法前设置下划线即可。   # 私有函数会重命名机制为Person1.__run，因此不可直接调用。 重命名机制的优先级比用户自定义低
        print('private running...')


print(Person1.__dict__)

print('------------------------------------')


# 系统内置一些特殊方法

class Person2(object):
    def __init__(self, name, age):  # 构造函数
        self.name = name
        self.age = age

    # 实现object的信息格式化方法。
    # 面向用户
    def __str__(self):
        return f'name={self.name}, age={self.age}'

    # 打印实例信息，一般不用。如果用户定义了，就能用repr(p)来获取实例对象信息了
    # 面向开发人员，面向解释器
    def __repr__(self):
        return 'repr'


# 生命周期方法， 关于python内存管理


# 其他内置方法

p = Person2('sz', 18)
print(p.__dict__)

# 打印类中的属性值
print(p)  # <__main__.Person2 object at 0x7fddc77703a0> 【重点】
print(p.__str__())  # 信息格式化，如果用户无定义，则返回类信息，如果用户定义，则返回用户定义的格式。 总之，用户定义的优先级最高。
print(str(p))

# 获取实例对象的实例信息
print(repr(p))  # 原因是定义好__str__之后，print(p)就不实用了。 因此需要repr()

print('------------------------------------')


# __call__方法

class Person3(object):
    # 如果无定义__call__，默认通过对象直接调用函数是不可以调用的， 定义之后，默认会调用__call__
    def __call__(self, *args, **kwargs):
        print('__call__', args, kwargs)


p3 = Person3()
p3('name', 'age')  # 当对象实例化后，可以通过直接调用实例，将对象传入。 # 偏函数

print('创建了%s类型的画笔, 它是%s颜色' % ('钢笔', '红色'))


def create_pen(pen_type, pen_color):
    print('创建了%s类型的画笔, 它是%s颜色' % (pen_type, pen_color))


# 创建偏函数
import functools

gangbi_pen = functools.partial(create_pen, pen_type='钢笔')
# gangbi_pen('红色')    # TypeError: create_pen() got multiple values for argument 'type'
gangbi_pen(pen_color='红色')  # 指定入参。 另外一种方式是调换参数的顺序


class PenFactory(object):

    def __init__(self, pen_type):
        self.pen_type = pen_type

    # 思想类似于偏函数
    def __call__(self, pen_color):
        print('创建了%s类型的画笔, 它是%s颜色' % (self.pen_type, pen_color))


gangbi_factory = PenFactory('钢笔')
gangbi_factory('红色')            # 结果想要的就是通过函数调用的方式，将更改属性。函数调用没有自定义函数，而是通过内置的__call__
gangbi_factory('绿色')
gangbi_factory('蓝色')
