from playwright.sync_api import sync_playwright
import ddddocr


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=['--start-maximized']
    )
    context = browser.new_context(no_viewport=False)
    page = context.new_page()
    page.goto('https://www.3ayy.com/vod-s/-------------.html?wd=%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9%E5%B9%B4%E7%95%AA')

    # 定位到验证码并截图保存
    page.locator('.mac_verify_img').screenshot(path='./verify_img.png')

    # 实例化识别方法
    ocr = ddddocr.DdddOcr(show_ad=True)

    with open('./verify_img.png', 'rb') as f:
        img = f.read()
        print(f'识别的验证码为：{img}')
    code = ocr.classification(img)
    page.get_by_role("textbox").fill(code)

    page.pause()



