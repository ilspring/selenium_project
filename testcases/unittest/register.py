from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
from selenium import webdriver
from time import sleep
import pytest



class TestUserRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://testerhome.com/account/sign_up')
        cls.driver.maximize_window()

    # 测试登录验证码错误
    def test_register_code_error(self):
        username='test1'
        name='test1'
        email='111@11.com'
        pwd='1111'
        conpwd='111'
        phone='13000000000'
        code='11111'
        phone_code='1111'
        expected='问题导致无法提交'

        self.driver.find_element(By.ID,'user_login').send_keys(username)
        self.driver.find_element(By.ID,'user_name').send_keys(name)
        self.driver.find_element(By.ID,'user_email').send_keys(email)
        self.driver.find_element(By.ID,'user_password').send_keys(pwd)
        self.driver.find_element(By.ID,'user_password_confirmation').send_keys(conpwd)
        self.driver.find_element(By.ID,'user_phone_number').send_keys(phone)
        self.driver.find_element(By.NAME,'_rucaptcha').send_keys(code)
        self.driver.find_element(By.ID,'user_phone_code').send_keys(phone_code)
        self.driver.find_element(By.NAME,'commit').click()

        #断言
        # WebDriverWait(self.driver,5).until(EC.alert_is_present())
        err_msg=self.driver.find_element(By.XPATH,'//*[@id="new_user"]/div[1]/div/strong').get_attribute('value')
        print('错误提示:',err_msg)
        #验证
        # assert alert.text==expected
        self.assertEqual(err_msg,expected)
        # alert.accept()


    #测试成功
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
        # assert alert.text == expected
        self.assertIn('社区置顶')
        alert.accept()

if __name__ == '__main__':
    unittest.main()