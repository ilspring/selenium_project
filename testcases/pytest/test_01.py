import pytest

class TestLoginCase(object):
    def test01(self):
        print('结果是test01')
        assert 1==1

    def test02(self):
        print('结果是test02')
        assert 2==2

if __name__=='__main__':
    pytest.main(['-vs','test01.py'])