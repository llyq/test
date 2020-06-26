#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_add.py
# @create by :2020/6/24 22:16
# @author    :liuyuqing

import unittest
import HTMLTestRunnerNew
import ddt
from log import MyLogger


# def add(num1, num2):
#     sum = num1 + num2
#     return sum

my_log = MyLogger()
test_data = [[1, 3], [4, 16]]

@ddt.ddt
class TestAdd(unittest.TestCase):

    def setUp(self):
        print("执行用例前置")

    @ddt.data(*test_data)
    @ddt.unpack
    def test_print_data(self, a, b):
        # my_log.info(a)
        # my_log.info(b)
        print(a)
        print(b)

    def test_add_two(self):
        result = add(1, 2)
        print(result)
        # 期望值与实际值比较，一般期望值放第一个 msg用例执行失败才展示
        try:
            self.assertEqual(3, result, "断言失败")
        except AssertionError as e:
            print("出错了 {}".format(e))
            raise e

    def test_add_two22(self):
        result = add(1, 2)
        print(result)
        # 期望值与实际值比较，一般期望值放第一个 msg用例执行失败才展示
        try:
            self.assertEqual(2, result, "断言失败")
        except AssertionError as e:
            print("出错了 {}".format(e))
            raise e

    def tearDown(self):
        print("执行用例后置")


if __name__ == '__main__':
    # unittest.main()
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
