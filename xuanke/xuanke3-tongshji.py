import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random

url = "http://jw.xujc.com/"
b = webdriver.Chrome()
b.get(url)
b.find_element(By.ID, "username").send_keys("CME19061")
b.find_element(By.ID, "password").send_keys("gaofan666")
imgcode = input("请输入验证码 : ")
b.find_element(By.ID, "imgcode").send_keys(imgcode)

ActionChains(b).click(b.find_element(By.ID, "loginbtn")).perform()
# print(str(b.page_source))
time.sleep(1)
b.find_element_by_link_text('选课报名').click()
b.find_element_by_link_text('选课').click()
time.sleep(1)
b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[2]/td[9]/input').click()
i = 0

while True:
    # 进入第4页(艺术导论)
    b.find_element_by_xpath('//*[@id="data_table"]/tfoot/tr/td/a[3]').click()
    max_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[5]/td[7]').text
    selected_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[5]/td[8]/span').text
    if eval(max_people) - eval(selected_people) > 0:
        b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[5]/td[9]').click()
        # 接收弹窗
        b.find_element_by_id("confirm").click()
        b.switch_to.alert.accept()
        b.find_element_by_xpath('//*[@id="page-nav"]/table/tbody/tr/td[1]/input[2]').click()
        time.sleep(random.randint(3, 5))
    # 进入第5页(劳动通论)
    b.find_element_by_xpath('//*[@id="data_table"]/tfoot/tr/td/a[4]').click()
    max_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[25]/td[7]').text
    selected_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[25]/td[8]').text
    if eval(max_people) - eval(selected_people) > 0:
        b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[25]/td[9]').click()
        # 接收弹窗
        b.find_element_by_id("confirm").click()
        b.switch_to.alert.accept()
        b.find_element_by_xpath('//*[@id="page-nav"]/table/tbody/tr/td[1]/input[2]').click()
        time.sleep(random.randint(3, 5))
    # 进入第6页(用经济学智慧解读中国)
    b.find_element_by_xpath('//*[@id="data_table"]/tfoot/tr/td/a[4]').click()
    max_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[45]/td[7]').text
    selected_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[45]/td[8]').text
    if eval(max_people) - eval(selected_people) > 0:
        b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[25]/td[9]').click()
        # 接收弹窗
        b.find_element_by_id("confirm").click()
        b.switch_to.alert.accept()
        b.find_element_by_xpath('//*[@id="page-nav"]/table/tbody/tr/td[1]/input[2]').click()
        time.sleep(random.randint(3, 5))
    # 大学生健康教育
    max_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[55]/td[7]').text
    selected_people = b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[55]/td[8]').text
    if eval(max_people) - eval(selected_people) > 0:
        b.find_element_by_xpath('//*[@id="data_table"]/tbody/tr[55]/td[9]').click()
        # 接收弹窗
        b.find_element_by_id("confirm").click()
        b.switch_to.alert.accept()
        b.find_element_by_xpath('//*[@id="page-nav"]/table/tbody/tr/td[1]/input[2]').click()
        time.sleep(random.randint(3, 5))

    #
    # b.find_element_by_xpath('//*[@id="data_table"]/tfoot/tr/td/a[3]').click()
    time.sleep(random.uniform(0.8, 1.5))
    i = i + 1
    # cur_time = time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime())
    dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')  # 含微秒的日期时间，来源 比特量化
    print(dt_ms + ": 正在可爱第" + str(i) + "次！！")
