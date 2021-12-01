import pymysql

db = pymysql.connect(host='localhost', user='root', password='123', port=3306, db='spiders')
cursor = db.cursor()
sql = 'create table if not exists student(id varchar(255) not null,name varchar(255) not null,age int not null,' \
      'primary key(id)) '
cursor.execute(sql)
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# <class 'pymysql.connections.Connection'>
# print(type(db))
# <class 'pymysql.cursors.Cursor'>
# print(type(cursor))
# cursor.execute("CREATE DATABASE spiders DEFAULT  CHARACTER SET utf8")
db.close()
