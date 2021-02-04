import json
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
    def test_create_user(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create?"
        r=requests.post(url,
                        data={
    "userid": "zhangsan",
    "name": "张画",
    "alias": "jackzhang",
    "mobile": "+86 13800000000",
    "department": [1, 2],
    "order":[10,40],
    "position": "产品经理",
    "gender": "1",
    "email": "zhangsan@gzdev.com",
    "is_leader_in_dept": [1, 0],
    "enable":1,
    "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
    "telephone": "020-123456",
    "address": "广州市海珠区新港中路",
    "main_department": 1,
    "extattr": {
        "attrs": [
            {
                "type": 0,
                "name": "文本名称",
                "text": {
                    "value": "文本"
                }
            },
            {
                "type": 1,
                "name": "网页名称",
                "web": {
                    "url": "http://www.test.com",
                    "title": "标题"
                }
            }
        ]
    },
    "to_invite": "true",
    "external_position": "高级产品经理",
    "external_profile": {
        "external_corp_name": "企业简称",
        "external_attr": [
            {
                "type": 0,
                "name": "文本名称",
                "text": {
                    "value": "文本"
                }
            },
            {
                "type": 1,
                "name": "网页名称",
                "web": {
                    "url": "http://www.test.com",
                    "title": "标题"
                }
            },
            {
                "type": 2,
                "name": "测试app",
                "miniprogram": {
                    "appid": "wx8bd8012614784fake",
                    "pagepath": "/index",
                    "title": "my miniprogram"
                }
            }
        ]
    }
},
params=
{"access_token":"Z1UpuQL3D7eH27sfEr4b5Vw6i_dVAwBvhcssmaX7Ulc-z9z0O-0cut6DqKXaWRAH_er_T3abwDtSfgT1w4-J2Y1VaBv_GKWToJFVx-OcmViadtKB6BdNn122xcDRy1IccwkQ4wnr_3B_QXC9Km8jhrDA0_Zc2xUOftIrWH4_22N1d_J4tI_EqwDxOdSBpbqFQw70GplIKOc9gr36bMwUfg"},
proxies = {"https": "http://192.168.50.46:7778", "http": "http://192.168.50.46:7778"}
)

    def test_case(self):
        print(str(time.time_ns()))

