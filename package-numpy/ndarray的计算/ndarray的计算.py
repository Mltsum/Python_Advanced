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
        numpy 用到的常用函数
"""

a = np.arange(2)
print(a)
b = np.arange(2)
print(b)

# np.add()
print(np.add(a, b))
print(a + b)

# np.substract()
print(np.subtract(a, b))
print(a - b)

# np.substract()
print(np.multiply(a, b))
print(a * b)

# np.substract()
a[0] = 10
b[0] = 5
print(np.divide(a, b))
print(a // b)