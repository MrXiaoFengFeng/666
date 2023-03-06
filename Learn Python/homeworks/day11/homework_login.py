# 2.1：编写用户登录接口
# 1、输入账号密码完成验证，验证通过后输出"登录成功"
# 2、可以登录不同的用户
# 3、同一账号输错三次锁定，（提示：锁定的用户存入文件中，
# 这样才能保证程序关闭后，该用户仍然被锁定）

## 2.2：编写程序实现用户注册后，可以登录
import json
import jmespath


def login():
    username = input("请输入登录账号")
    password = input("请输入密码")
    if not all([username, password]):
        print("ERROR : 账号和密码不能为空")
        print("登录失败")
        exit()  # return

    with open("user.json", 'r', encoding='utf-8') as f:
        table_data = json.load(f)

    if not table_data:
        exit("数据库读取失败")

    table_username = jmespath.search("[*].username", table_data)

    if username not in table_username:
        exit("ERROR: 用户名或密码错误")

    table_password = jmespath.search(f"[?username=='{username}'] | [0].password", table_data)
    if not password or password != table_password:
        exit("ERROR: 用户名或密码错误")

    print(f"{username} 登录成功")

    func_num = input("0：登录\n"
                     "1：注册\n"
                     "")

    func_map = {
        "0": login,
        "1": regsiter
    }

    if func_num.isdigit() and func_num in func_map:
        func = func_map[func_num]
        func()
    else:
        print("请输入0 / 1")


def regsiter():
    pass


def main():
    func_num = input("0：登录\n"
                     "1：注册\n"
                     "请输入你的选择:""")

    func_map = {
        "0": login,
        "1": regsiter
    }

    if func_num.isdigit() and func_num in func_map:
        func = func_map[func_num]
        func()
    else:
        print("请输入0 / 1")


if __name__ == '__main__':
    main()
