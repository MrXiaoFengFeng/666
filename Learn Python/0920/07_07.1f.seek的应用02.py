import time

with open(r'file/access.log',mode='rb') as f:
    #1.将指针跳到文件末尾
    f.seek(0,2)
    while True:
        line = f.readline()
        if len(line) == 0:
            time.sleep(0.3)
        else:
            print(line.decode('utf-8'),end='')