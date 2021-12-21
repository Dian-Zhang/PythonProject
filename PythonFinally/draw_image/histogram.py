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
i = 1
for row in cursor.fetchall():
    video_name.append("(" + str(i) + ")" + row[4])
    video_online_people.append(int(row[6]))
    i += 1
print(video_online_people)
print(video_name)
# 开始准备画图
plt.rcParams['font.sans-serif'] = ['kaiTi']
plt.figure(figsize=(17, 17))
plt.title("在线人数")
plt.xlabel("UP主名称")
plt.ylabel("视频在线人数")
plt.ylim(int(video_online_people[19] / 1000) * 1000, math.ceil(video_online_people[0] / 1000) * 1000)
color = "red"
plt.bar(video_name, video_online_people, color=color, width=0.3, linewidth=1.0, linestyle="--")
pylab.xticks(rotation=15)
# 为每个条形图添加数值标签
for a, b in zip(video_name, video_online_people):
    plt.text(a, b, b, ha='center', va='bottom', )
plt.savefig('D:\Devp\PycharmProjects\pythonProject\PythonFinally\webapp\static\img\hist.png')
plt.show()
db.close()
