# 下载事件监听 事件监听听filechooser
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://lanzoui.com/iWhw6z921yb')


    # 1.先配置一个下载文件保存地址路径

    def download_handler(download):
        # 保存文件到本地
        print(download.url)  # 下载地址
        print(download.suggested_filename)  # 下载名称
        download.save_as(path='./'+download.suggested_filename)


    # 2.建立监听事件
    page.on('download', download_handler)

    loc = page.frame_locator('.ifr2').get_by_role("link", name="电信下载")

    loc.click()

    page.pause()
