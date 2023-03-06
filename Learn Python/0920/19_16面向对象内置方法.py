# 1、什么是内置方法？
# 定义再类内部，以__开头并以__结尾的方法
# 特点：会在某种情况下自动触发执行


# 2、为何要用内置方法？
# 为了定制化我们的类or对象

# 3、如何使用内置方法
# __str__:在打印对象时，会自动触发。然后将返回值（必须是字符串类型）当做本次打印的结果输出
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         print('运行了')
#         # return 'hahhaha'
#         return f'<{self.name}, {self.age}>'
#
#
# obj = People('egon', 18)
#
# # 打印对象，自动触发执行
# # print(obj.__str__())
# print(obj)  # <egon, 18>

# obj1 = int(10)
# print(obj1)  # 内置的类的类型 10


# __del__:在清理对象前触发，会先执行该方法
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.x = open('a.txt', mode= 'w')
        # self.x = '占据的是操作系统资源'

    def __del__(self):
        # print('run...')
        # 发起系统调用，告诉操作系统挥手相关的系统资源
        self.x.close()


obj = People('egon', 18)
print('======>')
"""
======>
run...
结束运行程序后清理应用程序的资源。触发运行
"""