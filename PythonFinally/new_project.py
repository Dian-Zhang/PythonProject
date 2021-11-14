import html

import requests
from bs4 import BeautifulSoup
import json
import time
import random


def get_html_text(url):
    try:
        h = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/68.0.3440.106 Safari/537.36'
             }
        r = requests.get(url, headers=h, timeout=3000)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("异常:", e)
        return str(e)


def pushplus(content):
    token = '8c74fd69375a4210b7f8f48ba92d55b6'  # 在pushpush网站中可以找到
    title = 'My Python Final Project'  # 改成你要的标题内容
    content = content  # 改成你要的正文内容
    url = 'http://pushplus.hxtrip.com/send'
    data = {
        "token": token,
        "title": title,
        "content": content,
        # "template": json
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/html'}
    res = requests.post(url, data=body, headers=headers)
    return res


# print("@@@@@@@@@@@@开始储存@@@@@@@@@@")
# print("@@@@@@@@@@@@结束储存@@@@@@@@@@")
video_records = []  # 所有视频纪录的信息
while True:
    print("@@@@@@@@@@@@开始解析@@@@@@@@@@")
    url = "https://www.bilibili.com/video/online.html"
    html_str = get_html_text(url)

    soup = BeautifulSoup(html_str, 'html.parser')
    node_href = soup.find_all('a', target='_blank')
    node_views = soup.find_all('span', class_='play')
    node_dm = soup.find_all('span', class_='dm')
    node_author = soup.find_all('a', target='blank')
    node_online_people = soup.find_all('p', class_='ol')
    video_url = []  # 视频地址
    video_name = []  # 视频名字
    # video_img_url = []  # 视频图片地址
    video_views = []  # 视频观看人数
    video_dm = []  # 视频弹幕数
    video_author = []  # 视频作者名字
    video_author_homepage = []  # 视频作者主页
    video_online_people = []  # 视频在线观看人数
    # video_date = []  # 视频的发出时间
    temp_video_records = []  # 所有视频纪录的信息
    for item in node_href:
        video_url.append(str(item['href']).strip('//'))
        name = str(item['title'])
        video_name.append(name)
        # node_img = soup.find_all('img', alt=name)
        # for item_img in node_img:
        #     print("@@@")
        #     print(item_img['src'])
        #
        #     video_img_url.append(str(item_img['src']))
    for item in node_views:
        video_views.append(str(item.text).strip('\n '))
        #
    for item in node_dm:
        video_dm.append(str(item.text).strip('\n '))
        #
    for item in node_author:
        video_author.append(str(item.text).strip('\n '))
        video_author_homepage.append(str(item['href']).strip('/'))
        #
    for item in node_online_people:
        video_online_people.append(str(item.text).strip('\n ').strip('人在看'))  # 这里为了保持观看人数是数字
        #
    for item_url in video_url:
        soup_video = BeautifulSoup(get_html_text('http://' + item_url), 'html.parser')
        node_video_date = soup_video.find_all('div', class_='video-data')
        node_video_views = soup_video.find_all('span', class_='view')
        node_video_dm = soup_video.find_all('span', class_='dm')
        # for item_date in node_video_date:
        #     print(item_date)
        #     temp_item_date = str(item_date).split('<span>')[1][0:19]
        #     # print(temp_item_date)
        #     # if temp_item_date == ' ':
        #     #     video_date.append("番剧无时间")
        #     # else:
        #     video_date.append(temp_item_date)
    for item_views in node_video_views:
        video_views.append(str(item_views['title']).strip('总播放数'))
        # print(str(item_views['title']))
    for item_dm in node_video_dm:
        video_dm.append(str(item_dm['title']).strip('历史累计弹幕数'))
    for i in range(len(video_url)):
        temp = {}
        temp.update({'video_url': video_url[i]})
        temp.update({'video_name': video_name[i]})
        temp.update({'video_views': video_views[i]})
        temp.update({'video_dm': video_dm[i]})
        temp.update({'video_author': video_author[i]})
        temp.update({'video_author_homepage': video_author_homepage[i]})
        temp.update({'video_online_people': video_online_people[i]})
        # temp.update({'video_date': video_date[i]})
        temp_video_records.append(temp)
    # 如果满足一定的条件就开始推推送
    print("@@@@@@@@@@@@开始推送@@@@@@@@@@")
    video_records = temp_video_records
    html = '<table style="width:100%;background-color:#60D978;">'
    # html += "<img src='" + "'" + "/>"
    html += '<tr><th colspan="2">' + "观看列表排行榜" + '</th></tr>'
    num = 1
    color = ['#f58f98', '#f05b72', '#f391a9', '#b2d235', '#cde6c7', '#a1a3a6', '#7bbfea', '#f7acbc', '#deab8a',
             '#817936']
    tablecolor = ['#94d6da', '#feeeed']
    flag = False
    for dict_item in video_records:
        my_div_color = color[random.randint(0, 9)]
        html += '<tr>'
        html += '<th rowspan="3" style="width:20px" bgcolor="' + color[random.randint(0, 9)] + '">' + str(
            num) + '</th>'
        html += '<td bgcolor="' + tablecolor[flag] + '">' + dict_item['video_name'] + '</td>'
        html += '</tr>' + '<tr>'
        html += '<td bgcolor="' + tablecolor[flag] + '">' + "当前在线人数:" + dict_item[
            'video_online_people'] + '</td>'
        html += '</tr>' + '<tr>'
        html += '<td bgcolor="' + tablecolor[flag] + '">' + "<a href='" + "http://" + dict_item[
            'video_url'] + "'>" + "点此链接观看" + "</a>" + '</td>'
        html += '</tr>'
        num = num + 1
        if flag:
            flag = False
        else:
            flag = True
    html += '</table>'
    print(html)
    # print(video_date)
    content = html
    res = pushplus(content)
    if res.status_code == 200:
        print("@@@@@@@@@@@@结束推送@@@@@@@@@@")
    time.sleep(1200)
