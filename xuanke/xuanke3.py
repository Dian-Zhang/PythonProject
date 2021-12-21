import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random

url = "http://jw.xujc.com/"
b = webdriver.Chrome()
b.get(url)
b.find_element(By.ID, "username").send_keys("CME19061")
b.find_element(By.ID, "password").send_keys("gf123456")
imgcode = input("请输入验证码 : ")
b.find_element(By.ID, "imgcode").send_keys(imgcode)

ActionChains(b).click(b.find_element(By.ID, "loginbtn")).perform()
# print(str(b.page_source))
time.sleep(1)
b.find_element_by_link_text('选课报名').click()
b.find_element_by_link_text('选课').click()
time.sleep(1)
b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[4]/td[9]/input').click()
i = 0
while True:
    max_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[13]/td[7]').text
    selected_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[13]/td[8]/span').text
    if eval(max_people) - eval(selected_people) > 0:
        b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[13]/td[9]').click()
    b.find_element_by_xpath('//*[@id="page-nav"]/table/tbody/tr/td[1]/input[2]').click()
    time.sleep(random.randint(1, 3))
    i = i + 1
    cur_time = time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime())
    print(cur_time + ": 已进行" + str(i) + "次抢课！！")
