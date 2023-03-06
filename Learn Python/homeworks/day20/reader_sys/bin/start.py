'''
项目启动入口
'''

import os
import sys

# 将项目的根目录，添加到sys.path中
sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)

# print(__file__)
from core import src


if __name__ == '__main__':
    src.run()