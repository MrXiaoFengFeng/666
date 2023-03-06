print('模块foo==》》')
x = 1


def get():
    print(x)


def change():
    global x
    x = 0
    print('change后的x值为：',x)

__all__ =['x','change','get'] # __all__控制*代表的名字有哪些
# print(__name__) # __name__ = __main__
# #1.当foo.py被运行时，__name__的 值为'__main__'
# #2.当foo.py被当做模块导入时，__name__ = 'foo'
#
# if __name__ == '__main__':
#     print('文件被执行')
#     get()
#     change()
# else:
#     # 被当做模块导入时做的事情
#     print('文件被导入')
#     pass

if __name__ == '__main__':
    get()
    change()
