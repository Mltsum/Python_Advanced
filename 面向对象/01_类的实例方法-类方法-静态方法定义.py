import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np

print('------------------------------------')

"""
    python之面向对象
        好处是学习python的封装思想，来封装C++。
"""


# 数据类型(int, float...)和对象类型(数据机构类型，比如元祖，列表，字典...)

# pass 指的是空语句，目的是为了保证代码结构的完整性

# 小技巧: 对象.print, 对自动补充为print(money)
class Money:
    def __init__(self):
        self.ele1 = None
        self.ele2 = None
        self.ele3 = None


print(Money.__name__)  # 类名

money = Money()
print(money)  # <__main__.Money object at 0x7fdf240939a0>  __main__之所以可以调用同文件中的其他类，是因为其他该类的类名为__main__.Money。

print(money.__class__)  # 对象的类名和其实例化之前的类是一致的。

# __dict__ 表示当前对象的所有属性(C++也可以封装对应的方法)
print(money.__dict__)  # {'ele1': None, 'ele2': None, 'ele3': None}

# 删除对象中的属性
# del money.ele1
print(money.ele1)  # AttributeError: 'Money' object has no attribute 'ele1'


# 限制对象添加属性; 避免对象被无限添加属性

class Person:
    # 限定类中的属性列表。slots: 槽
    # __slots__ = ['age']  # AttributeError: 'Person' object has no attribute 'num'

    # 实例方法: 实例方法的第一个参数默认会是self
    # 表示该方法是存储在类中
    def func1(self):
        print(f'实例方法{self}')
        pass

    # 类方法: 类方法的第一个参数默认会是cls
    # 表示该方法是存储在类中
    # 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def func2(cls):
        print(f'类方法{cls}')
        pass

    # 静态方法: 静态方法的第一个参数为空
    # 表示该方法是存储在类中
    # 可以通过类调用，也可以通过对象调用
    @staticmethod
    def func3():
        print(f'静态方法')
        pass

# 说明__slots__
p1 = Person()
p1.age = 1
# p1.num = 10
# print(p1.__dict__)


# 属性也可以是一个方法
def run():
    pass
p1.run = run


p1.func1()    # 需要接收一个实例(实例方法<__main__.Person object at 0x7fe01b560c40>)
p1.func2()    # 需要接收一个类(类方法<class '__main__.Person'>)  p1对象的本质也是它对应的类
p1.func3()    # 静态方法

# 静态方法，实例方法，类方法都是存储在类中，而不是对象中。
# {'__module__': '__main__', 'func1': <function Person.func1 at 0x7fae71071820>,
# 'func2': <classmethod object at 0x7fae6e069820>, 'func3': <staticmethod object at 0x7fae6e156130>, '__dict__':
# <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>,
# '__doc__': None}
print(Person.__dict__)
# 对象中存储了对象的属性(其中属性也可以定义为方法)
# {'age': 1, 'run': <function run at 0x7fc65ddba160>}
print(p1.__dict__)


print('------------------------------------')


# 类方法的调用
Person.func2()  # 可以通过类调用，也可以通过对象调用
p1.func2()      # 通过对象调用

# 静态方法的调用
Person.func3()  # 可以通过类调用，也可以通过对象调用
p1.func3()




