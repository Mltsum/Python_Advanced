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
        不同维度的ndarray进行相互转换
"""

print('---------------------------------')

a = np.arange(6)
print(a)
# 一维度转多维度
b = a.reshape(2, 3)
print(b)

print('---------------------------------')

# 多维度转一维度 reshape(-1)
a = np.arange(6)
# 一维度转多维度
b = a.reshape(2, 3)
print(b)
b = b.reshape(-1)
print(b)

print('---------------------------------')

# 多维度转一维度 - ravel(缠绕)
a = np.arange(6)
# 一维度转多维度
b = a.reshape(2, 3)
print(b)
b = b.ravel()
print(b)

print('---------------------------------')

# 多维度转一维度 - flatten
a = np.arange(6)
# 一维度转多维度
b = a.reshape(2, 3)
print(b)
b = b.flatten()
print(b)
