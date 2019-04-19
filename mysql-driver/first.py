# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     port='3306',
#     user='demo',
#     passwd="JHjh@2310699"
# )
# # mycursor=mydb.cursor()
# # mycursor.execute("CREATE DATABASE demo")
import pymysql
def connectMysql():
    mydb=pymysql.connect('localhost','demo','JHjh@2310699','demo_db') # 数据库所在的ip，数据库名，密码，使用的数据库名
    cursor=mydb.cursor()    #s使用cursor()方法创建一个游标对象cursor
    cursor.execute("SELECT VERSION()")#执行查询语句
    data=cursor.fetchone()  #获取单条数据
    print("Database version :%s" %data)
    sql='''
    CREATE TABLE DEMO(
        name VARCHAR(20) NOT NULL,
        age INT NOT NULL,
        sex VARCHAR(2) NOT NULL,
        score FLOAT NOT NULL
    )
    '''
    cursor.execute(sql)
    mydb.close()


connectMysql()
 