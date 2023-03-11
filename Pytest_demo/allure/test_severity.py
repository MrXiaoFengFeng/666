import allure
import pytest

@allure.severity(allure.severity_level.TRIVIAL)
def test_1():
    print('one')

@allure.severity(allure.severity_level.NORMAL)
def test_2():
    print('two')

@allure.severity(allure.severity_level.CRITICAL)
def test_3():
    print('three')

@allure.severity(allure.severity_level.BLOCKER)
def test_4():
    print('four')

if __name__ == '__main__':
    pytest.main()