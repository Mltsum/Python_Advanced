import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np

print('---------------------------------')

"""
    Numpy: 科学计算基础库
    最核心数据类型: ndarray(多维数组类型)
    底层用C写, 因此速率会很快
    
    本模块:
        生成[任意类型] [任意维度]的数组
"""

# range 左闭右开 [start, end)
for i in range(0, 10, 1):
    print(i)

# range 列表化
lst = list(range(10))

print('---------------------------------')

# 创建数组(左闭右开)
a = np.arange(1,10)
print(a)
print(type(a))  # ndarray

print('---------------------------------')

# 对数组进行开根号(直接向量处理)
b = np.sqrt(a)
print(b)
print(type(b))

print('---------------------------------')

# 创建多维数组
c = np.array([1, 2, 3, 4])
print(c)
print(type(c))

# 设置数据类型
c1 = np.array([1, 2, 3, 4], dtype=float)

# 设置数据维度 ndmin 设置数据的维度  dtype 设置数据的类型
c2 = np.array([1, 2, 3, 4], dtype=float, ndmin=3)
print(c2)
print(type(c2))

print('---------------------------------')

# 创建二维数组
d = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(d)
print(type(d))

print('---------------------------------')

# 创建三维数组
e = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]]])
print(e)
print(type(e))

print('---------------------------------')

# 使用随机数创建数组[0.0,1.0)
f = np.random.random(size=5)
print(f)
# 使用随机数创建二维数组[0.0,1.0)
f = np.random.random(size=(3, 4))
print(f)
# 使用随机数创建三维数组[0.0,1.0)
f = np.random.random(size=(2, 3, 4))
print(f)

print('---------------------------------')

# 创建随机整数
g = np.random.randint(5, size=(2, 2))
print(g)

print('---------------------------------')

#  创建正态分布(期望为0，方差为1)
f = np.random.randn(4)
print(f)

print('---------------------------------')

