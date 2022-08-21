import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#实例unittest怎么使用
class TestUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass.........')
        cls.driver=webdriver.Chrome()
        cls.driver.get('https://www.baidu.com')
        cls.driver.maximize_window()

    def test01(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        print('test01')

    def test02(self):
        print('test02')
        self.assertEqual(1,1)
        # self.assertIn(1,[1,2,3])

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownclass....')
        cls.drver.close()


class TestUnittest02(unittest.TestCase):
    def test03(self):
        print('test03')

    def test04(self):
        print('test04')


if __name__=='__main__':
    # unittest.main()

    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    # 1、通过测试用例类加载、测试套件
    suite.addTests(loader.loadTestsFromTestCase(TestUnittest))
    suite.addTests(loader.loadTestsFromTestCase(TestUnittest02))

    #2、通过测试用例模板加载
    suite.addTest(loader.loadTestsFromModule(TestUnittest02))

    #3、通过路劲加载
    import os
    path=os.path.dirname(os.path.abspath(__file__))
    suite.addTest(loader.discover(path))

    runner=unittest.TextTestRunner()
    runner.run(suite)