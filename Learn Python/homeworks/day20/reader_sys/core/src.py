'''
source,此处存放核心业务逻辑代码
'''
import time
from db import db_handler
from lib import common


# 注册功能
def register():
    print('注册功能执行中。。。')
    while True:
        username = input('请输入你注册的用户名：').strip()
        # 1.先校验用户是否存在
        # 涉及数据的操作：调用查看数据功能 --> select
        # user_data --> [user, pwd, bal] or None
        user_data = db_handler.select(username)

        # 若存在则让用户重新输入
        if user_data:
            print('当前输入的用户已存在，请重新输入！')
            continue

        password = input('请输入你的密码:').strip()
        re_password = input('请确认你的密码:').strip()
        # 判断两次输入的密码是否一致
        if password == re_password:
            print(f'用户{username}注册成功！')
            db_handler.save(username, password)
            break
        else:
            print('两次输入的密码不一致，请重新输入！')


# 全局变量记录用户登录状态
login_user = None


# 登录功能
def login():
    print('登录功能执行中。。。')
    while True:
        username = input('请输入你的用户名：').strip()
        # 判断用户名是否存在于db.txt中
        userdata = db_handler.select(username)
        # 若用户不存在，则报错
        if not userdata:
            print('你输入的用户不存在，请重新输入！')
            continue
        # 若用户存在，则继续输入密码
        password = input('请输入你的密码：').strip()
        if password == userdata[1]:
            print(f'用户{username}登录成功！')
            global login_user
            login_user = username
            break
        else:
            print('用户名或密码错误，登录失败')


# 充值功能
@common.login_auth
def recharge():
    print('充值功能执行中。。。')
    while True:
        # 1、让用户输入充值金额
        balance = input('请输入你的充值金额：')
        # 2、判断用书输入的是否是数字
        if not balance.isdigit():
            print('请输入数字！')
            continue
        balance = int(balance)

        # 3、修改当前用户的金额
        # 3.1、获取当前用户的金额
        user, pwd, bal = db_handler.select(login_user)
        # 3.2、修改当前用户修改前的金额
        old_data = f'{user}:{pwd}:{bal}'
        print(old_data, type(old_data))

        # 3.3、修改当前用户金额,做加钱操作
        bal = int(bal)
        bal += balance

        # 3.4、拼接“修改后”的当前用户数据
        new_data = f'{user}:{pwd}:{bal}'

        # 3.5、调用修改数据功能
        db_handler.update(old_data, new_data)
        print(f'当前用户: [{login_user}] 成功充值金额:[{balance}] 元')

        # 3.6、日志记录充值功能
        # 日志格式为："时间 用户名 操作(充值or消费) 金额"
        now_time = time.strftime('%Y-%m-%d %X')
        log_data = f'当前时间为{now_time} 用户{login_user} 成功充值{balance}元'
        print(log_data)
        common.append_log(log_data)

        break


# 阅读小说功能
@common.login_auth
def reader():
    '''
    1、写该功能之前，现将小说数据，存放在story_class.txt文件中
    2、先将story_class.txt文件中的数据获取出来，解析成字典类型
    :return:
    '''
    print('阅读小说功能执行中。。。')
    # 获取story_class.txt文件中的字典数据
    story_dic = db_handler.get_all_story()
    '''
    {
    "0":{
            "0":["倚天.txt",3],
            "1":["沙雕.txt",10]
    },

    "1":{
            "0":["令人.txt",6],
            "1":["二狗.txt",5]
    },
    "2":{
        "0":["矮跟.txt",6],
        "1":["坦克.txt",5]
    },
    }
    '''
    # 如果没获取到内容则报错未找到小说数据
    if not story_dic:
        print('未找到小说数据，请联系管理员！')
        return

    while True:
        # 1、打印小说种类选择信息
        print('''
        ============欢迎来到小说阅读系统，请输入你的编号=================
        0 玄幻武侠
        1 都市爱情
        2 矮跟和坦克
        ===========================END=================================
        ''')
        # 2、让用户输入小说选择编号
        choice1 = input('请输入你选择的小说类型编号：').strip()
        # 3、判断用户输入的编号是否在小说字典数据内
        # 若输入有误，则重新输入
        if choice1 not in story_dic:
            print('编号输入有误，请重新输入！')
            continue

        # 4、获取当前编号类型中的所有小说数据
        fiction_dic = story_dic.get(choice1)
        '''
            "0":["倚天.txt",3],
            "1":["沙雕.txt",10]
        '''

        # 5、打印当前类型的说有小说，让用户选择
        for number, fiction_list in fiction_dic.items():
            print(f'小说编号[{number}] 小说名字[{fiction_list[0]}] 小说价格[{fiction_list[1]}]')

        # 6、让用户选择需要购买的小说
        while True:
            choice2 = input('请输入需要购买的小说编号:').strip()
            if choice2 not in fiction_dic:
                print('编号输入有误，请重新输入区')
                continue
            # name -->小说名字，price -->小说价格
            fiction_name, price = fiction_dic.get(choice2)

            # 7、让用户输入y选择是否购买商品
            choice3 = input(f'当前选择的小说为[{fiction_name}] 价格为[{price}],请输入"y"确认购买，或退出程序：').strip()

            # 8、判断用户输入的是否是y
            if choice3 == 'y':
                # 9、校验当前用户的金额是否大于等于小说单价
                # 9.1 获取当前用户金额
                user, pwd, bal = db_handler.select(login_user)

                # 9.2 判断金额
                # 当前用户金额
                bal = int(bal)
                # 小说单价
                price = int(price)

                if bal < price:
                    print('余额不足，请充值后再购买！')
                    break
                # 10、开始扣费
                # 10.1 拼接用户修改前的数据
                old_data = f'{user}:{pwd}:{bal}'

                # 10.2 对用户做扣钱操作
                bal -= price

                # 10.3 拼接用户修改后的数据
                new_data = f'{user}:{pwd}:{bal}'
                db_handler.update(old_data, new_data)

                print('当前小说购买成功！自动打开小说阅读')
                fiction_data = db_handler.show_fiction_data(fiction_name)
                print(
                    f'''
                    ===============当前小说数据如下==========
                    {fiction_data}
                    '''
                )

                # 11、日志记录充值功能
                # 日志格式为："时间 用户名 操作(充值or消费) 金额"
                now_time = time.strftime('%Y-%m-%d %X')
                log_data = f'当前时间为{now_time} 用户{login_user} 成功消费{price}元'
                print(log_data)
                common.append_log(log_data)
                break
        break


# 函数字典
func_dic = {
    '0': register,
    '1': login,
    '2': recharge,
    '3': reader,
}


# 启动函数
def run():
    '''
    # 一：程序运行开始时显示
    0 账号注册
    1 账号登录
    2 充值功能
    3 阅读小说
    '''

    while True:
        print(
            '''
            ==============小说阅读器欢迎你================
            0 账号注册
            1 账号登录
            2 充值功能
            3 阅读小说
            ====================  end  ==================
            '''
        )
        # 让用户输入编号
        choice = input('请输入你的编号[输入"q"退出程序]:')

        if choice == 'q':
            break
        # 判断用户输入的编号是否在字典内
        if choice not in func_dic:
            print('你输入的编号有误，重新输入')
            continue

        # 若存在则调用函数对象
        func_dic.get(choice)()
