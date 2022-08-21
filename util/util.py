import pickle
import random
import string
import logging
import logging.handlers
import datetime
from PIL import Image
import os,muggle_ocr,time
from selenium.webdriver.common.by import By

'''公共方法'''
def get_code(driver,id):
    # 获取验证码图片
    t = time.time()
    path=os.path.dirname(os.path.dirname(__file__))+'\\screenshots'
    img_name = path+ '\\' +str(t) + '.png'
    driver.save_screenshot(img_name)

    # ce = driver.find_element(By.CLASS_NAME, 'rucaptcha-image')
    ce = driver.find_element(By.CLASS_NAME, id)
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    # 保存截取的坐标图
    im = Image.open(img_name)
    img = im.crop((left, top, right, height))

    t = time.time()
    img_name2 = path + '\\' +str(t) + '.png'
    img.save(img_name2) #截取到验证码图片保存

    # 解析截取的验证码图片
    # 初始化sdk；model_type 包含了 ModelType.OCR/ModelType.Captcha 两种模式,分别对应常规图片与验证码
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
    with open(img_name2, 'rb') as f:
        code = f.read()
    text = sdk.predict(image_bytes=code)
    # print(text)
    return text

#随机生成字符串
def get_random_str():
    rand_str=''.join(random.sample(string.ascii_letters+string.digits,8))
    return rand_str

#日志模块
def get_logger():
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    all_path=os.path.dirname(os.path.dirname(__file__))+'\\logs\\all.txt'
    rf_handle = logging.handlers.TimedRotatingFileHandler(all_path, when='midnight', interval=1, backupCount=7,atTime=datetime.time(0, 0, 0, 0))
    rf_handle.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))

    err_path=os.path.dirname(os.path.dirname(__file__))+'\\logs\\error.txt'
    f_handle = logging.FileHandler(err_path,encoding='utf-8')
    f_handle.setLevel(logging.ERROR)
    f_handle.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s'))

    logger.addHandler(rf_handle)
    logger.addHandler(f_handle)
    return logger

#加载cookie的两个方法
def save_cookie(driver,path):
    with open(path,'wb') as filehandler:
        cookies=driver.get_cookies()
        print(cookies)
        pickle.dump(cookies,filehandler)

def load_cookie(driver,path):
    with open(path,'rb') as cookiesfile:
        cookies=pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)


