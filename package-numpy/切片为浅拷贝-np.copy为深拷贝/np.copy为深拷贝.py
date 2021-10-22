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
        切片其实是浅拷贝，如果想要深拷贝，则应该使用np.copy()
"""

print('---------------------------------')
#
a = np.arange(1, 13)
a = a.reshape(3, 4)
print(a)

# 切片获取到的新数组是原数组的浅拷贝

sub_a = a[:2, :2]
print(sub_a)

sub_a[0][0] = 1000

print(sub_a)
print(a)

# 如果不想浅拷贝，则可以采用深拷贝
sub_a1 = np.copy(a[:2, :2])
sub_a1[0][0] = 2000

print(sub_a1)
print(a)







