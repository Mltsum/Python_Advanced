import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np
import pydoc

print('------------------------------------')

"""
    python之面向对象
        类的内建函数 -  自定义比较类对象的方式？  
"""


# 确定当前类的bool值
# __bool__

class Person1(object):
    def __init__(self, status):
        self.status = status

    # 控制本对象是True还是False
    def __bool__(self):
        return self.status


p1 = Person1(True)
if p1:
    print('p1 是 True')

p2 = Person1(False)
if p2:
    print('p2 是 False')
