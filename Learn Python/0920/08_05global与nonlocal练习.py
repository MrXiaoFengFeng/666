#题目1：
# input = 333
# def func():
#     input = 444
# func()
# print(input) # 333

#题目2：
# def func():
#     print(x) # 111
# x = 111
# func()

#题目3：
# x = 1
# def func():
#     print(x) # 333 333在1后赋值，所以为333
#
# def foo():
#     x = 222
#     func()
# x = 333
# foo()


#题目4：
# input = 111
# def f1():
#     def f2():
#         print(input) # 222
#     input = 222
#
#     f2()
# input = 333
#
# f1()

#题目5：
# x = 111
# def func():
#     print(x) #报错，x=222需要在打印前面，先定义后调用
#     x = 222
#
# func()