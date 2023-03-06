# 绝对导入,以包的文件夹作为起始来进行导入

# import sys
# print('----------这是init的sys.path')
# print(sys.path)

# from package1.m1 import f1
# from package1.m2 import f2
# from package1.m3 import f3
#
# from package1.bbb.m4 import f4  # package1内有了f4
#
#


#相对导入:仅限于包内使用，不能跨出包
#.代表当前文件夹
#..代表上一层文件夹
import sys
from .m1 import f1
from .m2 import f2
from .m3 import f3
from .bbb.m4 import f4


# import...
# 强调：
# 1、相对导入不能跨出包，所以相对导入仅限于包内模块间互相调用

#而绝对导入是没有任何限制的，所以绝对导入是一种通用的导入方式