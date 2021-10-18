import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract
from time import sleep  # 休眠

"""
    设计模式之模版方法模式  
    1. 提取算法中不变的部分和变化的部分。不变的部分模版化，变化的部分交给子类实现
"""


# 定义算法的骨架，但算法的实现交给子类实现
class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):  # 原子操作
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # 模版方法，程序运行的框架，但细节未实现; 细节交给继承者实现
    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:  # 当关闭窗口时，程序中断(ctrl + c)
                break
        self.stop()


class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行...")

    def stop(self):
        print("窗口停止运行...")

    def repaint(self):
        print(self.msg)


window = MyWindow("hello...")
window.run()
