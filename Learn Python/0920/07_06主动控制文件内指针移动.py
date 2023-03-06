

#指针移动的单位都是以bytes/字节为单位
#只有一种情况特殊：
    # t模式下的read(n),n代表的是字符的个数

# with open(r'file/j.txt',mode='rt',encoding='utf-8') as f:
# with open(r'file/j.txt',mode='rt',encoding='utf-8') as f:
#     res = f.read(4)
#     print(res)  #abc你(4个字符)

#================================
# f.seek(n,模式):n指的是指针的移动的bytes(字节)个数
#模式：
# 文件内容：abc你好
#0:参照物是文件的开头位置
# f.seek(9,0)
# f.seek(3,0)
#
# #1:参照物是当前指针所在的位置
# f.seek(9,1) #默认打开为文件指针在开头，指针移9个bytes
# f.seek(3,1) #再往后移三个就是12bytes
#
# #2:参照物是文件末尾位置，应该是倒着移动
# f.seek(-9,2)  #默认打开文件指针在文件末尾，倒着移9个bytes，即到了文章开头,0bytes
# f.seek(-3,2)  #默认打开文件指针在文件末尾，倒着移3个bytes,读取指针后面的值。bytes=6，结果为好

#只有0模式可以在t、b下使用，1和2必须在b模式下用
# f.tell() #获取文件指针当前的位置
#abc你好
# with open(r'file/j.txt',mode='rt',encoding='utf-8') as f:
#
#     f.seek(9,0)
#     f.seek(3,0)  #参照文件开头移动了3个字节
#     print(f.tell()) #查看当前文件指针距离开头的位置，输出结果为3
#     res = f.read() #从第三个字节的位置读到文件末尾，输出结果为：你好
#     print(res)
    #注意，由于在t模式下，会将读取的内容自动解码，所以必须保证读取的内容是一个完整中文书籍，否则解码失败

# with open(r'file/j.txt',mode='rb') as f:
#     f.seek(-9,2)
#     print(f.tell()) #0
#     f.seek(-3,2)
#     print(f.tell()) #6
#     print(f.read().decode('utf-8')) #输出结果为：好  #1个中文=3个bytes

