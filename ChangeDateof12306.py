'''
待解决问题：选了日期后，要选查询按钮时因日历把按钮遮挡了，所以要随便点下页面的label比如
“出发日期”后再点“查询”。
'''
#coding = utf-8 
import time
from selenium import webdriver
#from selenium.webdriver.support.wait import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
maxwindow = driver.maximize_window()
driver.get('https://www.12306.cn/index/')
time.sleep(3)
train_dateEle = driver.find_element_by_id('train_date')
js='document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
time.sleep(3)
train_dateEle.clear()
time.sleep(3)
train_dateEle.send_keys('2020-03-05')

'''
#去掉readonly属性，两种js书写方法都正确
js='document.getElementById("train_date").removeAttribute("readonly");' #javascript的document对象方式
#js = "$('input[id=train_date]').removeAttr('readonly')" #css定位方式
driver.execute_script(js)
date_element = driver.find_element_by_id('train_date')
date_element.click()
time.sleep(2)
date_element.clear()
time.sleep(2)
date_element.send_keys('2020-01-23')
time.sleep(2)
'''