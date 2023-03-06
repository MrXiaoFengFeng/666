
# 单继承背景下的属性查找
# 示范1：
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1()  # obj.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj = Bar()
# #先从对象本身找，没找到去父类找，self指对象本身
# obj.f2()
#
# # Foo.f2
# # Bar.f1


# 示范2，就想访问父类中的f1：
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         Foo.f1(self)  # 调用当前类的f1
#
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj = Bar()
# #先从对象本身找，没找到去父类找，self指对象本身
# obj.f2()
#
# # Foo.f2
# # Foo.f1


# 示范3，就想访问父类中的f1：
class Foo:
    def __f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.__f1()   # self._Foo__f1


class Bar(Foo):
    def f1(self):
        print('Bar.f1')

obj = Bar()
#先从对象本身找，没找到去父类找，self指对象本身
obj.f2()

# Foo.f2
# Foo.f1