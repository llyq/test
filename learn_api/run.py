#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :run.py
# @create by :2020/6/26 22:28
# @author    :liuyuqing

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestAdd))

# file = open("test.txt", "w+", encoding='UTF-8')
# 执行上下文管理器
# with open("test.txt", "w+", encoding='UTF-8') as file:
#     runner = unittest.TextTestRunner(stream=file, verbosity=2)  #0  1  2最详细
#     runner.run(suite)
# print(file.closed)
with open("../../test_report.html", "wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="测试报告title", description="测试报告desc",
                                              tester="雨晴")
    runner.run(suite)
