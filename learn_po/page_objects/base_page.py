#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :base_page.py
# @create by :2020/6/26 23:45
# @author    :liuyuqing
import logging
import datetime
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #等待元素可见
    def wait_element_visiable(self, locator, times=30, poll_frequency=0.5, doc=''):
        logging.info("等待元素{}可见".format(locator))
        try:
            #开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            #结束等待时间
            end = datetime.datetime.now()
            #求一个差值，写在日志中，等待了多长时间
            logging.info("等待结束。等待时长：{0}".format((end - start).seconds))
        except:
            logging.exception("等待元素可见失败！！！")
            self.save_screenshot(doc)
            raise

    #等待元素存在
    def wait_element_prensence(self):
        pass

    #查找元素
    def get_element(self, locator, doc=''):
        logging.info("查找元素{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！")
            self.save_screenshot(doc)
            raise

    #点击元素
    def click_element(self, locator, doc=''):
        element = self.get_element(locator, doc)
        logging.info("{0}点击元素{1}".format(doc, locator))
        try:
            element.click()
        except:
            logging.exception("点击元素失败！！！")
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self, locator, text, doc=''):
        element = self.get_element(locator, doc)
        logging.info("{0}输入元素{1}".format(doc, locator))
        try:
            element.send_keys(text)
        except:
            logging.exception("输入元素失败！！！")
            self.save_screenshot(doc)
            raise

    #读取元素的文本内容
    def get_text(self, locator, doc=''):
        element = self.get_element(locator, doc)
        try:
            return element.text
        except:
            logging.exception("读取元素的文本内容失败！！！")
            self.save_screenshot(doc)
            raise


    #获取元素属性
    def get_element_attribute(self, locator, doc=''):
        element = self.get_element(locator, doc)
        try:
            return element.get_attribute()
        except:
            logging.exception("获取元素属性失败！！！")
            self.save_screenshot(doc)
            raise

    #alert处理
    def alert_action(self, action='accept'):
        pass

    #iframe切换
    def switch_iframe(self, iframe, reference):
        pass

    #上传操作
    def upload_file(self):
        pass

    #滚动条处理
    #窗口切换

    #截图
    def save_screenshot(self, name):
        #图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        now = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
        file_name = "截屏存放的路径" + name + now
        self.driver.save_screenshot(file_name)
        logging.info("截取网页成功，文件路径为：{0}".format(file_name))















if __name__ == '__main__':
    start = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
    print(start)
    # time.sleep(1)
    # end = datetime.datetime.now()
    # print(end)
    # mistiming = (end - start).seconds
    # print(mistiming)
