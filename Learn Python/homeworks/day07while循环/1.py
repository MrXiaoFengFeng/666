dict1 = {
    'a' : [1,2]
}
# # 'a':[1,2]
# #
# dict1['a'] = [1,2]
#
# print(dict1)
# print(dict1['a'][1])
#
# # dict1['a'][1] = dict1['a'][1] +3
#
# print(dict1.update(dict1['a'][1])
#       )

# list1 = {
#     'mac': [3000, 1],
# }
# a=2
# list1.update({'mac' : [3000,3+a]})
#
# print(list1['mac'][0])
while True:
    choice_num = input('请输入你想购买的商品数目：').strip()
    if not choice_num.isdigit():
        # choice_num = int(choice_num)
        print(666,type(choice_num))
        continue
    else:
        print(333)
