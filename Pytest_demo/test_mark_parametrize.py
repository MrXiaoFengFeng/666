import sys

import pytest
#1、 参数化，前两个变量，后面是对应的数据
# 3+5->test_input  8->expected
# @pytest.mark.parametrize('test_input, expected', [('3+5', 8), ('2+5', 7), ('7*5', 30)])
# def test_eval(test_input, expected):
#     # eval 将字符串str当成有效的表达式来求值，并返回结果,字符串反射成数字
#     assert eval(test_input) == expected
#




#2、 参数组合
# @pytest.mark.parametrize('x',[1,2])
# @pytest.mark.parametrize('y',[8,10,11])
# def test_foo(x, y):
#     print(f'测试数据组合为{x}{y}')


# 3、方法名作为参数
test_user_data = ['tom', 'jerry']
@pytest.fixture(scope='module')
def login_r(request):
    # 接收并传入的参数
    user = request.param
    print(f'\n 打开首页准备登录，登录用户{user}')
    return user


#功能不完善，预期就为失败/ 希望测试由于某种情况就应该失败
@pytest.mark.xfail
# @pytest.mark.skipif(sys.platform == 'win32', reason = '不在macos上执行')
# @pytest.mark.skip('这次不执行登录了')
# indirect=True,可以把传过来的参数当函数执行
@pytest.mark.parametrize('login_r', test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f'用例中login_r返回的值为；{a}')
    assert a != ""
    raise NameError


if __name__ == '__main__':
    pytest.main()