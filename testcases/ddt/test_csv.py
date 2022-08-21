import pytest,csv
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)

#读取csv文件
def get_data():
    with open('test.csv','r') as f:
        lst=csv.reader(f)
        mydata=[]
        for row in lst:
            #extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
            mydata.extend(row)
        return mydata

@pytest.mark.parametrize('name',get_data())
def test1(name):
    print(name)






if __name__== '__main__':
    # get_data()
    pytest.main(['-sv','test_csv.py'])