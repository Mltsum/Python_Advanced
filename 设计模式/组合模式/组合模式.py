import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

"""
    Python中的组合模式
    将对象组合成树形结构，以表示"部分-整体"的层次结构，组合模式对于部分和整体的使用具有一致性。
"""


# 定义一个抽象形状类
class Graphic:
    # 目的是定义一个抽象类，使得对部分和整体的使用具有一致性
    def draw(self):
        pass


# 实现点类
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点(%s, %s)" % (self.x, self.y)

    def draw(self):
        print(str(self))


# 实现线类
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段[%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))


# 实现复杂图形
class Picture(Graphic):
    def __init__(self, iterable):       # 对于多层切层数不定的组合时，定义同样的虚接口和组合是关键
        self.children = []
        for i in iterable:
            self.add(i)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("picture start...")
        for i in self.children:
            print(str(i))
        print("picture end...")


p1 = Point(1, 1)
l1 = Line(Point(2, 2), Point(3, 3))
l2 = Line(Point(4, 4), Point(5, 5))
pic = Picture([p1, l1, l2])
pic.draw()
