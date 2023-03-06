# x = yield 返回值
# 案例1：
# def dog(name):
#     print('道哥%s准备吃东西啦！'%name)
#     while True:
#         # x拿到的是yield接收到的值
#         x = yield # x=骨头，第二次x=肉包子
#         print('道哥%s吃了 %s'%(name,x))
#
# g = dog('tom')
# g.send(None) # 等同于next(g) 初始化yield
#
# g.send('骨头')
# g.send('肉包子')
# g.send(['馒头','饺子'])


# 结果
# 道哥tom吃了 骨头
# 道哥tom吃了 肉包子
# 道哥tom吃了 ['馒头', '饺子']


# g.close()
# g.send('222') # 关闭后就无法传值了StopIteration




# 案例2：
def dog(name):
    food_list = []
    print('道哥%s准备吃东西啦！'%name)
    while True:
        # x拿到的是yield接收到的值
        x = yield food_list  # x='骨头'
        print('道哥%s吃了 %s'%(name,x))
        food_list.append(x)

g = dog('tom')

res =g.send(None)
print(res)

res = g.send('骨头')
print('第1次后foodlist包含',res)
g.send('肉包子')
print('第2次后foodlist包含',res)
g.send('馒头')
print('第3次后foodlist包含',res)

#结果
# 道哥tom准备吃东西啦！
# []
# 道哥tom吃了 骨头
# 第1次后foodlist包含 ['骨头']
# 道哥tom吃了 肉包子
# 第2次后foodlist包含 ['骨头', '肉包子']
# 道哥tom吃了 馒头
# 第3次后foodlist包含 ['骨头', '肉包子', '馒头']


#
# def func():
#     print('start........')
#     x = yield 111
#     print('哈哈哈哈')
#     yield 2222
#
# g = func()
# res = g.send(None)
# print(res)
#
# res1 = next(g)
# # res1 = g.send('666')
# print(res1)
#
# # res2 = g.send('777')
# # print(res2)
