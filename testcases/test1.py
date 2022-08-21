from selenium import webdriver
from time import sleep
import pyautogui
from selenium.webdriver.common.by import By


def test1():
    driver=webdriver.Chrome()
    driver.get('https://testerhome.com/account/sign_up')
    driver.maximize_window()
    sleep(1)
    elem=driver.find_element(By.CLASS_NAME,'custom-control-label')
    r1=elem.rect
    pyautogui.moveTo(r1['x']+10,r1['y']+130)
    pyautogui.click()
    sleep(3)