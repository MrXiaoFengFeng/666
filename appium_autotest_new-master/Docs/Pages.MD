# Pages文件使用指南
1. Base_Page
   - **包含底层的公共函数**
    1. get_phone_size(self) 
        - 无需传入参数
        - 返回Page对象中的driver
        - 以(x,y)返回屏幕尺寸
        - 底层函数是driver.get_window_size()
    2. def mswipe(self, direction, element=None, n=1)
        - 必要参数"direction"为滑动的方向
        - 默认以整个屏幕为滑动区域滑动,若传入了"element"参数，则以"element"所在的区域滑动
        - 默认滑动1次,如需滑动多次可传入"n"
        - 针对全面屏手势进行了边界优化,如误触全面屏手势可修改"MAX_EDGE_LIMIT"变量解決
        - 本函数思路为获取"element"的边界值,从中心靠近滑动反方向0.25倍长或宽位置滑动至0.75倍长或宽位置,所以可能有滑动超边界的问题(比如一张图片没有划走或者想翻一页但是翻了两页),如遇问题建议用函数start_end_slide(self, start_x, start_y, end_x, end_y)替代,该函数需手动设置滑动的起始点和结束点
        - 函数底层为driver.swipe(from_x, from_y, to_x, to_y)
    3. def mclick(e)
        - 传入"element"对象,并对对象进行点击
        - 是e.click()的封装
    4. def find_text(self, keyword)
        - 传入"keyword"字符串对象
        - 函数通过查找xpath元素的text信息进行对象的查找
        - 因其效率低下且容易忽略已存在的问题,所有此函数仅在无法通过id定位元素时才推荐使用
        - 此函数会自动保存屏幕截图,方便后期核对
        - 若有多个元素符合要求,会以列表形式返回数据
        - 以下情况推荐使用此函数
           - 多个元素id相同时
           - 无法确定元素id时
           - 对当前界面进行模糊查找时
        - 此函数是对driver.find_elements_by_xpath()的封装
    5. def touch_text(self, text)
        - 传入"text"对象
        - 函数通过调用find_text(self, text)查找文本为text的元素并对其进行点击操作
        - 同样的,不建议大规模使用此函数
        - 在测试点初始化时会用到此函数进行目录跳转
    6. def send_back_key(self)
        - 无需传入对象
        - 函数向对应设备发送返回键信息,使设备返回至上一级
        - 考虑到很多应用或手机系统的设置,返回动画较长,建议在此函数后加1-2秒的等待时间
        - 此函数是对driver.press_keycode(4)的封装
    7. def swipe_find(self, text, direction="up", MAX_TRY_TIME=10)
        - 必要传入对象"text"为待查找的信息
        - "direction"为当前界面找不到时滑动屏幕的方向
        - "MAX_TRY_TIME"为最大尝试次数
        - 此函数功能在于能够向指定方向查找元素,比如部分信息在当前页面下方,但因为待测机型分辨率不同所以无法定义滑动多少再去查找,所以此函数会循环进行滑动和查找,直至找到元素
        - 因其调用了find_text,所以仍以列表形式返回信息
        - 在每次滑动时都会截屏记录方便后期debug
    8. def adb_shell(self, shell)
        - 必要传入对象"shell"
        - 此函数自动获取当前设备名,并执行shell命令
        - 注意,传入的shell是adb shell后的命令
        - 此函数返回shell的返回信息,是对os.popen的封装
    9. mishoop_open(self)
        - 打开小米商城app
        - 无需传入参数,是对driver.start_activity的封装
    10.  def go_page(self, pth)
        - 需要以列表方式传入pth
        - pth为进入需测试页面的路径,要求一字不差
    11. get_element(self, ele_conf)
        - 从本地字典获取元素id
        - 需要传入元素字典
        - 此函数首先根据字典中id查找元素,若返回元素为多个,则根据字典中text查找元素,二者相比后,返回与字典匹配度最高的元素
        - 推荐使用此方法
    12. open_plugin(self, id)
        - 传入pluginId
        - 此函数是对adb shell的封装,通过调用应用程序的.plugin.PluginRootActivity来开启商城的指定界面,指定界面的id保存于Config\PluginsId.yml中
   - **包含全局基本信息**
    1. driver信息
        - 在conftest中,获取到driver变量,并通过子类Pages传入给BasePage,使driver变量不需要重复获取
        - 通过Page.driver可调用driver变量,进行后续的操作
    2. 包名及activity信息
    3. element信息
        - 通过读取yml文件获取element信息并记录在self.element中
2. 子类Pages
    - **包含此页面的特定配置信息及样例配置**
       - 如Good_Page中保存了进入测试用例页面的路径,用例的价格信息等,方便与测试结果比对
    - **包含仅此页面才需要的特定函数**
       - 如此页面的进入函数,及重置函数
