import random

# print(random.random())  #(0,1) 大于0且小于1之间的小数
#
# print(random.randint(1,3)) # [1,3] 开区间。头尾都能取到。大于等于1且小于等于3之间的证书
#
# print(random.randrange(1,3)) #[1,3) 前开后闭 大于等于1且小于3 的整数
#
#
# print(random.choice(1,'aaa',[2,3])) #1或aaa或[2,3]

# print(random.sample([1,'23',[4,5]],2))  # 列表元素任意2个组合

# print(random.uniform(1,5))  # 大于1小于5 的小数 1.5701574354427685

# list = [1,2,3,4,56,7]
# random.shuffle(list)  # shuffle 打乱列表内数据的顺序，相当于'洗牌'
# print(list)  # [56, 2, 7, 4, 1, 3]





#案例应用：随机验证码
# import random
# x12abc
#
#
# for i in range(6):
#     从26个大写字母随机取一个=chr(random.randint(65,90))
#     从10个数字中随机取一个=str(random.randint(0,9))
#     随机字符 = random.choice([字母+数字])
#     res += 随机字符


import random

def make_code(size = 4):  # size 控制验证码的长度
    res= ''
    for i in range(size):
        s1 = chr(random.randint(65,90))  #char(65,90)对应阿斯克码大写字母A~Z，随机取一个
        s2 =  str(random.randint(0,9)) # 因为要拼接，所以数字需要转化成str
        res += random.choice([s1,s2])
    return res

print(make_code(6))