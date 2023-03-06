# 练习1：
# 写函数，用户传入修改的文件名，与要修改的内容执行函数，完成批量修改操作


def modify_file(filename, old, new):
    import os
    with open(filename, 'r', encoding='utf-8') as read_f, \
            open('.bak.swap', 'w', encoding='utf-8') as write_f:
        for line in read_f:
            if old in line:
                line = line.replace(old, new)
            write_f.write(line)
    os.remove(filename)
    os.rename('.bak.swap', filename)


modify_file('/Users/egon/PycharmProjects/python/a.txt', 'egon', 'egon_new')