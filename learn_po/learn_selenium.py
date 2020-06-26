#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :learn_selenium.py
# @create by :2020/6/26 16:38
# @author    :liuyuqing
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service_log_path="log_selenium.log")

driver.get("http://www.baidu.com")
driver.maximize_window()
#全局等待  隐性等待
# driver.implicitly_wait(30)

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

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, id)))

handles = driver.window_handles
WebDriverWait(driver, 10).until(EC.new_window_is_opened(handles))
#关闭当前窗口
# driver.close()
#结束会话，关闭进程之类
driver.quit()

