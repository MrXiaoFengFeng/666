#1.打开文件
# windows路径分隔符问题
# open('C:\a\b\d\d.txt') #\会转义
# 方法1(推荐)：
# open(r'C:\a\b\d\d.txt') #r不转义rawstring
# 方法2：
# open('C:/a/b/c/d.txt')
f = open(r'file/a.txt', mode='rt')
print(f)

#2.操作文件：读/写文件,应用程序对文件的读写请求都是在向操作系统发送系统调用，
# 然后有操作系统控制硬盘把输入读入内存、或者写入硬盘。

res = f.read()
print(res)

#3.关闭文件
f.close() #回收操作系统资源
# del f #回收应用程序资源，不用考虑。python自动回收