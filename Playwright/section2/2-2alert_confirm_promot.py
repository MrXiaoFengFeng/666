from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


def run(p):
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.baidu.com')

    loc = page.locator('#s-usersetting-top')
    loc.hover()  # 悬停在某个元素上
    page.wait_for_timeout(2000)
    s = page.get_by_text('搜索设置')
    expect(s).to_be_visible()  # 判断文字显示后再进行点击操作
    page.click('text=搜索设置')
    page.wait_for_timeout(1000)
    page.click('text=仅简体中文')
    page.click('text=每页20条')

    # 多个弹窗事件判断逻辑处理
    # def handle_dialog(dialog):
    #     """监听后处理"""
    #
    #     print(dialog.message)
    #     print(dialog.type)
    #     print(dialog.default_value)
    #     if dialog.type == 'prompt':
    #         dialog.accept(prompt_text='hello world')
    #     else:
    #         dialog.dismiss()
    #     page.on('dialog', handle_dialog)
    # 再点击触发弹窗前需要先建立一个监听，可以选择接收或者取消
    page.on("dialog", lambda dialog: dialog.accept())  # 一直保持
    # page.once("dialog", lambda dialog: dialog.dismiss())  #只监听运行一次
    page.on("dialog", lambda dialog: print(dialog.message))
    page.click('text=保存设置')

    browser.close()


if __name__ == '__main__':
    with sync_playwright() as p:
        run(p)
