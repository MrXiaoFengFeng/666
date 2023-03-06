# 1.命名关键字参数（了解）
# 在定义函数时，*后定义的参数如下所示，称之为命名关键字参数
#特点：
#1.命名关键字实参必须按照key=value的形式为其传值
# 示例1：
# def func(x,y,*,a,b): #其中，a和b称之为命名关键字参数
#     print(x,y) #1 2
#     print(a,b) #dgdg 444
# func(1,2,a='dgdg',b=444)


# 示例2：
# def func(x,y,*,a=111,b): #其中，a和b称之为命名关键字参数，
#     # a=111相当于给a赋值，不存在位置形参需在关键字形参后面，前面带*相当于关键字参数
#     print(x,y) #1 2
#     print(a,b) #111 444
# func(1,2,b=444)

# 2.组合使用（了解）
#形参混用的顺序：位置形参，默认形参,*args,命名关键字形参，**kwargs
# def func(x,y=111,*args,z,**kwargs):
#     print(x)
#     print(y)
#     print(args)
#     print(z)
#     print(kwargs)

#实参混用的顺序：

def func(x,y,z,a,b,c):
    print(x)
    print(y)
    print(a)
    print(b)
    print(c)

func(111,*[333,444],a=222,**{'b':555,'c':666})
#结果： ==》解析：*[333,444]打散后是位置实参，需在关键字实参前面
#111
# 333
# 222
# 555
# 666