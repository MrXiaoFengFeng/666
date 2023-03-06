# 1、把登录与注册的密码都换成密文形式
# 注册
import configparser
import hashlib
import json

# 把登录和注册的密码加密成密文
import os


def get_pwd_md5(password):
    # 1.先给密码加密成密文
    md5_obj = hashlib.md5()
    # 加盐
    salt = 'jojo'
    md5_obj.update(password.encode('utf-8'))
    # 给盐加密
    md5_obj.update(salt.encode('utf-8'))

    md5_password = md5_obj.hexdigest()

    return md5_password


def register():
    username = input('请输入你注册的用户名：').strip()
    password = input('请输入你的密码：').strip()
    re_password = input('请确认你的密码：').strip()
    if password == re_password:
        # 1、调用密码加密
        md5_password = get_pwd_md5(password)
        # 2.再组织用户数据并保存
        user_dic = {
            'username': username,
            'password': md5_password,
            'balance': 15000,
        }
        with open('user_db.json', 'w', encoding='utf-8') as f:
            json.dump(user_dic, f)


# 登录
def login():
    # 1. 先将user_db.json文件中的用户数据读取出来
    with open('user_db.json', 'r', encoding='utf-8') as f:
        user_dic = json.load(f)

    username = input('请输入你的用户名：').strip()
    # 2.判断用户名是否正确
    if username == user_dic.get('username'):
        password = input('请输入你的密码：').strip()
        # 2.1 调用密码加密功能
        md5_password = get_pwd_md5(password)
        print(md5_password == '91d2708c838f90c1dd57f3dd95b01803')

        # 2.2 判断用户输入的密码与文件中的密码是否一致
        if md5_password == user_dic.get(password):
            print('登录成功！')
            print(f'用户{username} 余额{user_dic.get("balance")}')


# register()
# login()


# 2、文件完整性校验（考虑大文件）
'''
1. 先打开一个未修改作业.txt文件，获取到该文件的md5值，并保存
2.再打开修改后的作业.txt文件，并校验与未修改前md5值是否一致
3.若校验成功，则证明文件是完整的
'''


def get_file_md5(file_path):
    # 1.先通过os.path.getsize获取到文件的大小（int类型）
    file_size = os.path.getsize(file_path)
    # 2.在文件的四个位置找到一个点
    # 2.1获取文件开头的位置
    offset1 = 0
    # 2.2获取文件1/3位置
    offset2 = file_size // 3
    # 2.3获取文件2/3位置
    offset3 = (file_size // 3) * 2
    # 2.3获取文件最后位置
    offset4 = file_size - 10
    # get_data_list:里面存放文件中4个位置的值，每个位置获取10个值
    get_data_list = [offset1, offset2, offset3, offset4]

    # 创建一个空哈希对象
    md5_obj = hashlib.md5()
    with open(file_path, 'rb') as f:
        # 循环4个位置
        for offset in get_data_list:
            # 将光标移动到四个位置中
            f.seek(offset)
            # 读取10个bytes数据
            read_data = f.read(10)
            # 通过md5将4个位置截取的字符做一个MD5加密
            md5_obj.update(read_data)

    return md5_obj.hexdigest()


file_md5 = get_file_md5(r'E:\WorkSpace\Learn Python\homeworks\day22\作业.txt')
# print(file_md5)  # d8fd89143d18726f5beff1d32a0996e8
# 修改文件后md5就改变了


# 4、项目的配置文件采用configparser进行解析
# 生成mysql配置信息
conf_obj = configparser.ConfigParser()
conf_obj['MYSQL'] = {
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'USER': 'tank',
    'PASSWORD': '123456',
}

with open('mysql.ini', 'w') as f:
    conf_obj.write(f)


# 校验mysql配置信息
conf_obj = configparser.ConfigParser()
conf_obj.read('mysql.ini')
# 获取配置信息标题
title = conf_obj.sections()
if 'MYSQL' in title:
    ini_user = conf_obj['MYSQL']['USER']
    ini_pwd = conf_obj['MYSQL']['PASSWORD']

    if ini_user == 'tank' and ini_pwd == '123456':
        print('mysql连接成功！')

