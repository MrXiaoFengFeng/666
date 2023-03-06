#一.*****定义函数*****
# 函数的使用必须遵循[先定义，后调用]的原则。
# 函数的定义就相当于事先将函数体代码保存起来，然后将内存地址赋值个函数名，
#     函数名就是对这段代码的引用，这和变量的定义是相似的。
# 没有事先定义函数而直接调用，就相当于在引用一个不存在的变量名。

# 定义函数的语法：
# def 函数名(参数1,参数2,...):
#     '''文档描述'''
#     函数体
#     return 值
# 结构描述
# 1.def:定义函数的关键字
# 2.函数名:函数名指向函数内存地址，是对函数体代码的引用。函数的命名应该反映出函数的功能
# 3.括号:括号要加冒号，然后再下一行开始缩进编写函数体的代码
# 4.冒号:括号后要加冒号，然后再下一行开始缩进编写函数体的代码
# 5.'''文档描述''':描述函数功能，参数介绍等信息的文档，非必要，但是建议加上，从而增强函数的可读性
# 6.函数体:由语句和表达式组成
# 7.return值:定义函数的返回值，return是可有可无的

# =========================================
#形式1：无参函数
# def func():
#     print('哈哈哈哈')
#     print('哈哈哈哈')
# func()

#定义函数发生的事情
# 1.申请内存空间保存函数体代码
# 2.将上述内存地址绑定给函数名
# 3.定义函数不会执行函数体代码，但是会检测函数体的语法

#调用函数发生的事情
# 1.通过函数名找到函数的内存地址
# 2.然后通过加括号就是在触发函数体代码的执行
# print(func)  #<function func at 0x0000021102A1F160>返回内存地址
# func() #哈哈哈哈 哈哈哈哈


#示范1：
# def bar(): #bar=函数的内存地址
#     print('from bar')

# def foo():
#     print(bar) #<function bar at 0x0000016E3196F160>指向bar 内存地址
#     bar() #from bar调用bar()函数
#     print('from foo')
#
# foo()

#示范2：
#定义函数不会执行函数体代码，只检测函数体的语法
# def foo():
#     print(bar) #<function bar at 0x0000016E3196F160>指向bar 内存地址
#     bar() #from bar调用bar()函数
#     print('from foo')
#
# def bar(): #bar=函数的内存地址
#     print('from bar')
#
# foo() #from foo调用foo()函数
# bar()并不会报错，因为没有语法错误，当调用foo()时，bar()已经被扔进内存了
#=》from bar
# from foo



# --------------------------
# 形式2：有参函数
# def func(x,y): #x=1 y=2
#     print(x,y)
# func(1,2) #1 2
#


# ----------------------------
# 形式3：空函数，函数体代码为pass
# def func(x,y):
#     pass


# 三种定义方式分别用在何处
# 1.无参函数的应用场景
# def interactive():
#     name = input('username>:')
#     age = input('age>:')
#     gender = input('gender>:')
#     msg = f'名字{name},年龄{age},性别{gender}'
#     print(msg)
#
# interactive()


#2.有参函数的应用场景
#加法运算
# def add():
#     x = 10
#     y = 20
#     res = x+y
#     print(res)  #如果这个函数以后不需要被别的程序调用，则参数可以写在代码体内

# def add(x,y): #参数-》原材料
#
#     res = x+y
#     return res #返回值-》产品
#
#      #print(res)
# # add(10,20) #如果函数需要被调用，则把参数写在括号内，调用函数的时候给参数传值
# res = add(1,2)
# print(res)

#3.空参函数的应用场景，构思程序结构
# def add()
#     '''加法'''
#     pass
# def minus()
#     '''减法'''
#     pass




#二.****************调用函数*************
# 1.语句的形式：只加括号调用函数
# add()
# add(1,2)


# 2.表达形式：
# def add(x,y):
#     res = x +y
#     return res
# # 赋值表达式
# res = add(1,2)
# print(res)
#
# #数学表达式
# res = add(1,2)*10
# print(res)
#
#
# #3.函数调用可以当做参数
# res = add(add(1,2),10)
# print(res)



#三、********************函数返回值********************
# return是函数结束的标志，即函数体代码一旦运行到return，
# 会立刻终止函数的运行，并且会将return后的值当做本次运行的结果返回
# 1.返回None:函数体内没有return,则return None
# def func():
#     return
# res = func()
# print(res)  #None

# 2.返回一个值：return 值
# def func():
#     return 10
# res = func()
# print(res) #10


#3.返回多个值：用逗号分隔开对个值，会被return返回成元组
def func():
    return 10,'aa',[2,3]
res = func()
print(res,type(res))  #(10, 'aa', [2, 3])