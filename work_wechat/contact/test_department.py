import datetime
import logging
import os

import pytest
import requests

from work_wechat.contact.token import Weixin
from work_wechat.contact.utlis import Utlis

logging.getLogger().setLevel(logging.INFO)

class TestDepartment:

    def test_create_name(self,token):
        data = {
            "name": "Wechat_SS" + str(datetime.datetime.now().timestamp()),
            "parentid": 1,
        }

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token},
                          json=data
                          ).json()
        # logging.debug(r)
        print(r)

    @pytest.mark.parametrize("name", [
        "广州研发中心",
        "東京アニメ研究所",
        "도쿄애니메이션연구소",
        "Am institut für außerirdische technologie",
        "Институт аниме в токио"
    ])
    def test_create_order(self, name,token):
        data = {
            "name": name+Utlis.udid(),
            "parentid": 1,
            "order": 1,
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token},
                          json=data
                          ).json()
        logging.debug(r)


    def test_get(self,token):
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                     params={"access_token":token}
                     ).json()
        # logging.debug(r)
        print(r)
        logging.info("hello world:{}")
