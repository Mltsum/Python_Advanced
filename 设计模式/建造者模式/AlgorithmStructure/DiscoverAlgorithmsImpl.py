import os
import sys
from abc import ABCMeta, abstractmethod
from DiscoverAlgorithmsBuilder import DiscoverAlgorithmsBuilder


# 用某种方式实现各个模块
class DiscoverAlgorithmsImpl(DiscoverAlgorithmsBuilder):
    def __init__(self):
        super(DiscoverAlgorithmsImpl, self).__init__()

    def detection_builder(self):
        print("调用检测算法")

    def classify_builder(self):
        print("调用分类算法")

    def samples_builder(self):
        print("调用采样算法")

    def multitask_builder(self):
        print("调用多任务算法")
