#加载本地浏览器用户缓存数据
#在运行的时候，先关闭本地的chrome 浏览器，再执行代码，就可以看到启动的浏览器，打开网站不需要登录了,但是未加载插件
import getpass
from playwright.sync_api import sync_playwright
print(getpass.getuser()) # 获取用户名；在本地谷歌浏览器输入chrome://version/也可获取

# USER_DIR_PATH = f'C:\\Users\\Smile\\AppData\\Local\\Google\\Chrome\\User Data'
# 用自动获取的用户名
USER_DIR_PATH = f'C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\User Data'

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        headless=False,
        channel='chrome',
        user_data_dir=USER_DIR_PATH,
        viewport={'width': 1920, 'height': 1080}
    )
    page = browser.new_page()
    page.goto('https://www.baidu.com')

    page.pause()
