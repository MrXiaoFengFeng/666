''' 2020-03-11 作业题
1、有列表['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量

2、用列表的insert与pop方法模拟队列


3. 用列表的insert与pop方法模拟堆栈

4、简单购物车,要求如下：
实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数以三元组形式加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　　
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}

5、有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中

即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}

6、统计s='hello alex alex say hello sb sb'中每个单词的个数
'''

# 1、有列表['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
# list = ['alex',49,[1900,3,18]]
# name,age,birth = list
# year,month,day14 = birth
# print(list,birth)

# 2、用列表的insert与pop方法模拟队列
# FIFO:先进先出
# list1 = []
# # 根据列表的索引的位置插入数据
# list1.insert(0,'我是第一个坦克')
# list1.insert(1,'我是第二个坦克')
# list1.insert(2,'我是第三个坦克')
# print(list1)  # ['我是第一个坦克', '我是第二个坦克', '我是第三个坦克']
# 数据开始出队列,取首个删除
# list1.pop(0)
# print(list1)
# list1.pop(0)
# print(list1)
# list1.pop(0)
# print(list1)


# 3. 用列表的insert与pop方法模拟堆栈
# 堆栈 ：LIFO, Last In First Out先进后出
# list1 = []
# # 根据列表的索引的位置插入数据
# list1.insert(0,'我是第一个坦克')
# list1.insert(1,'我是第二个坦克')
# list1.insert(2,'我是第三个坦克')
# print(list1)
#
# list1.pop()  #默认取出列表中最后一个数据
# print(list1)
# list1.pop()  #默认取出列表中最后一个数据
# print(list1)
# list1.pop()  #默认取出列表中最后一个数据
# print(list1)


# 4、简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，
# 则将商品名，价格，购买个数以三元组形式加入购物列表，
# 如果输入为空或其他非法输入则要求用户重新输入　　

# msg_dic = {
#     'apple': 10,
#     'tesla': 100000,
#     'mac': 3000,
#     'lenovo': 30000,
#     'chicken': 10,
# }

# while True:
#     for key, value in msg_dic.items():
#         print(key,value)
#
#     shop_goods = input('请输入你想购买的商品：').strip()
#     if shop_goods in msg_dic:
#         print(shop_goods,msg_dic[shop_goods])
#         shop_num = input('请输入你想购买的数目：').strip()
#         if shop_num.isdigit():
#             shop_num = int(shop_num)
#             print(shop_num)
#         shop_prices = msg_dic[shop_goods] * shop_num
#         Shopping_cart = (shop_goods, shop_num, shop_prices)
#         print(f'你购买的商品为{shop_goods}，商品数目为{shop_num}，总价格为{shop_prices}')
#     else:
#         print('不存在你需要的商品，请重新输入')

