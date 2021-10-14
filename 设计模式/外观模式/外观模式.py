import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

"""
    设计模式之外观模式
"""


# 设置抽象类
class Module(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class CPU(Module):
    def run(self):
        print("CPU开始运行")

    def stop(self):
        print("CPU停止运行")


class Disk(Module):
    def run(self):
        print("硬盘开始运行")

    def stop(self):
        print("硬盘运行")


class Memory(Module):
    def run(self):
        print("内存上电")

    def stop(self):
        print("内存下电")

# 外观模式实现
class Computer(Module):
    # 1. 高层模块需要灵活调度子系统
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# 客户端
# 1. 用户无需知道底层模块的调用，相当于隔离了调用层和模块层， 避免调用出现错误。提高安全性
# 2. 好处是解耦。
computer = Computer()
computer.run()
computer.stop()
