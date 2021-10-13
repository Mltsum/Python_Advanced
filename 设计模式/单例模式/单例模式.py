import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

"""
    Python中的单例模式: 应用对象，整个应用中只出现一次，如日志系统。
"""


class Singleton:
    # __new__是一种负责创建[类实例]的静态方法，它无需使用 staticmethod 装饰器修饰，且该方法会优先 __init__() 初始化方法被调用
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 调用父类的new方法来创建一个实例
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10)
b = MyClass(20)

print(id(a))
print(id(b))  # id一致，就说明两个是同一个实例
