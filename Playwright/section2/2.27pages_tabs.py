from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.baidu.com')

    loc = page.locator('.s-top-left>a')

    # 打开所有页面
    for link in loc.all():
        link.click()
        print(link.get_by_title())


    page.pause()