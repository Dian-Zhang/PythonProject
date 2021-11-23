import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # path是你自己的chrome浏览器的文件路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(options=chrome_options)
    return browser


i = 0
while True:
    url = 'https://www.xujc.com'
    # html_str = get_html_text(url)
    # print(html_str)
    # time.sleep(0.3)
    browser = share_browser()
    # 有界面
    # path = 'chromedriver.exe'
    # browser = webdriver.Chrome(path)
    browser.get(url)
    # content = browser.page_source
    # print(content)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "第" + str(i) + "次访问")
    i += 1
