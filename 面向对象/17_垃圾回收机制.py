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
        垃圾回收
"""


class Person():
    pass


p1 = Person()  # p1 是指针
print(sys.getrefcount(p1))  # 引用计数2, 原因是是p1传递给getrefcount后, 引用计数会加1
p2 = p1  # 赋值操作, p2 也是指针，都是指向对象。 因此对象的引用计数为2
print(sys.getrefcount(p2))

del p2  # 引用计数 -1
print(sys.getrefcount(p1))
del p1  # 引用计数 -1
# print(sys.getrefcount(p1))    # 已被垃圾回收

# 当引用计数为0时，系统就会回收这个对象。


print('------------------------------------')


# 引用计数加1的场景:
# 1. 构造函数
# 2. 赋值构造
# 3. 当传入函数时
# 4. 当对象放置入容器时

class Person1(object):
    pass


p3 = Person1()
print(sys.getrefcount(p3))

p4 = p3

print(sys.getrefcount(p4))

lst = [p4]  # 当对象放入容器时, 引用计数加1
print(sys.getrefcount(p4))

# 引用计数减1的场景:
# 1. del 1, 析构函数
# 2. 赋值析构
# 3. 对象离开作用域
# 4. 对象所在容器被销毁，或者从容器被删除

lst.clear()
print(sys.getrefcount(p4))

p4 = 123
print(sys.getrefcount(p3))



