# 默写无参一个装饰器

from functools import wraps

def outter(func):
    # func = index
    @wraps(func)
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        return res
    return wrapper


@outter
def index(x,y):
    '''这是index的说明'''
    print('welcome to index page')
    print(x,y)


index(1,2)
