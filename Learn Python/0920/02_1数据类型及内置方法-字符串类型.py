# int
# 数据类型转换

# #2.1 纯数字的字符串转换为整型
# res = int('123155')
# print(res,type(res))

#2.2
#十进制--》二进制(0b表示二进制)
# 11->1011
# print(bin(11)) #0b1011
# # 反转：
# print(int(0b1011),2)
#
# #十进制--》八进制(0o)
# print(oct(11)) #0o13
# print(int(0o13),8)
#
# #十进制--》十六进制(0x)
# print(hex(11)) #0xb
# print(int(0xb),11)


#jion拼接的用法
# l = ['a','b','c']
# res= ':'.join(l)
# print(res)  #a:b:c

# #replace的用法
# msg = 'hello word hello'
# print(msg.replace('hello','HELLO',)) #逗号后面不写数表示替换所有的you
# print(msg.replace('hello','HELLO',1)) #逗号后面写数字表示替换1次


#isdigit(bytes和Unicode)的用法(isnumberic()#unicode、中文数字(四)、阿拉伯数字(IV))
#判断字符串是否由纯数字组成
print('20'.isdigit())
print('2323'.isdigit())
print("23dw".isalnum()) #字母或者数字组成