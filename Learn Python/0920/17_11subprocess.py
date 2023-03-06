
import subprocess

obj = subprocess.Popen('echo 123 ; ls / ; ls /root' ,shell = True,
                       stdout = subprocess.PIPE,
                       stderr = subprocess.PIPE
                       )
# print(obj)
# 正确的管道返回信息
# res = obj.stdout.read()
# print(res.decode('utf-8'))
#
# # 错误的管道报错信息
err_res = obj.stderr.read()
print(err_res.decode('utf-8'))