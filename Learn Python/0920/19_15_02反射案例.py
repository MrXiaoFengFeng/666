
# obj = 10
# if hasattr(obj, 'x'):
#     print(getattr(obj, 'x'))
# else:
#     pass

# 如果能获取到对象的属性，则返回x的属性值，默认返回是None
# print(getattr(obj, 'x', None))  # None

# if hasattr(obj, 'x'):
#     setattr(obj, 'x', 11111)  # 10.x = 11111
# else:
#     pass



class Ftp:
    def put(self):
        print('正在执行上传功能')

    def get(self):
        print('正在执行下载功能')

    def interactive(self):
        method = input('>>:').strip()  # method = 'put'
        if hasattr(self, method):
            getattr(self, method)()
        else:
            print('输入的指令不存在')


obj = Ftp()
obj.x = 10  # 给自定义类可以添加属性，给内置的不行例如：obj1.xxx = 11
print(obj.__dict__)
obj.interactive()
