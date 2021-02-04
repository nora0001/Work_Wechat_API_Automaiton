import logging
import time
import requests

from work_wechat.contact.token import Weixin
import pystache

from work_wechat.contact.user import User
from work_wechat.contact.utlis import Utlis


class TestUser:
    @classmethod
    def setup_class(cls):
        #todo: create depart
        cls.user =User()


    def test_create(self):
        uid=str(time.time_ns())
        data ={
            "userid": uid,
            "name": "Work_Shuaijie"+uid,
            "email":uid + "@testerhome.com"
        }
        r = self.user.create(data)
        logging.debug(r)
        assert r['errcode']==0


    def test_create_by_real(self):

        uid = str(time.time_ns())
        mobile = str(time.time()).replace(".","")[0:11]
        data = str(Utlis.parse("user_create.json",{
            "userid": uid,
            "name": "Tem_Shuaijie"+uid,
            "title": "master",
            "email": mobile+"qq.com",
            "mobile": mobile,
        }))
        data=data.encode("UTF-8")
        r=self.user.create(data=data)
        logging.debug(r)
        assert r['errcode']==0


    def test_list(self):
        r=self.user.list()
        logging.debug(r)
        # print(r)
        r = self.user.list(department_id=2)
        logging.debug(r)


    def test_get_user(self):
        # print(Utlis.parse("user_create.json",{"name":"李四", "title": "校长", "mail": "1@1.com"}))
        uid = str(time.time_ns())
        # mobile = str(time.time()).replace(".", "")[0:11]
        mobile = Utlis.udid()
        print(str(Utlis.parse("user_create.json",{
            "userid": uid,
            "name": "Work_Shuaijie"+uid,
            "title": "master",
            "email": mobile+"qq.com",
            "mobile": mobile,
        })))

