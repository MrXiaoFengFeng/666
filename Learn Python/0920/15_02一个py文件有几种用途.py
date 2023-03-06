#一个python文件有两种用途
# 1、被当成程序运行
# 2、被当做模块导入

import foo



# print(__name__) # __name__ = __main__
# #1.当foo.py被运行时，__name__的 值为'__main__'
# #2.当foo.py被当做模块导入时，__name__ = 'foo'
#
# if __name__ == '__main__':
#     print('文件被执行')
#     get()
#     change()
# else:
#     # 被当做模块导入时做的事情
#     print('文件被导入')
#     pass


# 编写一个规范的模块
#!/usr/bin/env python #通常只在类unix环境有效,作用是可以使用脚本名来执行，而无需直接调用解释器。

# "The module is used to..." #模块的文档描述
#
# import sys #导入模块
#
# x=1 #定义全局变量,如果非必须,则最好使用局部变量,这样可以提高代码的易维护性,并且可以节省内存提高性能
#
# class Foo: #定义类,并写好类的注释
#     'Class Foo is used to...'
#     pass
#
# def test(): #定义函数,并写好函数的注释
#     'Function test is used to…'
#     pass
#
# if __name__ == '__main__': #主程序
#     test() #在被当做脚本执行时,执行此处的代码