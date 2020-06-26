#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :simple_example.py
# @create by :2020/6/23 0:15
# @author    :liuyuqing
import random

"""
s = "hello"
print(s.split())
"""

"""
price = int(input("请输入购买金额:"))
if 50 <= price <= 100:
    discount = 0.1
    amount = price * (1 - discount)
    print("折扣是：{}，最终需付款金额：{}".format(discount, amount))
elif price > 100:
    discount = 0.2
    amount = price * (1 - discount)
    print("折扣是：{}，最终需付款金额：{}".format(discount, amount))
else:
    print("无折扣，最终金额为{}".format(price))
"""

"""
number = random.randint(0, 9)
print(number)
"""

"""
a = {'age': 20,
     'name': '名称',
     'height': 1.60,
     'hourse': 'reading'}
print(a.values())
print(a.keys())
for item in a.values():
    print(item)
"""

"""
count = 0
for item in range(10):
    sex = input("请问你的性别是：")
    age = input("请问你的年龄是：")
    if 10 <= int(age) <= 20 and sex == 'f':
        count += 1
        print("恭喜你，符合加入我们足球队")
    else:
        print("很遗憾，你不满足我们的条件")
print("符合条件人数：{}".format(count))
"""

"""
L = [1, 3, 4, 5, 10, 8]
for i in range(2, 5):
    print(L[i])
"""

"""
sum = 0
for num in range(1, 101):
    sum  = sum + num
print(sum)
"""

"""
lines = int(input("请输入行数："))
for line in range(lines+1):
    print("*" * line)
"""

"""
sum = 0
a = 0
while a <= 100:
    sum = sum + a
    a += 1
print(sum)
"""

"""
count = 0
i = int(input("请输入询问次数："))
while True:
    i -= 1
    sex = input("请问你的性别是：")
    age = input("请问你的年龄是：")
    if 10 <= int(age) <= 20 and sex == 'f':
        count += 1
        print("恭喜你，符合加入我们足球队")
    else:
        print("很遗憾，你不满足我们的条件")
    if i == 0:
        break
    else:
        continue
print("符合条件人数：{}".format(count))
"""

"""
new_number = ''
number = input("请输入四位数：")
for item in number:
    num = int(item) + 5
    new_number += str(num)
print(new_number[::-1])
"""

def sum(*args):
    return args

def sum_kw(**kwargs):
    return kwargs

print(sum(1,2,3,4))
print(sum_kw(name='name', aa=1))

import os
print(os.getcwd())
print(os.path.realpath(__file__))
new_path = os.path.join(os.getcwd(), 'mulu01\jibie01', 'wenjian01')
print(new_path)
print(os.path.isfile(os.getcwd()))
print(os.path.exists(new_path))
print(os.path.lexists(os.getcwd()))
print(os.listdir(os.getcwd()))

