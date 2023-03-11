import allure


def test_attach_text():
    allure.attach('这是一个纯文本', name='文本啦', attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach('<head></head><body>这是一块html body块</body>','html测试块', allure.attachment_type.HTML)


def test_attach_jpg():
    allure.attach.file('E:\\WorkSpace\\Pytest_demo\\allure\图片.jpg',
                       name='这是个图片',attachment_type=allure.attachment_type.JPG)