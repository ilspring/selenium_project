from testcases import test1,test02
from util import util
from selenium import webdriver
from testcases.basic.register import TestUserRegister
from testcases.basic import test_login,testht



if __name__ == '__main__':
    # case01=TestUserRegister()
    # case01.test_register_code_error()
    # case01.test_register_ok()
    login=test_login.TestUserLogin()
    # case02.test_username_error()
    login.test_userlogin_ok()
    login.test_ht()
    case=testht.TestHt(login)
    case.test_ht_error()