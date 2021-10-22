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
       
"""
a = np.arange(1, 25).reshape(8, 3)
print(a)

# transpose进行转置
b = a.transpose()
print(b)

# .T进行转置
print(a.T)

print('---------------拼接------------------')


# 多维数组的转置
c = b.reshape(2, 3, 4)
print(c)

print('---------------拼接------------------')

d = c.transpose()
print(d)
