from playwright.sync_api import sync_playwright

# 打开两个浏览器上下文
with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=['--start-maximized'],
        slow_mo=2000
    )
    # 创建上下文，浏览器实例1，打开第一个测试浏览器,与第二个数据互不干扰
    context1 = browser.new_context(no_viewport=True)
    page1 = context1.new_page()
    page1.goto('https://www.baidu.com')
    # 创建上下文，浏览器实例2，打开第一个测试浏览器
    context2 = browser.new_context()
    page2 = context2.new_page()
    page2.goto('https:www.bilibili.com')

    browser.close()
