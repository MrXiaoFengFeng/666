from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    # context = browser.new_context(accept_downloads=False)  # 屏蔽下载事件
    page = context.new_page()
    page.goto('https://deershare.com/send')

    # 方法1：上传事件监听filechooser
    page.on('filechooser', lambda file_chooser: file_chooser.set_files(r'E:\WorkSpace\Playwright\section2\全剧得.apk'))

    # 定位到点击元素
    page.click('text=上传文件')

    # 方法2：如果属性是input，用set_input_files('myfile')方法
    # page.get_by_label("选择文件").set_input_files('tou.png')



    page.pause()