from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys




class TestUserLogin(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.maximize_window()

    def test_username_error(self):
        #用户名为空
        username=''
        pwd='123456'
        expected='继续操作前请注册或者登录。'

        self.driver.find_element(By.ID,'user_login').send_keys(username)
        self.driver.find_element(By.ID,'user_password').send_keys(pwd)
        self.driver.find_element(By.NAME,'commit').click()

        # 断言
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # 验证
        assert alert.text == expected
        alert.accept()

    def test_userlogin_ok(self):
        username = 'ILwinter'
        pwd = '987073590.'
        expected = '社区置顶'

        self.driver.find_element(By.ID,'user_login').send_keys(username)
        self.driver.find_element(By.ID,'user_password').send_keys(pwd)
        self.driver.find_element(By.NAME,'commit').click()

        #断言
        # WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        # alert = self.driver.switch_to.alert
        # sleep(3)
        # # 验证
        # assert self.driver.title == expected
        # self.driver.close()

    def test_ht(self):
        # 定位到话题
        ele=self.driver.find_element(By.XPATH, '//*[@id="navbar-new-menu"]')
        ActionChains(self.driver).move_to_element(ele).click().perform()

        ele1=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/ul/li[2]/div/a[1]')
        # 鼠标移动到元素再点击
        ActionChains(self.driver).move_to_element(ele1).click().perform()

        # self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/ul/li[2]/div/a[1]').click()