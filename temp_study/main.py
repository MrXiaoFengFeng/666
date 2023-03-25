

import os
import sys
sys.path.append(r'E:\WorkSpace\temp_study\utils')
from utils import test1
from utils.http_client import HttpClient

test1.foo()
res = HttpClient()
print(res)