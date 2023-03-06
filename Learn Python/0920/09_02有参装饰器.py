

#@用法：只要碰到@语法，@会将后面的内存地址加括号调用：print()，
# 且将下面的函数当参数传入print(home)，将返回值返给home,home = print(home)

# @print  # home = print(home)
# def home(a,b,c):
#     pass
#
# print(home)



# @print('hello')  #相当于@None--》None(home)
# def home(a,b,c):
#     pass
#
# print(home)  #TypeError: 'NoneType' object is not callable


# res = print('hello')
# print(res)  #None


from functools import wraps