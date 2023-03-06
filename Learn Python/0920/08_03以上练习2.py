# 练习2：
# 写函数，计算传入字符串中【数字】、【字母】、【空格】及【其他】的个数


def check_str(msg):
    res = {
        'num': 0,
        'string': 0,
        'space': 0,
        'other': 0,
    }
    for s in msg:
        if s.isdigit():
            res['num'] += 1
        elif s.isalpha():
            res['string'] += 1
        elif s.isspace():
            res['space'] += 1
        else:
            res['other'] += 1
    return res


res = check_str("'WELCOME to egon's world 1234321'")
print(res)
