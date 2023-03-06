# 精髓：可以把函数当成变量取用
# func=内存地址

def func():
    print('from func')


# 1.可以赋值
# f = func
# print(f,func)
# f()

# 2.可以当做函数的参数传入
# def foo(x): # x = func 的内存地址
#     # print(x)
#     x()
# foo(func) # foo(func的内存地址)
# #结果：from func


# 3.可以当做函数当做另外一个函数的返回值
# def foo(x): # x = func的内存地址
#     return x # return  func的内存地址
#
# res = foo(func) # foo(func的内存地址)
# print(res) # res = func的内存地址
# res()
# #结果：from func

# 4.了可以当做容器类型的一个元素
# l = [func,]
# print(l)
# l[0]()

# dic = {'k1':func}
# print(dic)
# dic['k1']()


def login():
    print('登录功能')


def transfer():
    print('转账功能')


def check_balance():
    print('查询余额')

def withdraw():
    print('提现')

# func_dic = {
#     '1':login,
#     '2':transfer,
#     '3':check_balance,
#     '4':withdraw
# }

# func_dic['1']()

func_dic = {
    '0':['退出',None],
    '1':['登录',login],
    '2':['转账',transfer],
    '3':['查看余额',check_balance],
    '4':['提现',withdraw]
}
while True:
    # print(
    #     '''
    #     0 退出
    #     1 登录
    #     2 转账
    #     3 查询余额
    #     4 提现
    #     '''
    # ) # 2.进一步优化提示语内部，不需要再变更此处文案，写到字典里
    for k in func_dic:
        print(k,func_dic[k][0])
    choice = input('请输入你的指令：').strip()
    if not choice.isdigit():
        print('必须输入编号')
        continue

    # if choice == '0':
    #     break

    # if choice == '1':
    #     login()
    #
    # if choice == '2':
    #     transfer()
    #
    # if choice == '3':
    #     check_balance()
    #
    # else:
    #     print('指令不存在')

    if choice in func_dic:   # 优化1，将选择改变成一个字典，for循环遍历取就行
        func_dic[choice][1]() # 优化2，调用字典内函数地址取值
    else:
        print('输入的指令不存在')