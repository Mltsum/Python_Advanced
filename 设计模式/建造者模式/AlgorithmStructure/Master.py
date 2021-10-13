import os
import sys
from DiscoverAlgorithmsBuilder import DiscoverAlgorithmsBuilder


# 设置工程师，来确定算法执行的顺序
# 假设一个任务有10张图，可能的执行顺序如下
class Master:
    def __init__(self, number=10):
        self.task_pic_number = number

    def runningWithOrder1(self, builder):
        for i in range(self.task_pic_number):
            print("执行图%d:" % i)
            builder.detection_builder()
            builder.classify_builder()
            builder.samples_builder()
            builder.multitask_builder()
        return builder.result  # 可以直接从类中引入属性，即便没有定义，也可以在运行中检查

    def runningWithOrder2(self, builder):
        for i in range(self.task_pic_number):
            print("执行图%d:" % i)
            builder.detection_builder()
            builder.samples_builder()
            builder.multitask_builder()

        for i in range(self.task_pic_number):
            print("执行图%d的分类:" % i)
            builder.classify_builder()
        return builder.result
