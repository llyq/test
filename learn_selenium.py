#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :learn_selenium.py
# @create by :2020/6/26 16:38
# @author    :liuyuqing
import time
from selenium import webdriver

driver = webdriver.Chrome(service_log_path="log_selenium.log")

driver.get("http://www.baidu.com")
driver.maximize_window()
# driver.get("http://www.taobao.com")
# time.sleep(1)
# driver.back()
# time.sleep(1)
# driver.forward()
# time.sleep(1)
# driver.refresh()
# time.sleep(1)
# print(driver.title)
# print(driver.current_url)
# print(driver.current_window_handle)
ele = driver.find_element_by_id('kw')
print(ele)
print(ele.get_attribute('class'))

#关闭当前窗口
# driver.close()
#结束会话，关闭进程之类
driver.quit()

