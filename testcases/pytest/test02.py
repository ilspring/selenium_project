import pytest,allure
import os

# class TestCase02(object):
#     @pytest.mark.do
#     def test01(self):
#         print('测试1')
#         self.add()
#
#     #pytest函数命名要以test开头才会执行，或者其他函数调用执行
#     def add(self):
#         print('增加')
#
#     @pytest.mark.undo
#     def test02(self):
#         print('测试2')
#
#
#
# if __name__=='__main__':
#     pytest.main(['test02.py'])

#pytest生成测试报告
@pytest.fixture(scope='session')
def login():
    print('用例先登录')

@allure.step('步骤1：点xxx')
def step_1():
    print('1111')

@allure.step('步骤2：点xxx')
def step_2():
    print('222')

@allure.feature('编辑页面')
class TestEditPage():
    #编辑页面
    @allure.story('这是一个xxx的用例')
    def test1(self,login):
        '''先登录，再去执行xxx'''
        step_1()
        step_2()
        print('xxx的用例')

    @allure.story('打开a的页面')
    def test2(self,login):
        '''先登录，再去执行'''
        print('a的页面')

if __name__=='__main__':
    #注意：生成测试报告，必须在命令行执行
    #pytest --alluredir ./reports test02.py
    #allure.bat serve ./reports 启动allure 查看报告
    pytest.main(['--alluredir','./reports','test02.py'])
    os.system('allure.bat generate ./reports -o ./reporthtml --clean')

