import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np
import pydoc

print('------------------------------------')

"""
    python之面向对象
        类的访问权限
"""


# python 类属性的私有化
# 无下划线+属性:表示公有属性; _属性 表示受保护属性; __表示私有属性

class Animal:
    # 构造函数
    def __init__(self):
        self.element = None
        self.__element1 = None # 私有属性， 不想在类外被随意修改。 如果要提供方法，则写函数去获取。
        pass

    x = 10
    _x = 20
    __x = 30  # 实际上是伪私有，是编译器会自动将__x重命名为 _类名__x， 因此是访问不了的。

    def test(self):
        print(self._x)
        print(self.__x)

    def set_element1(self, value):
        # 范围检查
        if isinstance(value, int) and 0 < value < 200:
            self.__element1 = value
        else:
            print('数据非法！')


class Dog(Animal):
    def test(self):
        print(self.x)
        print(self._x)  # 继承也可以访问被保护的属性
        # print(self.__x)  # 子类访问不了父类的私有成员


# 测试公有属性
print('------------------------------------')
dog = Dog()
print(dog.x)  # 公有属性是可以在派生类中访问的
print('-----------------')

print(Dog.x)  # 公有属性是可以在模块中访问的

print('------------------------------------')

# 测试受保护属性
a = Animal()
a.test()
print('-----------------')

dog1 = Dog()
dog1.test()
print(Dog._x)  # 模块中也可以访问被保护属性，但是会有下划线警告

print('------------------------------------')

# 测试私有属性
dog3 = Dog()
# print(dog3.__x)     # 子类和模块中都不能访问基类的私有成员

# 通过私有属性的重命名机制来访问私有成员
a1 = Animal()
print(Animal.__dict__)
print(Animal._Animal__x)  # 访问到了私有属性

# 关于跨模块的访问权限
_x = 100  # 表示只在模块内可访问
__all__ = ["_x"]  # 表示本模块内的参数对其他模块也开放 且可改变protect和private的成员。
