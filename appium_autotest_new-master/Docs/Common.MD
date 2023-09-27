# Common目录说明
1. base_driver
   - 通过cmd命令建立appium服务端会话
   - 读取Appium_Caps.yml中的配置
   - 有 get_base_driver 方法返回webdriver对象
2. logshot
   - 全称为 logger shotter
   - 记录日志和截图的方法
   - 每次启动时,都会生成以启动时间命名的log文件和shot文件夹存放日志和截图
   - logger中有4个级别,在case中引入logger后即可使用
    1. debug  ->   logger.debug()
    2. info  ->   logger.info()
    3. warning  ->   logger.warning()
    4. error  ->   logger.error()
   - shotter有2个方法,在case中引入shotter后即可使用
    1. shotter.shot() -> 获取屏幕截图,可传入变量"name"为截图保存名称,若不传入即默认为"SHOT+数字"作为名称
    2. shotter.error() -> 获取屏幕截图,并命名为"ERROR+数字"

    **以上shotter方法均会把截图上传至allure**