import pytest

# @pytest.fixture()
# def init():
#     print('测试init')
#     return 1
#
# def test1(init):
#     print('测试1')
#
# def test2(init):
#     print('测试2')
#
# if __name__=='__main__':
#     pytest.main(['-sv','test04.py'])

class TestCase(object):
    @classmethod
    def setup_class(cls):
        print('setup-class')

    @classmethod
    def teardown_class(cls):
        print('teardown-class')


    def test01(self):

        print('class-test01')

    def test02(self):
        print('class-test02')

def setup_function():
    print('setup_function')

def teardown_function():
    print('teardown_function')

def setup_module():
    print('setup module')

def teardown_module():
    print('teardown_module')

def test1():
    print('测试1')

def test2():
    print('测试2')

if __name__=='__main__':
    pytest.main(['test04.py','-sv'])