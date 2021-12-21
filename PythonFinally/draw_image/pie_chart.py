import matplotlib.pyplot as plt
import pymysql
import math
import pylab

db = pymysql.connect(host='localhost', user='root', password='123', port=3306, db='my python final work')
cursor = db.cursor()
# the first is 每个时间段前二十个视频的在线人数
sql = "select * from watch_list where watch_list_id=3"
cursor.execute(sql)
print(cursor.rowcount)
video_online_people = []
video_name = []
for row in cursor.fetchall():
    video_name.append(row[4])
    video_online_people.append(int(row[6]))
print(video_online_people)
print(video_name)
sql = "select * from system_time_to_watch_list where watch_list_id=3"
cursor.execute(sql)
title = []
for row in cursor.fetchall():
    title.append(str(row[0]))
print(title)
# 开始画图
plt.rcParams['font.sans-serif'] = ['kaiTi']
fig1, ax1 = plt.subplots()
ax1.pie(video_online_people, labels=video_name, autopct='%.1f%%', pctdistance=0.9, radius=30)
ax1.axis('equal')
plt.title(title)
plt.savefig('D:\Devp\PycharmProjects\pythonProject\PythonFinally\webapp\static\img\pie.png')
plt.show()
db.close()
