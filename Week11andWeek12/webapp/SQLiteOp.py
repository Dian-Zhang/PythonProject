import os
import sqlite3


# 数据库连接
def connect_db():
    # 获取当前文件目录路径
    basedir = os.path.abspath(os.path.dirname(__file__))
    # 构造数据库连接
    database_url = os.path.join(basedir, "../tkkc.db")
    # 连接数据库并返回该数据库
    return sqlite3.connect(database_url)


# 数据表创建
def create_table(sql):
    try:
        db = connect_db()
        db.execute(sql)
        db.commit()
        db.close()
    except BaseException as e:
        print("出错了", e)


# 数据表数据插入
def insert_data(sql):
    try:
        db = connect_db()
        db.execute(sql)
        db.commit()
        db.close()
    except BaseException as e:
        print("出错了", e)


sql_createtable = '''
create table stus(
STU_ID string primary key,
STU_NO string not null,
STU_NAME string not null,
STU_INFO string
);
'''
sql_insert = '''
insert into stus(STU_ID,STU_NO,STU_NAME,STU_INFO) values ('stu01','CME19061','fan','')
'''

create_table(sql_createtable)  # 创建数据表
insert_data(sql_insert)  # 插入数据
