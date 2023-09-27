# 启动文件及pytest配置文件说明
## main.py
- 该测试脚本的启动程序
- 在main中添加了多线程信息
- 会自动获取已连接的安卓设备进行测试
- 使用了pytest的特性,通过args进行多线程测试
- 默认为一个设备一个线程 即```n = len(device_infos)```如需修改线程数只需要重新定义n即可
- 在get_infos中定义了caps信息,在此可修改server_port默认值(4723)


## conftest.py
- 该脚本为pytest的控制脚本
- 在会话开始时获取BasePage对象并向测试点传递实现不重复获取driver的目的
- parser为pytest的特性,将main中的配置文件传递给pytest以实现多线程并发