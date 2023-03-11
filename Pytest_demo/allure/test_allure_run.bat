

cd E:\WorkSpace\Pytest_demo\allure\
call pytest -vs test_attach.py --alluredir=E:\WorkSpace\Pytest_demo\allure\result


cd E:\WorkSpace\Pytest_demo\venv\Lib\site-packages\allure-2.21.0\bin
call allure generate E:\WorkSpace\Pytest_demo\allure\result -o E:\WorkSpace\Pytest_demo\allure\report --clean

cd E:\WorkSpace\Pytest_demo\venv\Lib\site-packages\allure-2.21.0\bin
call allure open E:/WorkSpace/Pytest_demo/allure/report/

