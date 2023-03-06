#无论是import还是from...import在导入模块是都涉及到查找问题
#优先级：
# 1、内存（内置模块）
# 2、从硬盘找

# import sys
# #值为一个列表，存放了一系列的文件夹
# #其中第一个文件夹是当前执行文件所在的文件夹
#
#
# print(sys.path) # E:\\WorkSpace\\Learn Python\\0920'




#了解：sys.modules查看已经加载到内存中的模块
# import sys
# import  模块foo
# print(sys.modules)




#从硬盘中找文件
import sys
#找foo.py就把foo.py的文件夹临时添加到环境变量中
sys.path.append(r'E:\WorkSpace\Learn Python\0920\file')

# import foo
# foo.get()


from foo import get
sys.path.append(r'E:\WorkSpace\Learn Python\0920\file')
get()