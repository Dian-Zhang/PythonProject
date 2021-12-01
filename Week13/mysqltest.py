import pymysql

db = pymysql.connect(host='localhost', user='root', password='123', port=3306, db='student', charset="utf8")
cursor = db.cursor()
# sql = "select * from info"
# sql="select * from info where STU_NO='%s'"
# cursor.execute(sql)
# data=('001')
# cursor.execute(sql%data)
# sql = "update info set STU_AGE='%d' where STU_NO='%s'"
# sql = "insert into info values('%s','%s','%d')"
sql = "delete from info where STU_NO='%s'"
# sql="inset into info values ()"
# data = (30, '001')
# data=('SWE001','cai',27)
data = ('SWE001')
cursor.execute(sql % data)
db.commit()
print(cursor.rowcount)
cursor.close()
db.close()
# for row in cursor.fetchall():
#     print("学号：", row[0], "姓名：", row[1], "年龄:", row[2])
