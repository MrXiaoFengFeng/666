from playwright.sync_api import sync_playwright

# 调用start返回playwright，playwright中包含start()和stop()
p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.baidu.com")
print(page.title())
browser.close()
p.stop()
