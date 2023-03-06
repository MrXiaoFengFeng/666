# 编写登陆接口
#
# 基础需求：
#
# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后退出程序
# 升级需求：
#
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

dic={
    'egon1':{'password':'123','count':0},
    'egon2':{'password':'123','count':0},
    'egon3':{'password':'123','count':0},

}


while True:
    name=input('username>>: ')

    if not name in dic:
        print('用户不存在')
        continue
    if dic[name]['count'] > 2:
        print('尝试次数过多,锁定')
        continue

    password=input('password>>: ')


    if password == dic[name]['password']:
        print('登录成功')
        break
    else:
        print('用户名或密码错误')
        dic[name]['count']+=1

# ============================================
#db.txt内容:egon1|egon2|
dic={
    'egon1':{'password':'123','count':0},
    'egon2':{'password':'123','count':0},
    'egon3':{'password':'123','count':0},
}

count=0
while True:
    name=input('u>>: ')
    if name not in dic:
        print('用户不存在')
        continue

    with open('db.txt','r') as f:
        lock_users=f.read().split('|')
        if name  in lock_users:
            print('用户%s已经被锁定' %name)
            break

    if dic[name]['count'] > 2:
        print('尝试次数过多,锁定')
        with open('db.txt','a') as f:
            f.write('%s|' %name)
        break

    password=input('p>>: ')

    if password == dic[name]:
        print('登录成功')
        break
    else:
        print('用户名或密码错误')
        dic[name]['count']+=1