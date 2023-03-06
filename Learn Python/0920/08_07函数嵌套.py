# 一、函数嵌套
# 1.函数的嵌套调用：在调用一个函数的过程中又调用其他函数

# 案例：取出最大值

# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
# def max4(a,b,c,d):
#     #1.比较ab，得到最大值res1
#     res1 = max2(a,b)
#
#     #2.将res1和c比较，得到最大值res2
#     res2 = max2(res1,c)
#
#     #3.将res2和d比较，得到最大值res3
#     res3 = max2(res2,d)
#
#     #4.返回res3
#     return res3
#
# res = max4(3,4,9,5)
# print(res)


# 二、函数的嵌套定义：在函数内定义其他函数

# def f1():
#     def f2():
#         pass


# 和圆形相关的计算（求圆形的周长或面积）

def circle(radius, action=0):
    from math import pi

    # 求圆形的周长
    def perimiter(radius):
        return 2 * pi * radius

    # 求圆形的面积
    def area(radiud):
        return pi * (radiud ** 2)

    if action == 0:
        return perimiter(radius)

    elif action == 1:
        return area(radius)


res = circle(20, action=1)
print(res)
