''''
1、包就是一个包含有__init__.py文件的文件夹

2、为何要有包
    包的本质是模块的一种形式，包是用来被当做模块导入

'''
# 1、产生一个名称空间
# 2、运行包下的__init__.py文件，将运行过程中产生的名字丢到1的名称空间中
# 3、在当前执行文件的名称空间中拿到一个名字mmm，mmm指向1的名称空间
#

#此为模块的使用者，调用E:\WorkSpace\Learn Python\0920\file\package1

import sys
# 模块使用者需要将模块所在的文件夹目录添加到环境变量中
sys.path.append(r'E:\WorkSpace\Learn Python\0920\file')
# #import
import package1  # package1下的__init__.py

# package1.f1()
# package1.f2()
# package1.f3()
package1.f4()








#from...import
# from package1 import f1
# from package1 import f2
# from package1 import f3
# from package1 import f4  # package1内有f4
#
# f1()
# f2()
# f3()
# f4()




# 强调：
# 1.关于包相关的导入语句也分为import和from ... import ...两种，但是无论哪种，无论在什么位置，在导入时都必须遵循一个原则：凡是在导入时带点的，点的左边都必须是一个包，否则非法。可以带有一连串的点，如import 顶级包.子包.子模块,但都必须遵循这个原则。但对于导入后，在使用时就没有这种限制了，点的左边可以是包,模块，函数，类(它们都可以用点的方式调用自己的属性)。
#
# 2、包A和包B下有同名模块也不会冲突，如A.a与B.a来自俩个命名空间
# 3、import导入文件时，产生名称空间中的名字来源于文件，import 包，产生的名称空间的名字同样来源于文件，即包下的__init__.py，导入包本质就是在导入该文件


