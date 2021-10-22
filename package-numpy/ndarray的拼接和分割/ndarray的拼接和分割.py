import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np

print('---------------拼接------------------')

"""
    Numpy: 科学计算基础库
    最核心数据类型: ndarray(多维数组类型)
    底层用C写, 因此速率会很快
    
    本模块:
        ndarray 的拼接和分割
"""

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(a)
print(b)

c = np.hstack((a, b))
print(c)

d = np.vstack((a, b))
print(d)

print('---------------------------------')

# concatenate, 拼接指定拼接的轴， 轴默认为0， 垂直方向拼接
e = np.concatenate((a, b), axis=0)
print(e)

print('---------------------------------')

# concatenate, 拼接指定拼接的轴， 轴默认为0， 垂直方向拼接
f = np.concatenate((a, b), axis=1)
print(f)

print('--------------分割-------------------')

g = np.arange(12)
x = np.split(g, 4)
print(x)

# 传递数组，按照位置分割
g = np.arange(12)
x = np.split(g, [2, 6])
print(x)
