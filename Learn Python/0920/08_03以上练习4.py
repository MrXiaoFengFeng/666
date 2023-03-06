# 练习4：
# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。



def func1(seq):
    if len(seq) > 2:
        seq=seq[0:2]
    return seq
print(func1([1,2,3,4]))