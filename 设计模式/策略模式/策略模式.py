import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

"""
    设计模式之策略模式 
    定义一系列的算法，将算法封装，是的他们可以相互替换，本模式使得算法可以独立于客户端变化而变化
    实际上变化发现算法SD/HD的不同策略应该进行策略模式的封装。 否则逻辑很乱。
"""


# 抽象策略
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


# 不同的算法策略
class FastStrategy(Strategy):
    def execute(self, data):
        print("用快速方式处理%s" % data)


# 用比较慢的方式处理
class SlowStrategy(Strategy):
    def execute(self, data):
        print("用慢速方式处理%s" % data)


# 上下文类: 将切换操作封装起来,不需要用户处理
class Context:
    def __init__(self, strategy, data):     # 核心是不同算法的抽象接口，这个接口方便了上下文的不同切换。
        self.strategy = strategy
        self.data = data

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


# 客户端代码
# 用户需要知晓不同策略的长处和短处。
data = "[...]"
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()
