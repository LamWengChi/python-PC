from BaiduMAP_API.MySQLAPI_demo import MysqlDemo

#连接mysql数据库
mysql = MysqlDemo('192.168.0.211','root','ddd123','ceshi')
# # print(mysql)
# 需要插入的数据
data = {
    'FIRST_NAME':"Tuling",
    'LAST_NAME':"Xuyuan",
    'AGE':18,
    'SEX':"G",
    'INCOME':"10000"
}
# 执行demo的insert插入数据
mysql.insert('BJTLXY',data)


# #查看数据
# sql = 'select * from BJTLXY where FIRST_NAME="liu"'
# #查看一条数据
# #  res = mysql.get_one(sql)
# # print(res)
# # 查看全部数据
# res = mysql.get_all('select * from BJTLXY')
# for item in res:
#     print(item)




##插入数据
# import pymysql
# db = pymysql.connect('192.168.0.211','root','ddd123','ceshi')
# cursor = db.cursor()
# sql = 'insert into BJTLXY(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES("liu","dana",18,"M","10000")'
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

##创建表
# import pymysql
# db = pymysql.connect('192.168.0.211','root','ddd123','ceshi')
# cursor = db.cursor()
# cursor.execute('DROP TABLES IF EXISTS BJTLXY')
# sql = """create table BJTLXY(
# FIRST_NAME CHAR(20) NOT NULL,
# LAST_NAME CHAR(20),
# AGE INT,
# SEX CHAR(1),
# INCOME FLOAT)"""
#
# cursor.execute(sql)
# db.close()