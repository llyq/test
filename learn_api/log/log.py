#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :log.py
# @create by :2020/6/25 19:36
# @author    :liuyuqing
import logging

# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error00")
# logging.critical("critical")
class MyLogger:

    def my_log(self,  msg, level):
        #定义日志收集器
        my_logger = logging.getLogger("name")
        #定义收集级别
        my_logger.setLevel('DEBUG')
        #设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        #创建输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('ERROR')
        ch.setFormatter(formatter)
        fh = logging.FileHandler('testlog.txt', encoding='UTF-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)
        #两者对接，收集与输出
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        #收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def error(self, msg):
        self.my_log(msg, 'ERROR')


if __name__ == '__main__':
    # MyLogger().my_log("dfjdsf", 'ERROR')
    # MyLogger().my_log("11", 'ERROR')
    # MyLogger().my_log("2233", 'ERROR')
    my_logger = MyLogger()
    my_logger.info("234234")
    my_logger.debug("ehfj")
    my_logger.error("errprrrr")