# while True:
#     for key, value in msg_dic.items():
#         print(key, value)
#     # 存入商品的单价和数目
#
#     choice_goods = input('请输入你想购买的商品：').strip()
#
#     # list1 = [choice_goods, msg_dic[choice_goods], choice_num]
#     list1 = []
#     # print(list1)
#     # if not choice_goods in msg_dic:
#     #     print('没有你想要的商品，请重新输入')
#     # else:
#     #     list1 = [choice_goods, msg_dic[choice_goods]]
#     #     print(list1)
#     #
#     #     # choice_num = input('请输入你想购买的商品数目：').strip()
#     #     while True:
#     #         choice_num = input('请输入你想购买的商品数目：').strip()
#     #         if not choice_num.isdigit():
#     #             print('请输入正确的商品数目')
#     #             choice_num = input('请输入你想购买的商品数目：').strip()
#     #
#     #         else:
#     #             choice_num = int(choice_num)
#     #             list1 = [choice_goods, msg_dic[choice_goods], choice_num]
#     #             check = msg_dic[choice_goods] * choice_num
#     #             print(f'你购买的{choice_goods}单价为{msg_dic[choice_goods]}数目为{choice_num}'
#     #                   f'合计价格为：{check}')
#     #             break
#     #     break
#     if choice_goods in msg_dic:
#         list1 = [choice_goods, msg_dic[choice_goods]]
#         print(list1)
#
#         # choice_num = input('请输入你想购买的商品数目：').strip()
#         while True:
#             choice_num = input('请输入你想购买的商品数目：').strip()
#             if choice_num.isdigit():
#                 choice_num = int(choice_num)
#                 list1 = [choice_goods, msg_dic[choice_goods], choice_num]
#                 check = msg_dic[choice_goods] * choice_num
#                 print(f'你购买的{choice_goods}单价为{msg_dic[choice_goods]}数目为{choice_num}'
#                       f'合计价格为：{check}')
#                 break
#             else:
#                 print('请输入正确的商品数目')
#                 choice_num = input('请输入你想购买的商品数目：').strip()
#         break
#     else:
#         print('没有你想要的商品，请重新输入')
# 4、简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，
# 则将商品名，价格，购买个数以三元组形式加入购物列表，拓展需求：如果用户还想继续加购怎么写？
# 如果输入为空或其他非法输入则要求用户重新输入　
msg_dic = {
    'apple': 10,
    'tesla': 100000,
    'mac': 3000,
    'lenovo': 30000,
    'chicken': 10,
}
# 定义一个空字典
shop_cart = {}
while True:
    print(msg_dic)
    # 存入商品的单价和数目
    choice_goods = input('请输入你想购买的商品：').strip()

    # dict1 ={'mac': [3000, 2]}
    if choice_goods not in msg_dic:
        print('没有你想要的商品，请重新输入')
        continue

    while True:
        choice_num = input('请输入你想购买的商品数目：').strip()
        if choice_num.isdigit():
            choice_num = int(choice_num)
            # 初始化默认字典dict1 ={'mac': [3000, 1]}
            # 如果字典为空，默认直接写入
            if not bool(shop_cart):
                shop_cart[choice_goods] = [msg_dic[choice_goods], choice_num]
                print(shop_cart)
                # 计算金额
                check = msg_dic[choice_goods] * choice_num
                print(f'你购买的{choice_goods}单价为{msg_dic[choice_goods]}元购买数目为{choice_num}'
                      f'合计价格为：{check}元')
                re_shop = input('你还想继续购物吗？输入Y/y继续加购，否则退出').strip()

                break

            # 如果不为空
            else:
                print(shop_cart)
                payment = {
                    'account': 0,
                }
                # 判断字典内是否已存在输入的那个商品，如果不存在，直接写，算出结果
                if not shop_cart.get(choice_goods):
                    shop_cart[choice_goods] = [msg_dic[choice_goods], choice_num]
                    check = msg_dic[choice_goods] * choice_num
                    print(shop_cart)
                    for choice_goods, choice_goods_pay in shop_cart.items():
                        payment[choice_goods] = choice_goods_pay[0] * choice_goods_pay[1]
                        payment['account'] = payment['account'] + payment[choice_goods]

                    # check = msg_dic[choice_goods] * final_num
                    # {'mac': [3000, 1], 'apple': [10, 1]}
                    # 你购买的apple单价为10元购买数目为1合计价格为：10元

                    print(f'你选购的商品为：{shop_cart}商品合计价格为；{payment["account"]}')
                    print(shop_cart)
                    # 重新选购选择，Y/y为继续，其他为退出
                    re_shop = input('你还想继续购物吗？输入Y/y继续加购，否则退出').strip()
                    break
                else:
                    # 选购数为和
                    final_num = shop_cart[choice_goods][1] + choice_num
                    # dict1[choice_goods] = [msg_dic[choice_goods], final_num]
                    # 更新购物车后的商品加购信息
                    # shop_cart[choice_goods] = [msg_dic[choice_goods], final_num]
                    shop_cart[choice_goods] = [msg_dic[choice_goods], final_num]
                    print(shop_cart)  # {'mac': [3000, 1], 'apple': [10, 7]}

                    # 计算购物金额
                    # payment = {
                    #     'account': 0,
                    # }

                    for choice_goods, choice_goods_pay in shop_cart.items():
                        payment[choice_goods] = choice_goods_pay[0] * choice_goods_pay[1]
                        payment['account'] = payment['account'] + payment[choice_goods]

                    # check = msg_dic[choice_goods] * final_num
                    # {'mac': [3000, 1], 'apple': [10, 1]}
                    # 你购买的apple单价为10元购买数目为1合计价格为：10元

                    print(f'你选购的商品为：{shop_cart}商品合计价格为；{payment["account"]}')
                    print(shop_cart)

                    # 重新选购选择，Y/y为继续，其他为退出
                    re_shop = input('你还想继续购物吗？输入Y/y继续加购，否则退出').strip()

                    break

        else:
            print('请输入正确的商品数目XXX')
        break
    if re_shop == 'Y' or re_shop == 'y':
        continue
    else:
        break






# 加购商品前：
# 1、商品判断是否在商品清单中，是继续。不是提示循环让输入
# 2、加购数目判断是否是数字，是继续，不是循环提示输入正确的
# 加购商品：
# 1、判断购物车是否为空，为空就直接将选中的商品和数量加入购物车，并结算出商品，提示是否要继续加购，y继续，其他终止
# 2、判断第二次加购的商品是否存在购物车内，
#     若不存在，则直接加入购物车，并结算出商品，提示是否要继续加购，提示是否要继续加购，y继续，其他终止；
#     若存在，则将已存在的商品数量更新，得出两次相同商品数量之和，提示是否要继续加购，y继续，其他终止；