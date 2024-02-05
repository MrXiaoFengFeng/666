from playwright.sync_api import sync_playwright

# 封装页面切换的公共方法
def switch_to_my_page(context, title=None, url=None):
    # 切换到指定的标签名或者url
    for my_page in context.pages:
        if title:
            if title in my_page.title():
                # 定位激活到当前pagetab
                my_page.bring_to_front()
                return my_page
        elif url:
            if url in my_page.url():
                my_page.bring_to_front()
                return my_page
        else:
            print('title or url not found!')
    return context.pages[0]




with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.baidu.com')

    loc = page.locator('#s-top-left>a')

    # 点击打开所有页面
    for link in loc.all():
        link.click()

    # # 遍历page对象
    # for i in context.pages:
    #     print(i.title())
    #     print(i.url)



    page1 = switch_to_my_page(context, title='盘')
    print(page1.title())

    page.pause()