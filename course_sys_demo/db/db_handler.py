import os, pickle
from conf import settings


# 保存数据
def save(obj):
    # 拼接保存数据的文件夹路径
    user_dir = os.path.join(
        settings.BD_PATH, obj.__class__.__name__,
    )
    # 若没有则创建
    if not os.path.isdir(user_dir):
        os.mkdir(user_dir)
    # print(user_dir)
    # 拼接文件路径
    user_path = os.path.join(
        user_dir, obj.user
    )
    # print(user_path)
    # 保存对象数据
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)


# 查看数据
def select(cls, username):
    # 拼接保存数据的文件夹路径
    user_path = os.path.join(
        settings.BD_PATH, cls.__name__, username
    )
    # 如果不存在路径，直接不返回
    if os.path.exists(user_path):
        # print(user_path)

        # 如果存在，查看对象数据
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj
