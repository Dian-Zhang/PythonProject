import matplotlib.pyplot as plt
import pymysql
import math
import pylab

db = pymysql.connect(host='localhost', user='root', password='123', port=3306, db='my python final work')
cursor = db.cursor()
# the first is 每个时间段前二十个视频的在线人数
sql = "select * from total_avg_people"
cursor.execute(sql)
print(cursor.rowcount)
total = []
avg_people = []
time = []
# 需要调正这个参数
flag = 1
for row in cursor.fetchall():
    if flag < 74:
        total.append(row[0])
        avg_people.append(row[1])
        time.append(str((row[3])))
    flag += 1
print(total)
print(avg_people)
print(time)
# 开始画图
plt.rcParams['font.sans-serif'] = ['kaiTi']
plt.figure(figsize=(100, 25))
plt.title("每个时间点的在线人数")
plt.xlabel("时间点")
plt.ylabel("视频在线人数")
plt.ylim(int(min(total) / 1000) * 1000, math.ceil(max(total) / 1000) * 1000)
plt.plot(time, total, color="red", linewidth=1.5, linestyle='-')
plt.legend(labels=["总人数"], loc="best")
pylab.xticks(rotation=15)
# plt.savefig('D:\Devp\PycharmProjects\pythonProject\PythonFinally\webapp\static\img\activity.png')
plt.show()
db.close()
