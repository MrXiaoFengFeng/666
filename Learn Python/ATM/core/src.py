import time
from lib.common import logger


def login():
    print('登录功能')
    logger('运行了登录功能')



def register():
    print('注册功能')
    logger('你运行了注册功能')


def withdraw():
    print('提现功能')
    logger('你提现了100元')


def transfer():
    print('转账功能')
    logger('你转账了20元')


func_dic = {
    '0': ['退出功能', exit],
    '1': ['登录功能', login],
    '2': ['注册功能', register],
    '3': ['提现功能', withdraw],
    '4': ['转账功能', transfer]
}

def run():
    while True:
        for k in func_dic:
            print(k,func_dic[k][0])

        choice = input('请输入你的编号:>').strip()
        if choice in func_dic:
            func_dic[choice][1]()
        else:
            print('请输入正确的数字')

