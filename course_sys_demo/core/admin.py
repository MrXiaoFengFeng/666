from interface import admin_interface


# 注册
def register():
    while True:
        username = input('请输入你注册的用户名：').strip()
        password = input('请输入你注册的密码：').strip()
        re_password = input('请确认你注册的密码：').strip()

        if password == re_password:
            # 调用接口，进行注册
            flag, msg = admin_interface.register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
            # admin_interface.register_interface(username, password)
            # break
        else:
            print('两次密码不一致')
        break

# 登录
def login():
    pass


# 创建学校
def create_school():
    pass


# 创建班级
def create_classes():
    pass


# 创建课程
def create_course():
    pass


# 创建教师
def create_teacher():
    pass



func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_classes,
    '5': create_course,
    '6': create_teacher,
}


# 管理员视图
def admin_view():
    """
    - 管理员功能
        - 管理员注册
        - 管理员登录
        - 创建学校
        - 创建班级（先选择校区）
            - 班级名称
            - 班级绑定的校区
        - 创建课程（课程绑定给班级，先选择班级）
            - 课程周期
            - 课程价格
        - 创建老师
            - 老师名称
            - 老师密码
    :return:
    """
    while True:
        print(
            '''
            1.管理员注册
            2.管理员登录
            3.创建学校
            4.创建班级
            5.创建课程
            6.创建老师
            '''
        )

        choice = input('请选择你的编号： ').strip()

        if choice not in func_dic:
            continue

        func_dic.get(choice)()


print(__name__)