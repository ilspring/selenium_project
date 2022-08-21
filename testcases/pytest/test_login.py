#coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
import pytest
from util import util


#pytest+ddt重构,ddt可用脚本、数据、CSV、Excel、json等格式

class TestUserLogin(object):
    login_data=[
        ('','123456','账号不能是空字符'),
        ('ILwinter','987073590.','社区置顶')

    ]

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.maximize_window()
        self.logger=util.get_logger()
        self.logger.info('测试用户登录')

    @pytest.mark.dependency(name='user_login')
    @pytest.mark.parametrize('username,pwd,expected',login_data)
    def test_user_login(self,username,pwd,expected):
       '''
        #用户名为空
        username=''
        pwd='123456'
        expected='继续操作前请注册或者登录。'
        '''

       self.driver.find_element(By.ID, 'user_login').clear()  # 同时执行调用清空，每一个输入框都清空
       self.driver.find_element(By.ID, 'user_login').send_keys(username)
       self.logger.debug('输入用户名称：%s', username)

       self.driver.find_element(By.ID, 'user_password').clear()  # 同时执行调用清空，每一个输入框都清空
       self.driver.find_element(By.ID, 'user_password').send_keys(pwd)
       self.logger.debug('密码是：%s', pwd)

       self.driver.find_element(By.NAME, 'commit').click()
       self.logger.debug('点击登录')

        # 断言
       if username=='':
           WebDriverWait(self.driver, 5).until(EC.alert_is_present())
           alert = self.driver.switch_to.alert
            # 验证

           assert alert.text == expected
           self.logger.error('断言出错%s','报错了',exc_info=1)
           alert.accept()
       else:
           WebDriverWait(self.driver, 5).until(EC.alert_is_present())
           alert = self.driver.switch_to.alert
           # 验证

           assert alert.text == expected
           self.logger.error('断言出错%s', '报错了', exc_info=1)
           sleep(3)
           alert.accept()
           self.driver.close()


'''
    @pytest.mark.dependency(name='user_login')
    def test_userlogin_ok(self):
        username = 'ILwinter'
        pwd = '987073590.'
        expected = '社区置顶'

        self.driver.find_element(By.ID,'user_login').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.ID,'user_login').send_keys(username)
        self.logger.debug('输入用户名称：%s',username)

        self.driver.find_element(By.ID,'user_password').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.ID,'user_password').send_keys(pwd)
        self.logger.debug('密码是：%s',pwd)

        self.driver.find_element(By.NAME,'commit').click()
        self.logger.debug('点击登录')

        # 断言
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        alert = self.driver.switch_to.alert
        sleep(3)
        # 验证
        try:
            assert self.driver.title == expected+'111'
        # self.assertEqual(alert.text,expected)
        except AssertionError as ae:
            self.logger.error('断言出错%s','报错了',exc_info=1)
        alert.accept()

    # def test_ht(self):
    #     # 定位到话题
    #     ele=self.driver.find_element(By.XPATH, '//*[@id="navbar-new-menu"]')
    #     ActionChains(self.driver).move_to_element(ele).click().perform()
    #
    #     ele1=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/ul/li[2]/div/a[1]')
    #     # 鼠标移动到元素再点击
    #     ActionChains(self.driver).move_to_element(ele1).click().perform()

        # self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/ul/li[2]/div/a[1]').click()

  
    '''

if __name__ == '__main__':
    pytest.main(['test_login.py'])