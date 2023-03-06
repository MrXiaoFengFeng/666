# 关系运算
# 有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
# pythons = {'xiaohua', 'egon', 'mimi', 'gangdan', 'biubiu'}
# linuxs = {'mimi', 'xiaohei', 'gangdan'}
# 1.
# 求出即报名python又报名linux课程的学员名字集合
# 2.
# 求出所有报名的学生名字集合
# 3.
# 求出只报名python课程的学员名字
# 4.
# 求出没有同时这两门课程的学员名字集合


'''
# 答案
# 求出即报名python又报名linux课程的学员名字集合
print(pythons & linuxs)
# 求出所有报名的学生名字集合
print(pythons | linuxs)
# 求出只报名python课程的学员名字
print(pythons - linuxs)
# 求出没有同时这两门课程的学员名字集合
print(pythons ^ linuxs)
'''