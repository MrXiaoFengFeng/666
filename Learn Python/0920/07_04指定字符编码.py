'''
#     t文本（默认的模式）
#         1.读写都已str为单位的
#         2.文本文件
#         3.必须指定encoding = 'utf-8'
'''

with open(r'file\c.txt',mode='rt',encoding='utf-8') as f:
    res = f.read()
    print(res,type(res))