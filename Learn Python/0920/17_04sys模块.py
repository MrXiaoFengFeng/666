# import sys

# python 3.8  run.py 1 2 3
# sys.argv获取的是解释器后参数值
#
# print(sys.argv)  # 返回列表['run.py','1','2','3']


# ----------------------------------------------
# 文件复制功能
# run.py

import sys

# src_file = input('源文件路径：').strip()
# dst_file = input('目标文件路径：').strip()

src_file = sys.argv[1]
dst_file = sys.argv[2]
print(sys.argv)  # ['E:\\WorkSpace\\Learn Python\\0920\\17_04sys模块.py', 'E:\\a.txt', 'E:\\b.txt']
with open(r'%s ' % src_file, mode='rb') as read_f, \
        open(r'%s ' % dst_file, mode='wb') as write_f:
    for line in read_f:
        write_f.write(line)

# cmd运行：
# python "E:\WorkSpace\Learn Python\0920\17_04sys模块.py" E:\a.txt E:\b.txt
