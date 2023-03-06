import os
import sys

sys.path.append(
    os.path.abspath(__file__)
)

from core import src


print(__name__)
if __name__ == '__main__':
    src.run()
