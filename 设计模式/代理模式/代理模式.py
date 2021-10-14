import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

"""
    设计模式之代理模式
    为对象提供一层代理以[控制对这个对象的访问]。
    场景
    1. 虚代理 : 根据[需要]创建[对象代理]
    2. 保护代理 : 控制对象的[访问权限]
"""


# 主体的接口
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self):
        pass


# 真实的对象
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r')
        print("读取文件内容...")
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w')
        f.write(content)
        f.close()


# 虚代理，目的是和Subject保持一致。
# 可提升性能
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            # 此时才会读取文件信息
            self.subj = RealSubject(self.filename)
            return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            return self.subj.set_content(content)


# 虚代理: 通过代理模式进行类的性能封装。
subj = VirtualProxy("notes")
print(subj.get_content())


# 保护代理
class ProtectProxy(Subject):
    def __init__(self, filename):  # __init__ 相当于C++中的构造函数
        self.filename = filename
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):  # 通过代理来控制对类的访问权限
        raise PermissionError("无写入权限")  # 抛出权限错误


subj1 = ProtectProxy("notes")
subj1.get_content()
subj1.set_content("xxx")
