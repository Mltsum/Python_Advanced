import os
import sys

'''
说明: 变化发现的结果

'''


class DiscoverAlgorithmsResult:
    def __init__(self, detectionResult=None, ClassifyResult=None, SampleResult=None, MultitaskResult=None):
        self.detectionResult = detectionResult
        self.ClassifyResult = ClassifyResult
        self.SampleResult = SampleResult
        self.MultitaskResult = MultitaskResult

        self.total_time_cost = 0

    def __str__(self):
        return "算法总耗时为:%d" % self.total_time_cost
