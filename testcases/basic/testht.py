from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys



class TestHt(object):
    def __init__(self,login):
        self.login=login


    #话题标题为空
    def test_ht_error(self):
        ht_title=''
        ht_body='有没有面试题做做'
        expected='问题导致无法提交'

        # #定位到话题
        # self.login.driver.find_element(By.XPATH,'//*[@id="navbar-new-menu"]').click()
        # self.login.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/ul/li[2]/div/a[1]').click()


        self.login.driver.find_element(By.ID,'node-selector-button').click()
        e=self.login.driver.find_element(By.XPATH,'//*[@id="node-selector"]/div/div/div[2]/div/div/div/div[7]/span/span[4]/a')
        sleep(1)
        #鼠标移动到元素再点击
        ActionChains(self.login.driver).move_to_element(e).click().perform()
        self.login.driver.find_element(By.ID,'topic_title').send_keys(ht_title)
        self.login.driver.find_element(By.ID,'topic_body').send_keys(ht_body)
        self.login.driver.find_element(By.ID,'save_as_draft').click()

        loc=(By.CLASS_NAME,'alert')
        WebDriverWait(self.login.driver,5).until(EC.visibility_of_element_located(loc))
        msg=self.login.driver.find_element(*loc).text

        assert msg==expected



