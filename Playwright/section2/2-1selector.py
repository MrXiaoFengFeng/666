"""
playwright 可以通过三种方式定位：css selector、xpath selector、html属性（id等）
或者text文本内容定位元素
"""
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.baidu.com')



    # 场景：搜索输入框填入playwright
    # locator方式 两种方式：
    # 1.先定位再操作
    # page.locator('#kw').fill('playwright')
    # page.locator('#su').click()

    # 直接调用内置封装方法
    # page.fill('#kw', 'playwright')
    # page.fill('id=kw', 'playwright')
    # page.click('#su')

    # 2.定位使用xpath和css
    # 明确指定说明方式
    # page.fill('css=#kw', 'playwright')
    # page.click('xpath=//*[@id="su"]')
    #
    # # 不指定说明，直接写系统也能分辨
    # page.fill('#kw', 'playwright')
    # page.click('#su')

    # 3.用文本定位操作
    # page.click('text=新')  # 模糊匹配
    # page.click('text="新闻"')

    # 4.组合定位
    # page.fill('span>>[id=kw]', 'playwright')
    # page.click('span>>#su')



    """
    这些是 playwright 推荐的内置定位器。
    • page.get_by_text() 通过文本内容定位。
    • page.get_by_label() 通过关联标签的文本定位表单控件。
    • page.get_by_placeholder() 按占位符定位输入。
    • page.get_by_title() 通过标题属性定位元素。
    • page.get_by_role() 通过显式和隐式可访问性属性进行定位。
    • page.get_by_alt_text() 通过替代文本定位元素，通常是图像。
    • page.get_by_test_id() 根据 data-testid 属性定位元素（可以配置其他属性）
    """


    # 文本匹配是绝对唯一的
    # page.get_by_text('网盘', exact=True).click()
    # page.get_by_text('网盘').click()

    # page.get_by_text('网盘') #可以用来断言
    # expect(page.get_by_text("网盘")).to_be_visible()
    # page.get_by_role('button', name='立即登录').click()  # 角色是按钮

    # xpath定位方式
    # page.locator('//*[text()="网盘"]').click()  # 精准匹配
    # page.locator('//*[contains(text(), "盘")]').click()


    page.pause()

    # context.close()