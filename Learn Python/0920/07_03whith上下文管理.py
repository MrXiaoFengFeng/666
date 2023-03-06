

# with open(r'file/a.txt', mode='rt') as f1,\
#         open(r'file/b.txt', mode='rt') as f2:
#     res1 = f1.read()
#     res2 = f2.read()
#     print(res1,res2) ##没读取到内容，因为光标换行了

inp_username = input('请输入你的账号：')
inp_password = input('请输入你的密码：')
#
# with open(r'file/user.txt',mode='rt',encoding='utf-8') as f:
#     res = f.read()
#     print(res)
#     username,password = res.split(':')
#
# if inp_username == username and inp_password == password:
#     print('登录成功')
# else:
#     print('账号或密码错误')

# 案例多行文字取值
with open(r'file/user.txt',mode='rt',encoding='utf-8') as f:
    for line in f:
        # print(line,end='')
        username,password = line.strip().split(':') #等同于line.strip('\n).split(':')
        if inp_username == username and inp_password == password:
            print('登录成功')
            break
    else:
        print('账号或密码错误')
