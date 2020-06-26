#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :learn_requests.py
# @create by :2020/6/25 14:38
# @author    :liuyuqing

import requests

class HttpRequests:

    def http_request(self, url, method, data=None, header=None, cookie=None):
        try:
            if method.upper() == 'GET':
                response = requests.get(url=url, params=data, headers=header, cookies=cookie)
            elif method.upper() == 'POST':
                response = requests.post(url=url, headers=header, json=data, cookies=cookie)
            else:
                print("请求方法错误")
        except Exception as e:
            print("请求错了{0}".format(e))
            raise e
        return response


if __name__ == '__main__':

    http_requests = HttpRequests()
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": "org=b9574fe5068f3d2da803da49da763ee2"
    }

    login_url = "http://test.erp.qipeidao.com/bs/user/login"
    login_data = {"corporationId":1,"loginName":"liuyuqing","password":"123"}

    login_brand_url = "http://test.erp.qipeidao.com/bs/user/setFactoryBrand?factoryBrandId=1"

    query_parts_url = "http://test.erp.qipeidao.com/bs/parts/query"
    query_parts_data = {"bookGoodsCategoryName":"","carType":"","isSales":0,"partsBrandName":"","imageNum":"","partsCode":"","pyFirstLetter":"","state":"","partsImageState":"","mnemonicCode":"","pageDTO":{"pageSize":50,"pagination":0}}

    # s = requests.session()
    resp1 = http_requests.http_request(url=login_url, data=login_data, method='post', header=headers)
    resp2 = http_requests.http_request(url=login_brand_url, method='get', header=resp1.cookies)
    resp3 = http_requests.http_request(url=query_parts_url, method='post', data=query_parts_data, header=headers, cookie=resp2.request.headers)
    print(resp1.text)
    print(resp2.text)
    print(resp3.text)
    print(resp2.request.headers)