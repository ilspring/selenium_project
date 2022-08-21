from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
from selenium import webdriver
from time import sleep
import pytest
from testcases.pom.pages.registerPage import UserRegisterPage


#pytest+ddt重构,ddt可用脚本、数据、CSV、Excel、json等格式
class TestUserRegister(object):
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver.get('https://testerhome.com/account/sign_up')
        # cls.driver.maximize_window()
        cls.registerPage=UserRegisterPage(cls.driver)
        cls.registerPage.goto_register_page()

    login_data=[
        ('tdemo001','test1','test@qq.com','111','111','13000000000','1111','111','短信验证码不正确'),
        ('demoest001', 'test1', 'test@qq.com', '111', '111', '13000000000', '1111', '111', '注册成功'),
    ]

    # 测试登录验证码错误
    @pytest.mark.parametrize('username,name,email,pwd,conpwd,phone,code,phone_code,expected',login_data)
    def test_register(self,username,name,email,pwd,conpwd,phone,code,phone_code,expected):
        self.registerPage.input_username(username)
        self.registerPage.input_name(name)
        self.registerPage.input_email(email)
        self.registerPage.input_pwd(pwd)
        self.registerPage.input_conpwd(conpwd)


        # 自动识别验证码
        if code !='666': #默认情况下验证码给一个666
            code = util.get_code(self.driver, 'rucaptcha-image')
        self.registerPage.input_code(code)

        self.registerPage.input_phone(phone)
        self.registerPage.input_phonecode(phone_code)

        self.registerPage.click_btn()

            # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
            # 验证
        assert alert.text == expected
            # self.assertIn('社区置顶')
        alert.accept()


'''   #测试成功
    def test_register_ok(self):
        username=util.get_random_str()
        name = username
        email=username+'@11.com'
        pwd='123456'
        conpwd='123456'
        phone='13000000000'
        #验证码自动获取
        code=''
        phone_code = '1111'
        expected='注册成功'
        self.driver.find_element(By.ID,'user_login').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.ID, 'user_login').send_keys(username)

        self.driver.find_element(By.ID,'user_name').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.ID, 'user_name').send_keys(name)

        self.driver.find_element(By.ID,'user_email').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.ID, 'user_email').send_keys(email)

        self.driver.find_element(By.ID,'user_password').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.ID, 'user_password').send_keys(pwd)

        self.driver.find_element(By.ID,'user_password_confirmation').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.ID, 'user_password_confirmation').send_keys(conpwd)

        self.driver.find_element(By.ID,'user_phone_number').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.ID, 'user_phone_number').send_keys(phone)

        #自动识别验证码
        code=util.get_code(self.driver,'rucaptcha-image')
        self.driver.find_element(By.NAME,'_rucaptcha').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.NAME, '_rucaptcha').send_keys(code)

        self.driver.find_element(By.ID,'user_phone_code').clear() #同时执行调用清空，每一个输入框都清空
        self.driver.find_element(By.ID,'user_phone_code').send_keys(phone_code)

        self.driver.find_element(By.NAME, 'commit').click()

        #等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # 验证
        assert alert.text == expected
        # self.assertIn('社区置顶')
        alert.accept()
        '''

if __name__ == '__main__':
    pytest.main(['testRegister.py'])