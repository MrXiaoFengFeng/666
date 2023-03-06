#两数比大小
def max2(x,y):
    if x > y:
        return x
    else:
        return y
res = max2(1,2)
print(res)

#三元表达式
#语法格式：条件成立时返回的值 if 条件 else  条件不成立时返回的值
# x = 1
# y = 2
#
# res = x if x > y else y
#
# print(res) # 2

res = 666 if 'egon' == 'egon' else 777
print(res) # 666