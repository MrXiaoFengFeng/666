

# 什么是反射？
# 指的是在程序运行过程中，可以“动态（最终运行前）”获取对象的信息


# 为何要用反射？




# 如何实现反射
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f'{self.name},{self.age}')

obj = People('egon', 18)


# 实现反射机制的步骤
# 1、先通过dir：查看某一个对象下可以.出那些属性来
# print(dir(obj))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'say']
"""

# 2、可以通过字符串反射到真正的属性上，得到属性值
# print(obj.__dict__['name'])  # egon
# print(obj.__dict__[dir(obj)[-2]])  # egon


# 通过字符串操作内置属性
# 四个内置函数的使用
# 判断对象下有没有什么属性
# 1、hasattr()
# print(hasattr(obj, 'name'))  # True
# print(hasattr(obj, 'x'))  # False

# 获取对象的属性值
# 2、getattr()
# print(getattr(obj, 'name'))  # egon


# 修改对象属性值
# 3、setattr()
# setattr(obj, 'name', 'jojo') # obj.name = egon
# print(obj.name)  # jojo


# 4、delattr()
# print(obj.__dict__)   # {'name': 'egon', 'age': 18}
# delattr(obj, 'name')  # del obj.name
# print(obj.__dict__)  # {'age': 18}


# 操作类
# print(getattr(obj, 'say'))  # obj.say 对象：<bound method People.say of <__main__.People object at 0x000002964656FF10>>
# print(getattr(People, 'say'))  # People.say 函数：<function People.say at 0x0000019B5C7F0790>
