import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np
import pydoc

print('------------------------------------')

"""
    python之面向对象
       如何写能自动生成类说明文档的类。 如何标准的设计类, 如何设计能方便别人使用的类。
       1. 增加标准注释 
       2.  python3 -m pydoc -h (-m 以脚本的方式运行模块 python3 --help)  
       (base) mingren@B-7E2NMD6M-2358 test % python3 -m pydoc -p 1234
        Server ready at http://localhost:1234/
        Server commands: [b]rowser, [q]uit
        
        (base) mingren@B-7E2NMD6M-2358 test % python3 -m pydoc -b   (-b, 自动检测端口)
        Server ready at http://localhost:59182/
        Server commands: [b]rowser, [q]uit

        (base) mingren@B-7E2NMD6M-2358 test % python3 -m pydoc -w test   (-w, 写成一个html文档 test.html，直接打开即是html页面文档)

"""


# 根据系统的类设计格式来设计用户的类
# type

class Person:
    """
    这是一个人类的描述

    Attributes:
        count : 表示计数
    """

    # 表示计数
    count = 1

    def run(self, distance, step):
        """
        这是一个人类运行的方法
        :param distance: 参数的含义; 参数的类型; 参数的默认值;
        :param step: 参数的含义; 参数的类型; 参数的默认值;
        :return: 返回值的意义; 返回值的类型; 返回值的默认值; 返回值的异常说明
        """
        print('running...')
        return distance / step


# 生成类的说明文档
help(Person)        # 默认继承的是内建的object : builtins.object
# class Person(builtins.object)
#     |  这是一个人类的描述
#     |
#     |  Attributes:
#     |      count : 表示计数
#     |
#     |  Methods defined here:
#     |
#     |  run(self, distance, step)
#     |      这是一个人类运行的方法
#     |      :param distance: 参数的含义; 参数的类型; 参数的默认值;
#     |      :param step: 参数的含义; 参数的类型; 参数的默认值;
#     |      :return: 返回值的意义; 返回值的类型; 返回值的默认值; 返回值的异常说明
#     |
#     |  ----------------------------------------------------------------------
#     |  Data descriptors defined here:
#     |
#     |  __dict__
#     |      dictionary for instance variables (if defined)
#     |
#     |  __weakref__
#     |      list of weak references to the object (if defined)
#     |
#     |  ----------------------------------------------------------------------
# :
# |  Data and other attributes defined here:
# :
# |
# :
# |  count = 1
# :
