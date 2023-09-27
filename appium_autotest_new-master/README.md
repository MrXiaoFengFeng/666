# Appium自动化测试脚本

项目简介
===
为减轻测试组人力资源消耗，完善了Appium_autotest框架

该框架可实现在Windows下对多个安卓设备进行多线程APP功能测试

该框架采用了Page-Object思想，将每个不同的页面都封装成一个类，并共同继承BasePage的基础公共类

在BasePage中封装了所有类都能用到的公共方法，其他Page中封装仅在该Page下才需要的特定方法，并读取该页面的特定配置文件，减少后期维护成本

功能特性
===

1. 支持自动识别已连接的可用ADB调试设备
2. 自动生成Allure报告
3. 方便使用和维护

```
具体文档请见 /Docs
```

环境依赖
===
- Jinkins(需正确安装Allure拓展)
- Allure
- Appium
- npm
- Python
- Java
  
部署步骤
===
1. 安装npm(https://nodejs.org/en/download/current/)
2. npm中安装appium和appium-doctor(不推荐GUI版本appium)
```
npm install -g appium
npm install -g appium-doctor
```
3. 安装jre，配置JAVA_HOME
4. 安装platform_tools，配置ANDROID_HOME
5. 使用appium-doctor检查环境依赖是否成功配置
```
appium-doctor --android
```
6. 克隆本项目至本地
```
git clone https://micode.be.xiaomi.com/qa-mall/appium_autotest_new.git
```
7. 安装python依赖
```
pip install -r ./reqiurment.txt
```
8. 运行main.py或将项目部署至Jinkens

目录结构描述
===
```
C:.
│  conftest.py      //pytest中conftest文件,用于配置测试信息
│  main.py          //多线程启动pytest
│  README.md
│  requirement.txt  //python依赖文件包
│
├─.vscode           //vscode配置文件
│      settings.json
│
├─allure-results    //生成的allure报告存放处
├─Common            //一些底层方法封装
│  │  base_driver.py
│  │  logshot.py
│  │  __init__.py
│
├─Config            //配置文件存放目录
│      Appium_Caps.yml
│      GoodPage_conf.yml
│      Page_Elements.yml
│
├─Docs              //帮助文档存放目录
├─log               //log存放目录
│
├─Pages             //PageObject封装
│  │  Base_Page.py
│  │  Good_Page.py
│  │  __init__.py
│
├─Plug-ins          //拓展工具目录
│      autoConf.py  //自动抓取app中的按钮及文字信息
│
├─shot              //测试中截图存放目录
│      
│
├─TestCase          //测试点存放目录
│      test_1.py

```


版本内容更新
===
- 2021.7.27
```
支持多线程自动识别已连接的设备
采用PO思想重新封装
减少了维护难度
提高可读性和可读性
```
- 2021.7.28
```
优化多线程
修改项目配置兼容Jenkins
```
- 2021.7.29
```
对yml文件存储格式进行优化
添加自动维护配置文件的工具
```
##**todo:**
1. 解决报告显示问题
2. 编写使用文档
3. 封装其他页面

