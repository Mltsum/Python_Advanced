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
        关于ndarray
"""

a = np.array([1, 2, 3], ndmin=3)
print(a)
print(f"shape:{a.shape}")
print(f"ndim:{a.ndim}")
print(f"type:{a.dtype}")
print(f"size:{a.size}")
print(f"itemsize:{a.itemsize}")

print('---------------------------------')

# 创建都是0的数组
b = np.zeros(5)
print(b)

# 创建都是1的数组
b = np.ones(5)
print(b)

# 将内存中已经有的值擦除
b = np.empty(8)
print(b)

# 创建等差数列
b = np.linspace(1, 10, 20, endpoint=True)
print(b)

# 创建等比数列
b = np.logspace(0, 9, 10)
print(b)

print('---------------------------------')
