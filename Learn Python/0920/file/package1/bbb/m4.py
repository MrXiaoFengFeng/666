
#导入f1
# 绝对路径
# from package1.m1 import f1
#相对路径
from ..m1 import f1


#导入同级f5
# 绝对路径
# from package1.bbb.m5 import f5
#相对路径
from .m5 import f5

def f4():
    print('这是f4')
    f1()
    f5()