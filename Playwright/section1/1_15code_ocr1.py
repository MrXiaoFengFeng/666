from playwright.sync_api import sync_playwright
import ddddocr


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=['--start-maximized']
    )
    page = browser.new_page(no_viewport=False)
    page.goto('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')

    page.locator('#email').fill('232@qq.com')
    page.locator('#pwd').fill('123456')

    # 定位到验证码，然后将验证码截图保存
    page.locator('#imgCode').screenshot(path='./imgcode.png')

    # 实例化
    ocr = ddddocr.DdddOcr(show_ad=False)
    with open('./imgcode.png', 'rb') as f:
        img_info = f.read()
        img = ocr.classification(img_info)
        print(f'识别的图片验证码为{img}')
    # 填入识别的验证码
    page.locator('#code').fill(img)

    page.pause()




