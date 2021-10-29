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
        类的内建函数 -  遍历自己创建的对象  
"""


class Person(object):

    def __init__(self):
        self.idx = 0
        self.result = [1, 2, 3, 4, 5, 6, 7, 8]

    # 遍历方式1， 提供获取元素的方法， 循环每次获取时就会轮训获取元素
    def __getitem__(self, _idx):
        print('__getitem__')
        return self.result[_idx]

    # 优先级是最高的。当有遍历调用时，优先调用此方法
    # 主要作用是返回一个迭代器，如果返回的不是迭代器，需要在返回类中实现__next__
    def __iter__(self):
        print('__inter__')
        # return iter([1, 2, 3, 4, 5])  # 调用列表迭代器的next方法
        return self  # 调用Person迭代器的next方法，但需要Person实现__next__方法

    # 遍历方式2
    # 表示本对象迭代器的下一个
    def __next__(self):
        self.idx += 1
        if self.idx < 10:
            return self.idx
        else:
            raise StopIteration('停止遍历')


p = Person()

# 访问下一个
print(next(p))
print(next(p))
print(next(p))
print(next(p))

# 其实本质还是通过下标来索引
# 迭代器用过一次就不能用拉, 原因是变量已经改变拉。
for idx in p:  # TypeError: 'type' object is not iterable
    print(idx)


# 判断是否为迭代器
# 迭代器必须实现__iter__ __next__
print(isinstance(p, collections.abc.Iterable))
