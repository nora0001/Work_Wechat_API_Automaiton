import datetime
import logging
import os
import re

import pytest
import requests
from regex import Regex

from work_wechat.contact.department import Department
from work_wechat.contact.token import Weixin
from work_wechat.contact.user import User
from work_wechat.contact.utlis import Utlis


logging.getLogger().setLevel(logging.INFO)

class TestDepartment:

    @classmethod
    def setup_class(cls):
        cls.depart=Department()

    def test_create_t001(self):
        data = {
            "name": "Wechat_SS" + str(datetime.datetime.now().timestamp()),
            "parentid": 1,
        }
        r = self.depart.create(data)
        logging.debug(r)
        assert r["errcode"]==0

    @pytest.mark.parametrize("name", [
        "广州研发中心",
        "東京アニメ研究所",
        "도쿄애니메이션연구소",
        "Am institut für",
        "Институт аниме"
    ])
    def test_create_order_t002(self, name):
        data = {
            "name": name+Utlis.udid(),
            "parentid": 1,
            "order": 1,
        }
        r = self.depart.create(data)
        logging.debug(r)
        assert r["errcode"]==0


    def test_get_list_t003(self):
        r=self.depart.get_list()
        logging.debug(r)
        logging.info("hello world:{}")
        assert r["errcode"]==0


    def test_update_t004(self):
        pass

    def test_delete_positive_t005(self):
        departid="5"
        r=self.depart.delete(departid)
        logging.info(r)
        assert r["errcode"]==0

    @pytest.mark.parametrize("departid", [
        "1","2","50"
    ])
    def test_delete_negative_depart_t006(self,departid):
        r = self.depart.delete(departid)
        logging.info(r)
        assert r["errcode"]==60005
        errmsg=re.findall("department contains user",r["errmsg"])
        if len(errmsg):
            assert errmsg[0]== "department contains user"

    def test_update_t007(self):
        data= {
            "id": 6,
            "name": "企划事业部",
            "name_en": "QHSY",
            "parentid": 2,
            "order": 1
        }
        r=self.depart.update(data)
        logging.info(r)
        assert r["errcode"]==0
