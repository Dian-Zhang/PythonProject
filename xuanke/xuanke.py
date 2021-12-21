import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

def get_html_text(url):
    try:
        h = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,ja-CN;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "jgxy_jw_user=CME19061; jgxy_jw_lb=%D1%A7%C9%FA; PHPSESSID=qkb5vieqk3ovjs4a0uuasv7ve0; jwimgcode=8f5eefd39836b8ae5f177f434f2888b8.1640072070",
            "Host": "jw.xujc.com",
            "Referer": "http://jw.xujc.com/student/index.php?c=ZzyKh&a=index",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }

        r = requests.get(url, headers=h, timeout=4000)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("异常:", e)
        return str(e)


while True:
    url = "http://jw.xujc.com/student/index.php?c=Xk&a=List&id=919"
    html_str = get_html_text(url)
    print(html_str)
    soup = BeautifulSoup(html_str, 'html.parser')

    time.sleep(1200)
