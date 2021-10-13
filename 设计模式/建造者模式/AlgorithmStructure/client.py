import os
import sys

from DiscoverAlgorithmsImpl import DiscoverAlgorithmsImpl   # python中引入包是 from file import class
from Master import Master

if __name__ == '__main__':
    # 客户端代码
    # 1. 实现各个自模块的方法
    builder_way1 = DiscoverAlgorithmsImpl()

    # 2. 采用调用顺序1实现变化发现算法
    master = Master()

    result = master.runningWithOrder2(builder_way1)

    print(result)
