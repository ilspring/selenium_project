import MySQLdb
import pytest

conn=MySQLdb.connect(
    user = 'root',
    passwd='123456',
    host='localhost',
    port=3306,
    db='test_db'
)

def get_data():
    query_sql='select id,username,pwd from user_tbl'
    lst=[]
    try:
        cursor=conn.cursor() #获取游标
        cursor.execute(query_sql)
        r=cursor.fetchall()
        for x in r:
            u=(x[0],x[1],x[2]) #0、1、2代表的是id,username,pwd
            lst.append(u)
        return lst
    finally:
        cursor.close()
        conn.close()

@pytest.mark.parametrize('id,name,pwd',get_data())
def test1(id,name,pwd):
    print(id,name,pwd)

if __name__ == '__main__':
    pytest.main(['-sv','test_db.py'])