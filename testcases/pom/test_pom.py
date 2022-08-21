from selenium import webdriver
import unittest
from time import sleep

from selenium.webdriver.common.by import By

#pom模式，数据和页面松耦合
class BaiduPage(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

        self.input_ele=(By.ID,'kw')
        self.btn_ele=(By.ID,'su')

    def goto_baidu(self,url):
        self.driver.get(url)

    def get_ele(self,url,kw):
        self.goto_baidu(url)
        self.driver.find_element(*self.input_ele).send_keys(kw)
        self.driver.find_element(*self.btn_ele).click()
        sleep(3)



class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        self.baiduPage=BaiduPage()

    def test_search(self):
        self.baiduPage.get_ele('https://www.baidu.com','selenium')

if __name__ == '__main__':
    unittest.main()
