import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠
import numpy as np
import pydoc
import collections.abc

print('------------------------------------')

"""
    python之面向对象
        
"""


class Person(object):
    # 操作类属性而不操作对象属性的方法，就需要设置为类方法，传入cls即可。
    result = 1  # 类属性

    def __init__(self):
        self.res = 1  # 对象属性， 只有成功构造后，才会有对象属性，因此self.element 必须是在__init__和具体的方法中使用

    # 如何自定义装饰器
    # 一般装饰器都不被外界调用，因此设置为私有方法
    def __zhuangshiqi(func):
        # 定义一个内部函数(装饰器)(其实就是定义一个函数，来形成这个装饰器，然后再装饰需要装饰的函数)
        def inner():
            print('内部...')
            return func

        return inner  # 返回inner()表示返回结果  返回inner表示返回函数引用

    def __zhuangshiqi1(func):
        pass

    # 使用自定义的装饰器
    @__zhuangshiqi1  # 嵌套装饰，取决代码逻辑谁在前和谁在后
    @__zhuangshiqi
    def function1(self):
        print('function1')
        return self     # 返回自身可以形成链式编程。
