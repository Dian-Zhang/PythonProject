import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['kaiTi']
plt.title("电影")
plt.xlabel("电影名称")
plt.ylabel("电影评分")
plt.ylim(5, 10)
x = ['A', 'B', 'C', 'D']
y = [9.7, 9, 7.6, 80]
exploevalue = (0.1, 0.1, 0.1, 0.1)
fig1, ax1 = plt.subplots()
ax1.pie(y, labels=x, explode=exploevalue, autopct='%.1f%%')
ax1.axis('equal')
# plt.plot(x, y, color='blue', linewidth=2.0, linestyle='-')
# plt.bar(x, y, color='grey', width=0.25, linewidth=2.0, linestyle='--')
# plt.legend(labels=['评分1', '评分2'], loc='best')
plt.show()
