from selenium import webdriver
import muggle_ocr
from PIL import Image
import time


from selenium.webdriver.common.by import By


def test01():
    b=webdriver.Chrome()
    b.get('https://testerhome.com/account/sign_up')
    b.maximize_window()

    #获取验证码图片
    t=time.time()
    img_name=str(t)+'.png'
    b.save_screenshot(img_name)
    time.sleep(3)

    ce=b.find_element(By.CLASS_NAME,'rucaptcha-image')
    print(ce.location)
    left=ce.location['x']
    top=ce.location['y']
    right=ce.size['width']+left
    height=ce.size['height']+top

    #保存截取的坐标图
    im=Image.open(img_name)
    img=im.crop((left,top,right,height))

    t=time.time()
    img_name2=str(t)+'.png'
    img.save(img_name2)

    time.sleep(3)
    #解析截取的验证码图片
    # 初始化sdk；model_type 包含了 ModelType.OCR/ModelType.Captcha 两种模式,分别对应常规图片与验证码
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
    with open(img_name2,'rb') as f:
        code=f.read()
    text=sdk.predict(image_bytes=code)
    print(text)


