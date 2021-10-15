import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

"""
    设计模式之责任链模式
    使得多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连接成一条链，并沿着链传递该请求，直到有一个对象处理它位置。
"""

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self,day):
        pass


class GeneralManager(Handler):

    def handle_leave(self,day):
        if day < 10:
            print(f"总经理准假{day}天")
        else:
            print("总经理认为你请假太久了，你还是辞职吧")

class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self,day):
        if day < 5:
            print(f"部门经理准假{day}天")
        else:
            print("部门经理权限不足, 应总经理审批，流程转向总经理...")
            self.next.handle_leave(day)


class ProjectManager(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self,day):
        if day < 3:
            print(f"项目主管准假{day}天")
        else:
            print("项目主管权限不足, 应部门经理审批，流程转向部门经理...")
            self.next.handle_leave(day)



# 客户端
# 优点是降低耦合度，高层代码不需要直到后面的流程，只需要关注项目主管类即可。
day = 4
h = ProjectManager()
h.handle_leave(10)


# 举例: 将算法流程设计为链表, 也可以设计为双链表等

class Module(metaclass=ABCMeta):
    @abstractmethod
    def running(self):
        pass


class Detect(Module):
    def __init__(self):
        self.next = Classify()
    def running(self):
        print("检测运行中...")
        self.next.running()


class Classify(Module):
    def __init__(self):
        self.next = MultiTask()

    def running(self):
        print("分类运行中...")
        self.next.running()


class MultiTask(Module):
    def __init__(self):
        self.next = LaneTask()

    def running(self):
        print("多任务运行中...")
        self.next.running()


class LaneTask(Module):
    def __init__(self):
        self.next = SampleTask()

    def running(self):
        print("车道线模块运行中...")
        self.next.running()


class SampleTask(Module):
    def running(self):
        print("采样模块运行中...")

# 客户端代码
r = Detect()
r.running()
