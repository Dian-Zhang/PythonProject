import requests
from bs4 import BeautifulSoup


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


url = "https://www.bilibili.com/video/online.html"
html_str = get_html_text(url)
print("@@@@@@@@@@@@开始解析@@@@@@@@@@")
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
video_date = []  # 视频的发出时间
for item in node_href:
    video_url.append(str(item['href']).strip('//'))
    name = str(item['title'])
    video_name.append(name)
    # node_img = soup.find_all('img', alt=name)
    # for item_img in node_img:
    #     # print(item_img)
    #     video_img_url.append(str(item_img['src']))
# for item in node_views:
#     video_views.append(str(item.text).strip('\n '))
#     #
# for item in node_dm:
#     video_dm.append(str(item.text).strip('\n '))
#     #
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
    for item_date in node_video_date:
        video_date.append(str(item_date).split('<span>')[1][0:19])
    for item_views in node_video_views:
        video_views.append(str(item_views['title']).strip('总播放数'))
    for item_dm in node_video_dm:
        video_dm.append(str(item_dm['title']).strip('历史累计弹幕数'))
print("@@@@@@@@@@@@解析结束@@@@@@@@@@")
print("@@@@@@@@@@@@开始储存@@@@@@@@@@")

