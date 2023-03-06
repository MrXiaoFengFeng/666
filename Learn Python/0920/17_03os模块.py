encoding:'utf-8'
import os


#获取某一个文件夹下所有的子文件及子文件夹的名字
# res = os.listdir('.')
# print(res)
#
# #os.path.getsize获取文件大小
# size = os.path.getsize(r'E:\WorkSpace\Learn Python\0920')
# print(size)


# os.system运行系统命令,相当于运行应用程序
# os.system(r'dir C:\\a')
# os.system('ls /')


# 向系统环境变量中增加一个键对值规定：key与value必须都是字符串,值为一个字典
print(os.environ)
#
# os.environ['aaaaaaaaa'] = '1111'
# print(os.environ)

#返回当前文件的绝对路径,
# print(os.path.abspath(__file__))  # E:\WorkSpace\Learn Python\0920\17_03os模块.py
# os.path.abspath会将地址转成符合平台需求的\样式
# print(__file__)  # E:\WorkSpace\Learn Python\0920\17_03os模块.py

#了解。。。
# os.path.split(path)->将path分割成目录和文件名二元组返回
# res = os.path.split(r'C:\\a\\b\\c\\d.txt')
# print(res)  # ('C:\\\\a\\\\b\\\\c', 'd.txt')
#
# # 获取文件夹名：
# print(os.path.dirname(r'C:\\a\\b\\c\\d.txt'))  # C:\\a\\b\\c
# #获取文件名
# print(os.path.basename(r'C:\\a\\b\\c\\d.txt'))  # d.txt


# 了解。。。如果path是绝对路径，返回True
# print(os.path.isabs(r'C:\\a\\b\\c\\d.txt'))  # True

# 如果path是一个存在的文件，返回True。否则返回False
# print(os.path.isfile(r'a.txt'))  # False
# # 如果path 是一个存在的目录，则返回True。否则返回False
# print(os.path.isdir(r'E:\WorkSpace\Learn Python\0920\file'))  # True

# windows 以盘符+：为起点，前面的忽略
# print(os.path.join('a','C:''b','c'))  # C:b\c
# # windows 以/为起点，前面的忽略
# print(os.path.join('a','/:''b','c'))  # /:b\c


# ----------------路径拼接----------------
# python3.5之后推出了一个新的模块pathlib
#
# from pathlib import Path
# # res = Path(__file__)  # E:\WorkSpace\Learn Python\0920\17_03os模块.py
#
# # res = Path(__file__).parent.parent
# # print(res)  # E:\WorkSpace\Learn Python
#
# res = Path('/a/b\\c') / 'd/e.txt'
# print(res)   # \a\b\c\d\e.txt  自动拼接
#
# print(res.resolve())  # E:\a\b\c\d\e.txt  自动处理\\为适合的平台展示