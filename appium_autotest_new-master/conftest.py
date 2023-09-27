import pytest, time, os, sys
o_path = os.getcwd()
pg_path = os.path.join(o_path,"Pages")
cm_path = os.path.join(o_path,"Common")
sys.path.append(o_path)
sys.path.append(pg_path)
sys.path.append(cm_path)
from Common.base_driver import BaseDriver
from Pages.Good_Page import GoodPage


base_driver = None

def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device_info", help=None)

@pytest.fixture(scope='session')
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture(scope='session')
def base_driver(cmdopt):
    global base_driver
    base_driver = BaseDriver(eval(cmdopt)).get_base_driver()
    yield base_driver

'''@pytest.fixture(scope = 'function', autouse=True)
def before(goodpage):
    goodpage.reset()'''
    


