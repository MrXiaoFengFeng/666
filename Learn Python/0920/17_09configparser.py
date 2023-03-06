import configparser

config = configparser.ConfigParser()
config.read(r'E:\WorkSpace\Learn Python\0920\file\configparer1.ini')


#1.获取section
# print(config.sections())  # ['section1', 'section2']


#2.获取某一section下的所有的options
# print(config.options('section1'))  # ['k1', 'k2', 'user', 'age', 'is_admin', 'salary']


#3.获取items
# print(config.items('section1'))
# [('k1', 'v1'), ('k2', 'v2'), ('user', 'egon'), ('age', '18'), ('is_admin', 'true'), ('salary', '31')]

#4.获取指定值

res = config.get('section1','user')
print(res, type(res))  # egon <class 'str'>


res = config.getint('section1','age')  # getint自动将字符串初始化成init
print(res, type(res))  # 18 <class 'int'>


res = config.getboolean('section1','is_admin')  # getboolean自动将字符串初始化成布尔值
print(res, type(res))  # True <class 'bool'>


res = config.getfloat('section1','salary')  # getfloat自动将字符串初始化成浮点型
print(res, type(res))  #31.0 <class 'float'>