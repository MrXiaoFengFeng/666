# hashlib模块
#什么是hash
    # hash一类算法，该算法接收传入的内容，经过运算得到一串hash值
# 1、hash值的特点：
# 用于文件完整性校验    # 1.1 只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
# 用于密码密文传输与验证 # 1.2 不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码
# 用于文件完整性校验    # 1.3 只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的



#2、hash的用途


# 3、如何用
#
# import hashlib
#
# m = hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# res = m.hexdigest()  # 'helloworld'
# print(res)  #fc5e038d38a57032085441e7fe7010b0
#
# #传入内容一样，取最终结果，hash值结果一样
# m = hashlib.md5('he'.encode('utf-8'))
# m.update('llo'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# res = m.hexdigest()  # 'helloworld'
# print(res)  #fc5e038d38a57032085441e7fe7010b0
#
#
#
# m.update(文件所有的内容)
# m.hexdigest()
#
#
# m.update(文件的一行)
# m.update(文件的一行)
# m.update(文件的一行)
# m.update(文件的一行)
# m.hexdigest()


# 加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。
# 所以，有必要对加密算法中添加自定义key再来做加密。

# 提升撞库成本：密码加盐

import hashlib
#在密码的指定位置加盐
m = hashlib.md5()
m.update('天王'.encode('utf-8'))
m.update('pass'.encode('utf-8'))
m.update('盖地'.encode('utf-8'))
m.update('word'.encode('utf-8'))
res = m.hexdigest()
print(res)