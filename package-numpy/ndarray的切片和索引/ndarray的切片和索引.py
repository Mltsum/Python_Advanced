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
        ndarray的切片和索引: 采用切片可以对ndarray做任意的组合拆分
"""

print('---------------------------------')
# 一维数组的切片和索引

# 创建一维数组 [start:stop:step] 左闭右开
a = np.arange(10)
print(a)
print(a[0])
print(a[-1])  # 倒数第N个

# 切片-正索引
print(a[:])  # 索引从开始到结束
print(a[3:5])  # 索引从开始到结束
print(a[1:7:2])  # 索引从开始到结束

# 切片-负索引
print(a[::-1])  # 索引从开始到结束
print(a[-5:-2])  # 索引从开始到结束


print('---------------------------------')
# 二维数组的切片和索引, 采用切片可以对ndarray做任意的组合拆分
b = np.arange(1, 13)
print(b)
b = b.reshape((4, 3))   # ndarray支持直接reshape
print(b)

# 索引
print(b[0][0])

# 切片[行切片，列切片] [[start:stop:step], [start:stop:step]]
# 获取所有行列
print(b[:, :])

# 获取所有行，第二列
print(b[:, 1])






