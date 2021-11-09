import re
import urllib

import requests
from bs4 import BeautifulSoup

h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/95.0.4638.54 Safari/537.36'
}
html_str = requests.get('https://movie.douban.com/top250', headers=h).text
# print(html_str)
soup = BeautifulSoup(html_str, 'html.parser')
movie_names = soup.find_all('div', class_='hd')
nums = soup.find_all("span", class_='rating_num', property='v:average')
for a in range(len(movie_names)):
    print("电影名:", movie_names[a].text.replace("\n", "").split('/')[0], "评分:", nums[a].text)
imgs = soup.find_all("img", src=re.compile("doubanio.com/view"))
for b in range(len(imgs)):
    # print(imgs[b]['src'])
    urllib.request.urlretrieve(imgs[b]['src'], './imgss/'+"%s.jpg" % movie_names[b].text.replace("\n", "").split('/')[0])


