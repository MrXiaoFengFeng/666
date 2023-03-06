'''
存放公共功能
'''
from conf import settings


# 登录认证装饰器
def login_auth(func):
    # 解决问题：循环导入问题
    from core import src

    def inner(*args, **kwargs):
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('用户未登录，请登录后再使用功能！')
            src.login()

    return inner


# 记录日志功能。应该放在公共功能中
def append_log(log_data):
    with open(settings.LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(log_data + '\n')
