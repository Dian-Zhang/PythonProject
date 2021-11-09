# 爬豆瓣电影Top250的25部电影名称和评分 爬虫和抓取部分，待补充存储部分代码
def get_html_text(url):
    try:
        h = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/68.0.3440.106 Safari/537.36'
             }
        r = requests.get(url, headers=h, timeout=3000)
        r.raise_for_status()  # 如果不是200，则引发HTTPError异常
        r.encoding = r.apparent_encoding  # 根据内容去确定编码格式
        return r.text
    except BaseException as e:
        print("出现异常：", e)
        return str(e)


#  爬虫代码
import requests
from bs4 import BeautifulSoup
import re
import csv
import openpyxl as ol

print("开始爬虫")
url = "https://movie.douban.com/top250"
html_text = get_html_text(url)
print("开始解析")
soup = BeautifulSoup(html_text, 'html.parser')
node = soup.find_all("span", class_="title")
node2 = soup.find_all("span", class_="rating_num")
name_list = []  # 存电影名称
score_list = []  # 存电影评分

for i in node:
    mname = i.string.strip()  # 移除字符串前后空格
    if mname[0] == '/':
        # if mnane.startswith('/'):
        continue
    name_list.append(mname)
for j in node2:
    score = j.string
    score_list.append(score)
for k in range(0, len(name_list)):
    print(name_list[k], score_list[k])


def write_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


data = []
filename = 'test.csv'
wb2 = ol.Workbook()
st2 = wb2.active
st2['A1'] = "电影排行榜"
st2.merge_cells('A1:B1')
st2.append(['名称', '评分'])
for k in range(0, len(name_list)):
    print(name_list[k], score_list[k])
    # data.append([name_list[k], score_list[k]])
    st2.append([name_list[k], score_list[k]])
# write_csv(filename, data)
wb2.save('new.xlsx')
