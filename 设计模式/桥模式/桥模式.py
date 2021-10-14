import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

"""
    Python中的桥模式 
    解决的问题: 将一个事物的两个维度分离，使其都可以独立的变化
    1. 维度独立
    2. 两个维度不可分离
"""


# 定义一个形状类
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color  # 将颜色作为形状的一个属性

    @abstractmethod
    def draw(self):
        pass


# 定义一个颜色类
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


# 画方形逻辑
class Rectangle(Shape):
    name = "方形"

    def draw(self):
        # 方形逻辑
        self.color.paint(self)


# 画圆形逻辑
class Circle(Shape):
    name = "圆形"

    def draw(self):
        # 圆形逻辑
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


class Green(Color):
    def paint(self, shape):
        print("绿色的%s" % shape.name)


# 其实说白了步骤就是:
# 1) 目的是构造一个物体的形状属性Rectangle，故有构造函数Rectangle
# 2) 但形状属性是分离不了颜色的，因此传入颜色属性，故有颜色的构造函数，传入之后是作为形状的一个属性。

shape = Rectangle(Red())  # 将一个物体的不同属性分离，使其可以独立变化。并可以随意组合成不同属性的物体。
shape.draw()

shape = Circle(Green())
shape.draw()
