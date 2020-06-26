#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sample2.py
# @create by :2020/6/25 0:01
# @author    :liuyuqing

#反射
class GetData:
    cookie = '233'

setattr(GetData, 'cookie', 'rrrr') #直接修改类里的属性
print(GetData.cookie)
print(getattr(GetData, 'cookie'))  #获取属性对应的值
print(hasattr(GetData, 'cookie'))   #判断是否有这个属性值
delattr(GetData, 'cookie')
print(hasattr(GetData, 'cookie'))

