import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

"""
    设计模式之观察者模式
    定义对象之间的一对多的依赖关系。当一个对象的状态发生变化时，所有依赖它的对象都得到通知并被自动更新。 观察者模式又称为"发布-订阅"模式。
    1. 要求又通知功能
    2. 要求松耦合，代码中不耦合，运行时耦合
    
    当发布者的信息更新时，所有观察者的信息都会自动进行更新。
"""


# 抽象观察者
class Observer(metaclass=ABCMeta):
    # 一旦发布者更新了信息，观察者就需要更新自己的信息
    @abstractmethod
    def update(self, notice):  # notice 应该是一个发布者
        pass


# 抽象发布者
class Notice:
    # 发布者和订阅者松耦合
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)


# 具体的发布者
class StaffNotice(Notice):
    def __init__(self, company_info=None):
        # super.__init__()  错误，而是super().__init__() 。
        # 否则会报错: TypeError: descriptor '__init__' of 'super' object needs an argument
        super().__init__()
        self.__company_info = company_info  # 将成员做成私有(在属性前加__)

    @property  # 装饰器   针对类外无法访问私有成员。 负责读取
    def company_info(self):
        return self.__company_info

    @company_info.setter  # 装饰器  针对私有成员的写入
    def company_info(self, info):
        self.__company_info = info
        self.notify()


# 具体的订阅者
class Staff(Observer):
    def __init__(self):
        # 当发布者发布信息后，订阅者需要缓存到本地
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


# 对于高层代码来看，只需要attach对象，而不需要主动去推送。而是在更新内容时，自动更新。
notice = StaffNotice()
s1 = Staff()
s2 = Staff()
notice.attach(s1)   # 当运行时，才能发布者才能知道观察者是谁。因此是弱耦合。
notice.attach(s2)
notice.company_info = "初始公司信息!"
print(s1.company_info)
notice.company_info = "公司赚钱拉，发钱!"
print(s1.company_info)
