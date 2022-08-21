#定位元素许多元素用的方法相同，单独写一个，其他类继承
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_text(self,text,*loc): #可变参数放最后面
        self.get_element(*loc).send_keys(text)

    def click_btn(self,*loc):
        self.driver.find_element(*loc).click()

    def get_title(self):
        return self.driver.title


class BaiduPage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        driver.get('https://www.baidu.com')

    def test_search(self):
        loc=(By.ID,'kw')
        loc2=(By.ID,'su')
        self.input_text('selenium',*loc)
        self.click(*loc2)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    baiduPage=BaiduPage(driver)
    baiduPage.test_search()