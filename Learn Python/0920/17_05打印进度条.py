# print('[%-50s]' %'#')

# 打印一个进度条
# import time
# res = ''
# for i in range(50):
#     res += '#'
#     time.sleep(0.2)
#     print('\r[%-50s]'%res,end='')


# 打印一个下载文件的进度条
# import time
#
# recv_size = 0
# total_size = 102500
#
# while recv_size < total_size:
#     time.sleep(0.02)  # 下载了1024个字节的数据
#     recv_size += 1024 #recv_size = 2048
#
#     # 打印进度条
#     persent = recv_size / total_size
#     if persent > 1:
#         persent = 1
#     res = int(50 * persent) * '#'
#     #一行进度条
#     print('\r下载进度为：[%-50s] %d%%'%(res,int(100 * persent)),end='')
#     #多行进度条
#     # print('\r下载进度为：[%-50s] %d%%'%(res,int(100 * persent)))


# 拆分为进度条功能：

import time
import sys

# def progress(persent):
#     if persent > 1:
#         persent = 1
#
#     res = int(50 * persent) * '#'
#     print('\r下载进度为：[%-50s] %d%%' % (res, int(100 * persent)), end='')
#将宽度也做成自定义
def progress(percent,width=50):
    if percent >= 1:
        percent=1
    show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
    print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')


recv_size = 0
total_size = 102500

while recv_size < total_size:
    time.sleep(0.02)  # 下载了1024个字节的数据
    recv_size += 1024  # recv_size = 2048

    # 打印进度条
    persent = recv_size / total_size  # 1024/102500

    # progress(persent)
    progress(persent,width=70)
