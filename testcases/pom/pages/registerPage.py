from selenium.webdriver.common.by import By
from time import sleep
from testcases.pom.pages.basePage import BasePage

class UserRegisterPage(BasePage):
    username_input=(By.ID,'user_login')
    name_input = (By.ID,'user_name')
    email_input = (By.ID,'email')
    pwd_input = (By.ID,'user_password')
    conpwd_input = (By.ID,'user_password')
    phone_input = (By.ID,'user_password_confirmation')
    code_input = (By.ID,'user_phone_number')
    phonecode_input = (By.ID,'_rucaptcha')
    register_btn=(By.NAME, 'commit')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def goto_register_page(self):
        self.driver.get('https://testerhome.com/account/sign_up')
        self.driver.maximize_window()

    def input_username(self,username):
        self.input_text(*self.username_input).clear()
        self.input_text(username,*self.username_input)

    def input_name(self,name):
        self.input_text(*self.name_input).clear()
        self.input_text(name,*self.name_input)

    def input_email(self,email):
        self.input_text(*self.email_input).clear()
        self.input_text(email,*self.email_input)

    def input_pwd(self,pwd):
        self.input_text(*self.pwd_input).clear()
        self.input_text(pwd,*self.pwd_input)

    def input_conpwd(self,conpwd):
        self.input_text(*self.conpwd_input).clear()
        self.input_text(conpwd,*self.conpwd_input)

    def input_phone(self,phone):
        self.input_text(*self.phone_input).clear()
        self.input_text(phone,*self.phone_input)

    def input_code(self,code):
        self.input_text(*self.code_input).clear()
        self.input_text(code,*self.code_input)

    def input_phonecode(self,phonecode):
        self.input_text(*self.phonecode_input).clear()
        self.input_text(phonecode,*self.phonecode_input)

    def clickbtn(self):
        self.click_btn(*self.register_btn)
        sleep(2)