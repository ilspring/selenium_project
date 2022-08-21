import pytest
import json

def get_data():
    with open('data_json.json','r') as f:
        lst=[]
        data=json.load(f)
        lst.extend(data['keys'])
        return lst

@pytest.mark.parametrize('name',get_data())
def test1(name): #遍历
    print(name)

if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv','test_json.py'])
