"""
用户保存对象，获取对象
"""
import os
import pickle
from conf import settings


# 保存对象数据
def save_data(obj):
    """
    # 1、获取对象的保存的文件夹路径
    # 以类名当做文件夹的名字
    # obj.__class__获取当前对象的类
    # obj.__class__.__name__获取当前对象的类的名字
    :param obj:
    :return:
    """
    # 以类名当做文件夹的名字
    user_dir_path = os.path.join(settings.DB_PATH, obj.__class__.__name__)

    # 2、判断文件夹是否存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 3、拼接当前用户的pickle文件路径，以用户作为文件名
    user_path = os.path.join(user_dir_path, obj.user)

    # 4、打开文件保存对象，通过pikcle保存
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)





# 查看对象数据
def select_data(cls, username):  # 类, username
    # 1、以类名当做文件夹的名字
    user_dir_path = os.path.join(
        settings.DB_PATH, cls.__name__)

    # 2、拼接当前用户的pickle文件路径，以用户作为文件名
    user_path = os.path.join(user_dir_path, username)
    print(user_path)
    # 3、判断文件如果存在则打开，并返回，若不存在，则代表用户不存在
    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj

