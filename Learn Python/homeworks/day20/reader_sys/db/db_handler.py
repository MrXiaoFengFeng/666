'''
用于存放操作数据代码
'''

from conf import settings
import os


# 查看数据
def select(username):
    '''
    - 接收用户输入的用户名
    - 若该用户存在，则返回当前用户的所有数据
    - 若不存在，则返回None
    :param username:
    :return:
    '''

    with open(settings.DB_TXT_PATH, 'r', encoding='utf-8') as f:
        # 获取db.txt文件中的每一行数据
        for line in f:
            # 在每一行中，判断接收过来的用户名是否存在于db.txt中
            if username in line:
                # 若用户存在，则在当前行中提取该用户的所有数据
                # user_data --> [user, pwd, bal]
                user_data = line.strip().split(':')
                # 将当前用户数据返回给调用者，存在就返回用户数据，不存在就返回None
                return user_data


# 保存数据
def save(username, password, balance=0):
    '''
    :param username: 注册用户名
    :param password: 注册的用户密码
    :param balance: 注册用户的初始金额设置为默认值
    :return:
    '''
    with open(settings.DB_TXT_PATH, 'a', encoding='utf-8') as f:
        f.write(f'{username}:{password}:{balance}\n')


# 更新数据
def update(old_data, new_data):
    # 1、拼接新的文件路径
    new_path = os.path.join(settings.DB_PATH, 'new.txt')
    # 2、读取db.txt文件的数据进行修改，写入到新文件new.txt中，在更换为db.txt文件
    with open(settings.DB_TXT_PATH, 'r', encoding='utf-8') as r_f, \
            open(new_path, 'w', encoding='utf-8') as w_f:
        # 2.1、新旧数据替换
        all_user_data = r_f.read()
        all_user_data = all_user_data.replace(old_data, new_data)

        # 2.2、将新数据写入新文件中
        w_f.write(all_user_data)

    # 3、文件名修改
    os.remove(settings.DB_TXT_PATH)
    os.rename(new_path, settings.DB_TXT_PATH)


# 读取小说字典数据
def get_all_story():
    with open(settings.STORY_CLASS_PATH, 'r', encoding='utf-8') as f:
        story_dic = eval(f.read())
        return story_dic


# 获取小说内容，查看单本小说
def show_fiction_data(fiction_name):
    # 获取小说路径
    fiction_path = os.path.join(settings.FICTIONS_PATH, fiction_name)

    # 打开文件，获取文件数据，并返回给用户
    with open(fiction_path, 'r', encoding='utf-8') as f:
        fiction_data = f.read()

        return fiction_data

