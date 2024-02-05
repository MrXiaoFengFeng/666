from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)  # 设置了每步等待时间为3s
    # context = browser.new_context()
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()  # 打开一个页面
    page.goto('http://demo.liumatest.cn/#/home/dashboard')  # 打开地址

    # 输入账号密码登录
    # page.fill('#username','demo')  # 输入账号
    # page.fill('#password','123456')  # 输入密码
    # page.click('#login')  # 点击登录
    # context.storage_state(path='auth.json')
    page.screenshot(path='./mi_sc.png')
    page.pause()
    browser.close()



    #playwright codegen --save-storage=E:\WorkSpace\Playwright\section1\auth.json
    #playwright codegen --save-storage=E:\WorkSpace\Playwright\section1\auth.json https://www.mi.com/shop/user/orderList
