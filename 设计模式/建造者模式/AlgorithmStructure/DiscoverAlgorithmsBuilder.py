import os
import sys
from DiscoverAlgorithmsResult import DiscoverAlgorithmsResult
from abc import abstractmethod, ABCMeta, ABC


# 算法中各个模块的算法实现，用于计算各个部件的结果
class DiscoverAlgorithmsBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.result = DiscoverAlgorithmsResult()

    @abstractmethod
    def detection_builder(self):
        """
        检测算法抽象
        :return: 检测算法结果
        """
        pass

    @abstractmethod
    def classify_builder(self):
        """
        分类算法抽象
        :return: 分类算法结果
        """
        pass

    @abstractmethod
    def samples_builder(self):
        """
        车道线采样点算法抽象
        :return: 采样结果值
        """
        pass

    @abstractmethod
    def multitask_builder(self):
        """
        多任务模型结果抽象
        :return: 多任务模型结果
        """
        pass
