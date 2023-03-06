"""
管理员接口
"""
# from db import db_handler
from db import models


# 需要管理的类放到models里
# class Admin:
#     def __init__(self, user, pwd):
#         self.user = user
#         self.pwd = pwd


def register_interface(user, pwd):
    """ # 方式一：先将调用类，得到对象，在接口层，调用数据层保存数据
    # 1.将用户数据，保存到对象中，然后再将对象传给数据层
    admin_obj = models.Admin(user, pwd)
    print(admin_obj.__dict__)

    # 2、然后再讲对象传给数据层
    db_handler.save(admin_obj)
    """
    # 方式二：调用类，在实例化的过程中，保存对象
    # 1)判断用户是否存在,调用类方法，传递类名与用户名
    user_obj = models.Admin.select(user)
    if user_obj:
        return False, '用户已存在'

    # 2）不存在，在调用类创建对象，并保存对象
    # 通过models调用数据层
    models.Admin(user, pwd)

    # 3、给视图层返回注册成功
    return True, '注册成功'

