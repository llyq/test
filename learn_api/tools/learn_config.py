#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :learn_config.py
# @create by :2020/6/25 13:49
# @author    :liuyuqing

import configparser

config = configparser.ConfigParser()
config.read('case.config', encoding='UTF-8')

#读取配置文件数据
data = config.get('section1', 'option11')
print(data)

data1 = config['section2']['option21']
print(data1)

print(config.sections())
print(config.items('section1'))