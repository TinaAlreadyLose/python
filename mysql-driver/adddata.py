#!usr/local/bin/python
'''
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数
'''
import pymysql
conmysql=pymysql.connect("localhost","demo","JHjh@2310699","demo_db")# 打开数据库连接
cursor=conmysql.cursor()#使用cursor()方法获取操作游标
def InsertUpdateDeleteData(sql):
    try:
        cursor.execute(sql) #执行sql语句
        conmysql.commit()   #提交到数据库执行
        print("success")
    except:
        print("failed")
        conmysql.rollback()#执行失败回滚
    conmysql.close()#关闭数据库
sql0="insert into DEMO \
    values('da',20,'F',60.3)"
sql1="insert into DEMO \
    values('%s',%s,'%s',%s) "% \
        ('tina',20,'W',65)
sql2="select * from DEMO"
# sql3="update DEMO set age=age+1 where name='%s'" %('tina')
sql3="UPDATE DEMO SET age=age+1  WHERE name='%s' " %('tina')
number=60.2
sql4="delete from DEMO where score=%s" %(number)
def insertDEMO(sql):
    try:
        cursor.execute(sql)# 执行sql语句
        conmysql.commit()#提交到数据库
    except:
        print('sql语句执行失败')
        conmysql.rollback()#发生错误则回滚N

def searchDEMO(sql):
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        for i in results:
            name=i[0]
            age=i[1]
            sex=i[2]
            sorce=i[3]
            print("name=%s,age=%s,sex=%s,score=%s"% \
                (name,age,sex,sorce))
    except:
        print("找不到该数据")

def updateDEMO(sql):
    try:
        cursor.execute(sql)#执行sql语句
        print("1")
        conmysql.commit()#提交到数据库执行
        print("2")
    except:
        print("跟新失败")
        conmysql.rollback()
def deleteDEMO(sql):
    try:
        cursor.execute(sql)
        conmysql.commit()
    except:
        print("删除失败")
        conmysql.rollback()
# insertDEMO(sql1)
# searchDEMO(sql2)
# updateDEMO(sql3)
#deleteDEMO(sql4)
conmysql.close()#关闭数据库连接
# 插入，更新，删除数据三合一
