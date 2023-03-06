# 一: 绑定方法：特殊之处在于将调用者本身当做第一个参数自动传入
#     1、绑定给对象的方法：调用者是对象，自动传入的是对象
#     2、绑定给类的方法：调用者类，自动传入的是类

# 方式1（笨办法）：
# class Mysql:
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
#     def func(self):
#         print(f'{self.ip} : {self.port}')
#
# obj1 = Mysql('1.1.1.1', 3306)
# obj1.func()
#
# obj2 = Mysql('10.10.10.10', 3309)
# obj2.func()

# 方式2：ip和端口都在文件中取
# import settings
#
# class Mysql:
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
#     def func(self):
#         print(f'{self.ip} : {self.port}')
#
#     @classmethod
#     def from_conf(cls):
#         return cls(settings.IP, settings.PORT)
#
# # obj1 = Mysql('1.1.1.1', 3306)
# # obj1.func()
# #
# # obj2 = Mysql('10.10.10.10', 3309)
# # obj2.func()
#
# obj3 = Mysql.from_conf()
# print(obj3.__dict__)  # {'ip': '127.0.0.1', 'port': 3306}



# 二、非绑定方法——》静态方法：staticmethod
#         没有绑定给任何人：调用者可是是类、对象，没有自动传参

class Mysql:
    def __init__(self, ip, port):
        self.nid = self.create_id()  # 每创建一个对象就生成一个id
        self.ip = ip
        self.port = port


    @staticmethod  # 将下述函数装饰城一个静态方法
    # def create_id(x, y, z):
        # print(x, y, z)
    def create_id():
        import uuid
        return uuid.uuid4()


    @classmethod
    def f1(cls):
        pass


    def f2(self):
        pass


obj1 = Mysql('1.1.1.1', 3306)
# Mysql.create_id(1, 2, 3)  # 1 2 3
# obj1.create_id(4, 5, 6)  # 4 5 6


# 非绑定
print(Mysql.create_id)  # <function Mysql.create_id at 0x000001D43EB8B550>
print(obj1.create_id)  # <function Mysql.create_id at 0x000001FA5B90B550>


# 绑定类
print(Mysql.f1)  # <bound method Mysql.f1 of <class '__main__.Mysql'>>
# 绑定对象
print(obj1.f2)  # <bound method Mysql.f2 of <__main__.Mysql object at 0x000002327B297F10>>