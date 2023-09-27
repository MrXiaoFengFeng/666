# 需求：写一个提取请求内容和响应内容的参数
# 现在我们开始编写

# 1、这里涉及json内相关参数提取，使用到jmespath
import os
import sys

import jmespath
from requests.models import Response

# 2、参数提取出来放在那里？，
# 内存--> 代码运行过程中长存， 数据库-->  redis 内存型数据库，高速读取， 不存mysql硬盘型的数据，因为参数读取要速度快，频率高

# 3、封装，先写虚的功能，再完成相关内容。虚的内容指的是你要完成步骤过程中，拆解出来的方法，步骤一 步骤二 步骤三
# 之前我们学习学过断言，断言后就是参数提取，那么我们要定义提取的数据结构
'''
提取参数后的参数名： 参数表达式
根据上述结构，发现字典格式合适
'''
temp_extract = {
    "session": "cookies.Session"
}


# 现在开始实现参数提取的方法，现在发现提取参数这个方法是可以当做一个工具方法，那么我们可以写成类方法


class Cache:

    # 提取参数
    @classmethod
    def extract_data(cls, var_name, actual_data_key_word, actual_data_expression, response):
        if hasattr(response, actual_data_key_word):
            property_or_func = getattr(response, actual_data_key_word)
            # 判断方法是否可以被调用，+()
            if callable(property_or_func):
                _property = property_or_func()
            else:
                _property = property_or_func

        # 判断是否存在表达式：
        if actual_data_expression:
            # 如果表达式存在，则用jmespath寻找表达式对应的内容
            __property = jmespath.search(actual_data_expression, _property)
        else:
            # 如果不存在，等于response反射的属性值
            __property = _property

        # 重点！这行代码是把需要缓存的数据存进类变量，类是常驻内存，所以我们没有用实例处理变量存储
        cache_data = {var_name: __property}
        # cls.__dict__.update(cache_data)  # 缓存方法错了
        # setattr(cls,cache_data[var_name], __property)
        setattr(cls,var_name, __property)
        print(cls.__dict__)
        # cls.var_name = __property

    # 提取参数后需要保存参数
    @classmethod
    def set_cache(cls, cache_desc: dict, response):
        # 重点重点来了，下述这段代码具有通用性，这个时候我们发现不止断言用到了，而且在参数提取也用到了，这个时候我们要把下述代码进行封装
        for var_name, var_expression in cache_desc.items():
            # 先解析 cookies.Session
            # 这里可以用断言写的那一段方法
            try:
                # 切割实际返回结果字段
                actual_data_key_word, actual_data_expression = var_expression.split(".", 1)

            except Exception:

                # 实际结果值等于实际切割后的值
                actual_data_key_word = var_expression
                # 表达式为None
                actual_data_expression = None

            # 下述功能已完善了提取，但没有缓存，我们把这段代码抽出来，放在extract，单独处理
            # 补充，这里需要从重构的response获取值
            # if hasattr(response, actual_data_key_word):
            #     property_or_func = getattr(response, actual_data_key_word)
            #     # 判断方法是否可以被调用，+()
            #     if callable(property_or_func):
            #         _property = property_or_func()
            #     else:
            #         _property = property_or_func

            # 循环遍历提取参数
            cls.extract_data(var_name, actual_data_key_word, actual_data_expression, response)


if __name__ == '__main__':
    # 继续写虚的调用
    # 我希望执行下述方法就可以完成参数的提取和保存
    # temp_extract = {
    #     "session": "cookies.Session"
    # }
    # Cache.set_cache(temp_extract)
    # 现在来实现上述方法的具体过程

    # 测试
    import requests
    # from utils.response_rebuild import ResponseObject
    from response_rebuild import ResponseObject

    request_desc = {
        "method": "post",
        "url": "http://www.kuaidi100.com/query",
        "params": "None",
        "data": {
            "type": "shunfeng",
            "postid": "SF1631643020688"
        }
    }
    resp = requests.request(**request_desc)
    print(resp.text)
    print(resp.cookies.get_dict())
    new_resp = ResponseObject(resp)
    # 测试参数缓存
    # 下述提取语法不对，cookies里面没有session
    temp_extract = {
        # "session": "cookies.Session"  # --> ?? {'_adadqeqwe1321312dasddocHref': '', '_adadqeqwe1321312dasddocReferrer': '', '_adadqeqwe1321312dasddocTitle': 'kuaidi100'}
        "context": "json.data[0].context"
    }
    print(Cache.set_cache(cache_desc=temp_extract, response=new_resp))
