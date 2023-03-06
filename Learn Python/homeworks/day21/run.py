import sys
import os
print(sys.argv)
'''
# sys.argv获取的是解释器后参数值
"D:\Program Files (x86)\Python\python.exe" "E:/WorkSpace/Learn Python/homeworks/day21/run.py"
['E:/WorkSpace/Learn Python/homeworks/day21/run.py']
'''

# 判断文件夹的路径是否存在
if sys.argv[1]:
    # 获取需要检测的文件夹路径
    dir_path = sys.argv[1]
    print(dir_path)

    # 判断文件夹路径是否存在
    if os.path.isdir(dir_path):

        # 获取文件的大小
        file_size = os.path.getsize(dir_path)
        print(f'查看文件夹路径为:{dir_path} 大小为:{file_size}')

