
# 什么是猴子补丁
# 属性在运行时的动态替换，叫做猴子补丁（Monkey Patch）。
# 猴子补丁的核心就是用自己的代码替换所用模块的源代码

# 猴子补丁的功能
# 拥有在模块运行时替换的功能, 例如: 一个函数对象赋值给另外一个函数对象(把函数原本的执行的功能给替换了)

#在入口处打猴子补丁
import json
import ujson

def monkey_patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads

monkey_patch_json() # 在入口文件处运行

json.dumps()
json.loads()


# 三.monkey patch的应用场景
# 如果我们的程序中已经基于json模块编写了大量代码了，发现有一个模块ujson比它性能更高，
# 但用法一样，我们肯定不会想所有的代码都换成ujson.dumps或者ujson.loads,那我们可能
# 会想到这么做
# import ujson as json，但是这么做的需要每个文件都重新导入一下，维护成本依然很高
# 此时我们就可以用到猴子补丁了