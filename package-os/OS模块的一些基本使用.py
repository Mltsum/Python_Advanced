import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np

print('------------------------------------')

"""
    python标准库之OS(operation system)
        python和其他语言的交互，和系统的交互
"""

# 系统相关内容
print('------------------------------------')
# os.name 操作系统名，mac: posix windows:nt
print(os.name)

# 环境变量
print(os.environ)

# 分隔符
print(os.sep)

# 多路径分隔符
print(os.pathsep)

# 换行分隔符
print(os.linesep)

print('------------------------------------')
# 获取当前文件夹
print(os.getcwd())

# 获取绝对路径
print(os.path.abspath('.'))

file = os.getcwd() + '/notes'
# 可直接根据file的绝对路径拆分目录和文件 ('/Users/mingren/Documents/07.Code/ScriptCrazyDevil/test', 'notes')
print(os.path.split(file))

# 判断绝对路径
print(os.path.isabs(file))

# 获取文件创建时间和最后修改时间
print(os.path.getatime(file))
print(os.path.getctime(file))

# 获取文件大小
print(os.path.getsize(file))

with open(file) as file:
    pass

print('----------------执行命令--------------------')
# 执行命令
os.system('pwd')
os.system('ll')






