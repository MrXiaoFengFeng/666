import unittest
from add import Caculator
from HTMLTestRunner_PY3 import HTMLTestRunner


class Do1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  # 只执行一次
        print('set UpClass')

    @classmethod
    def tearDownClass(cls) -> None:  # 只执行一次
        print('tearDownClass')

    def setUp(self) -> None:  # 每条用例执行前都执行一次
        print('所有用例运行前。。。')


    def tearDown(self) -> None:  # 每条用例执行前都执行一次
        print('所有用例运行后。。。')

    def test_01(self):
        res = Caculator(2, 3).add()
        print('用例1已运行')
        self.assertEqual(res, 5)

    @unittest.skip('不想测')
    def test_02(self):
        res = Caculator(2, -3).add()
        print('用例2已运行')
        self.assertEqual(res, -1)

    def test_03(self):
        res = Caculator(2, -3).sub()
        print('用例3已运行')
        self.assertNotEqual(res, 5)

class Do2(unittest.TestCase):
    def test_demo_01(self):
        print('demo_01')


    def test_demo_02(self):
        print('demo_02')

if __name__ == '__main__':
    # unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(Do1("test_01"))
    # suit.addTest(Do2("test_demo_01"))
    #
    # unittest.TextTestRunner().run(suit)


    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Do1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Do2)
    # suite = unittest.TestSuite([suite1, suite2])
    #
    # unittest.TextTestRunner().run(suite)



    # test_dir = "./"
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    # unittest.TextTestRunner().run(discover)


    report_title = "计算器的用例执行报告"
    desc = "用做展示修改样式后的HTMLTestRunner"
    report_file = "./TestReport.html"

    suite = unittest.TestSuite()
    suite.addTest(Do1("test_01"))
    suite.addTest(Do2("test_demo_01"))



    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(
            stream=report,
            title=report_title,
            description=desc,
        )
        runner.run(suite)
