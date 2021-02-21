import json
import random
import string
import time

import requests
import pytest
import logging

import urllib3

urllib3.disable_warnings()

class TestRequests(object):

    logging.basicConfig(level=logging.INFO)
    url = "https://testerhome.com/api/v3/topics.json?limit=2"

    def test_get(self):
        r = requests.get(self.url)
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))

    def test_post(self):
        r=requests.post(self.url,
                        headers={"a":"1","b":"b2"},
                        params={"a":1,"b":"string corntent"},
                        proxies={"https": "http://192.168.50.46:7778","http": "http://192.168.50.46:7778"},
                        verify =False
                        )
        print(r)

        # logging.info(r.url)
        # logging.info(r.text)
        # logging.info(json.dumps(r.json(),indent=2))

    def test_get_cookie(self):
        r=requests.get("https://httpbin.org/cookies")
        logging.info(r.url)
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))

    def test_xueqiu_quote(self):
        url= "https://101.201.175.228/v5/stock/portfolio/stock/list.json?"
        r=requests.get(url,
                       params={"category":"1"},
                       headers={"User-Agent":"Xueqiu Android 11.19"},
                       cookies={"u":"3446260770","xq_a_token":"5806a70c6bc5d5fb2b0978aeb1895532fffe502"})
        logging.info(r.url)
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))

    def test_creat_user(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/user/create?"
        r=requests.post(url,
                        access_token="")

    def test_get_access_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r=requests.get(url,
                       params={"corpid":"wwe5b7d33175284f5f","corpsecret":"FSWo2oKyBKgBFd1RxsfwK3LONb0XdFTuFcvvQRz4JLo"},
                       verify=False
                       ).json()

        print(r["access_token"])
        # logging.info(r.url)
        # logging.info(r.text)
        # logging.info(json.dumps(r.json(),indent=2))
        #
    def test_random(self):
        charat="\"_-@\""

        print("".join([random.choice(string.ascii_letters+"\"_-@\"")
                       if random.randint(0, 1)
                       else random.choice(string.digits)
                       for i in range(20)]))

#todo
"""
把部门，人员，消息推动，应用管理，素材，OA 的API 全部实现自动化测试
把代码上传到自己的github账号内
Allure2报告生成
"""

