# !/usr/bin/python3
# _*_coding:utf-8 _*_
from time import strftime

from py._xmlgen import html
import pytest

def pytest_collection_modifyitems(items):
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例描述', class_="sortable", col="name"))  # 表头添加Description
    cells.insert(4, html.th('执行时间', class_='sortable time', col='time'))
    cells.pop(-1)  # 删除link

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))  # 表头对应的内容
    cells.insert(4, html.td(strftime('%Y-%m-%d %H:%M:%S'), class_='col-time'))
    cells.pop(-1)  # 删除link列

@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):   # 清除执行成功的用例logs
    if report.passed:
        del data[:]
        data.append(html.div('正常通过用例不抓取日志', class_='empty log'))

@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "自动化测试报告"

# 修改Environment部分信息，配置测试报告环境信息
def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "web项目冒烟用例"
    config._metadata['接口地址'] = 'https://XX.XXX.XXX'
    config._metadata['开始时间'] = strftime('%Y-%m-%d %H:%M:%S')
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")
    config._metadata.pop("Packages")
    config._metadata.pop("Platform")
    config._metadata.pop("Plugins")
    config._metadata.pop("Python")

# 修改Summary部分的信息
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("所属部门: 测试部")])
    prefix.extend([html.p("测试人员: XXX")])

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if item.function.__doc__ is None:
        report.description = str(item.function.__name__)
    else:
        report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 设置编码显示中文
