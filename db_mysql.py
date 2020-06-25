#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :db_mysql.py
# @create by :2020/6/25 21:05
# @author    :liuyuqing
import mysql.connector
from learn_config import

class DbMysql:

    def db_mysql(self, query_sql, state='all'):
        config = configparser.ConfigParser()
        config.read('case.config', encoding='UTF-8')
        db_config = config.get('db', 'db_config')
        cnn = mysql.connector.connect(**db_config)

        cursor = cnn.cursor()
        cursor.execute(query_sql)
        if state == 1:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()

        cursor.close()
        cnn.close()






