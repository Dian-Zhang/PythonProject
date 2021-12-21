import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

i = 0
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
while True:
    url = 'http://jw.xujc.com/student/index.php?c=Xk&a=List&id=919'
    c = {
        "jgxy_jw_user": "CME19061",
        "jgxy_jw_lb": "%D1%A7%C9%FA",
        "PHPSESSID": "qkb5vieqk3ovjs4a0uuasv7ve0",
        "jwimgcode": "8f5eefd39836b8ae5f177f434f2888b8.1640072070"
    }
    # 进入浏览器设置
    options = webdriver.ChromeOptions()
    # 更换头部
    options.add_argument(h)
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    browser.add_cookie(c)
    browser.refresh()
    content = browser.page_source
    print(content)
    time.sleep(600)
