#以t模式为基础进行内存操作

#1.r(默认的操作模式)：只读模式，当文件不存在时报错，当文件存在时，文件指针跳到开始位置
# with open(r'file/c.txt',mode='rt',encoding='utf-8') as f:
#     print('第一次读'.center(20,'*'))
#     res = f.read() #把所有内容从硬盘读入内存
#     print(res)
#
#     print('第2次读'.center(20,'*'))
#     res1 = f.read() #把所有内容从硬盘读入内存
#     print(res1)

#2.w：只写模式，当文件不存在时会创建空文件，当文件存在会【清空】文件（重新以w打开也会清空），指针位于开始位置
# with open(r'file/d.txt',mode='wt',encoding='utf-8') as f:
#     # f.read() #报错不可读
#     res = f.write('你真棒啊！\n')

#3.a:只追加写，在文件不存在时会创建空文档，在文件存在时，指针会直接跳到文件有内容的末尾
# with open(r'file/e.txt', mode='at', encoding='utf-8') as f:
#
#     # f.read() #报错不可读
#     f.write('你真6啊1\n')
#     f.write('你真6啊2\n')
#     f.write('你真6啊3\n')
#     f.write('你真6啊4\n')

#强调w模式和a模式的异同：
# 相同点：在打开文件不关闭的情况下，连续的写入，新写的内容总会
# 跟在前些的内容之后。
# 不同点：以a模式重新打开文件，不会清空原文件内容，会将文件指针预启动到文件末尾

# #案例：
# a模式：用户注册
# username = input('请输入你的用户名：')
# password = input('请输入你的密码：')
# with open(r'file/db.txt',mode='at',encoding='utf-8') as f:
#     f.write(f'{username}:{password}\n')

# w模式：复制
# w模式案例
# raw_path = input('请输入原文件的路径：').strip()
#
# new_path = input('请输入要储存复制文件的位置：').strip()
#
# with open(rf'{raw_path}',mode='rt',encoding='utf-8') as f1,\
#         open(f'{new_path}',mode='wt',encoding='utf-8') as f2:
#     res = f1.read()
#     f2.write(res)
# with open(r'{}'.format(raw_path),mode='rt',encoding='utf-8') as f1,\
#         open(r'{}'.format(new_path),mode='wt',encoding='utf-8') as f2:
#     res = f1.read()
#     f2.write(res)

# ================================================
# #b模式：binary模式
# 1.读写都是以bytes为单位
# 2.可以针对所有文件
# 3.一定不能指定字符编码
# with open(r'file/b模式.mp4',mode='rb') as f:
#     res = f.read() #硬盘的二进制读入内存-》b模式下不做任何转换，直接读入内存
#     print(res) #bytes类型-》当成二进制

# with open(r'file/c.txt',mode='rb') as f:
#     res = f.read()
#     print(res,type(res)) #b'\xe5\x93\x88\xe5\x93\x88\xe5\x93\x88\xe5\x93\x88' <class 'bytes'>
#     print(res.decode()) #哈哈哈哈


#b模式应用案例1：
# with open(r'file/f.txt',mode='wb') as f:
#     f.write('你好啊哈哈哈哈hello'.encode('utf-8'))
#
#b模式应用案例2：复制拷贝工具
# raw_path = input('请输入原文件的路径：').strip()
# new_path = input('请输入要储存复制文件的位置：').strip()
#
# with open(rf'{raw_path}',mode='rb') as f1,\
#         open(f'{new_path}',mode='wb') as f2:
#     # res = f1.read() #内存占用过大
#     # f2.write(res)
#     for line in f1:
#         f2.write(line)


# 循环读取文件
#方式1：如果一行文件特别长，用while循环，自己控制每次读取的数据的数据量
# with open(r'file/test.jpg',mode='rb') as f:
#     while True:
#         res = f.read(1024)
#         # if len(res) == 0:
#         #     break #两个方式都可以
#         if not res:
#             break
#         print(len(res))

#方式2：以行位单位读，当一行内容过长时，会导致一次性读入内容数量过大
# with open(r'file/g.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         print(line,end='')

# with open(r'file/g.txt',mode='rb') as f:
#     for line in f:
#         print(line)

#其它文件操作：
# 读相关操作
f.read() #读取所有内容执行完该操作后明文件指针会移动到文件末尾
# 1.redline() #读取一行内容，光标移动到第二行首部
# with open(r'file/g.txt',mode='rt',encoding='utf-8') as f:
#     # res1 = f.readline() #一次读一行
#     # res2 = f.readline() #一次读一行
#     # print(res1,res2)
#     # while True: #while循环读取
#     #     line = f.readline()
#     #     if len(line) == 0:
#     #         break
#     #     print(line)
# #2.readlines() #读取每一行内容，存放于列表中。从当前位置开始，一次读很多行。文件数据量过大内存占用会过多导致内存溢出，慎用
#     res = f.readlines()
#     print(res) #['11\n', '2222\n', '3333\n', '444\n', '5555']

#2.写相关操作
# f.writelines()
# with open(r'file/h.txt', mode='wb') as f:
#     #纯英文或者数字，可以这加前缀b得到bytes
#     l = [b'111asss\n',
#          b'222\n',
#          b'33376',
#          b'444456\n',
#          '你好'.encode('utf-8'),
#          bytes('真的',encoding ='utf-8'),#bytes('你好'，encoding ='utf-8')
#          bytes('超级好',encoding ='utf-8')]
#     f.writelines(l)

#3.f.flush() 立即写入上面的内容
with open(r'file/h.txt',mode='wt',encoding='utf-8') as f:
    f.write('wefdsfsdhhhh哈哈哈')
    f.flush()

