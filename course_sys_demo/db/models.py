"""
用于存放类
"""
from db import db_handler


class Base:
    def save(self):
        db_handler.save(self)

    @classmethod
    def select(cls, user):
        # 传递类名与用户名给db_handler里的select
        obj = db_handler.select(cls, user)
        return obj


class Admin(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        # 调用类，即保存数据
        self.save()
