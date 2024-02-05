from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    context = browser.new_page(no_viewport=True)
    context.goto("https://baidu.com")
    print(context.title())

    browser.close()