import os
from ddt import ddt,data,unpack,file_data
import unittest

def get_data():
    testdata=[{'name':'tom','age':20},{'name':'kite','age':19}]
    return testdata


@ddt
class MyTestCase(unittest.TestCase):
    #读取元组数据-单组元素
    @data(1,2,3)
    def test1(self,value):
        print('测试1',value)

    #读取元组数据，多组元素
    @data((1,2,3),(4,5,6))
    def test2(self,value):
        print('测试2',value)

    #读取元组数据-拆分数据
    @data((1,2,3),(4,5,6))
    @unpack #拆分数据 pack打包
    def test3(self,value1,value2,value3):
        print('测试3',value1,value2,value3)

    #列表
    @data([{'name':'tom','age':20},{'name':'kite','age':19}])
    def test4(self,value):
        print('测试4',value)

    #字典
    @data({'name':'tom','age':20},{'name':'kite','age':19})
    def test5(self,value):
        print('测试5',value)

    #字典拆分
    @data({'name':'tom','age':20},{'name':'kite','age':19})
    def test6(self,name,age):
        print('测试6',name,age)

    #变量或者方法调用
    testdata=[{'name':'tom','age':20},{'name':'kite','age':19}]

    #@data(*testdata) #调用testdata变量
    @data(get_data()) #调用方法
    def test7(self,value):
        print('测试7',value)

    #读文件
    @file_data(os.getcwd()+'/data_json.json')
    def test8(self,value2):
        print('测试8',value2)

if __name__ == '__main__':
    unittest.main()

