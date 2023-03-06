import os



BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# LOG_PATH = r'%s\log\user.log'%BASE_DIR


path = r'log\user.log'
LOG_PATH = os.path.join(BASE_DIR,path)


print(LOG_PATH)