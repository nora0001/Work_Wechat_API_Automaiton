import time
import requests

from work_wechat.contact.token import Weixin
import pystache

from work_wechat.contact.user import User
from work_wechat.contact.utlis import Utlis


class TestUser:
    depart_id=1
    @classmethod
    def setup_class(cls):
        #todo: create depart
        cls.user =User()


    def test_create(self):
        uid=str(time.time())
        data ={
            "userid": uid,
            "name": uid,
            "department": [self.depart_id]
        }
        r = self.user.create(data)

        print(r)
        # assert r['errcode']==0


    def test_create_by_template(self):
        # department_id=30
        uid = str(time.time_ns())
        mobile = str(time.time()).replace(".","")[0:11]
        data = str(Utlis.parse("user_create.json",{
            "userid": uid,
            "name": "Work_Shuaijie"+uid,
            "title": "master",
            "email": mobile+"qq.com",
            "mobile": mobile
            # "department": department_id
        }))
        data=data.encode("UTF-8")
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token" : Weixin.get_token()},
                          data=data,
                          headers={"content-type":"application/json; charset=UTF-8"}
                          ).json()
        print(r)   


    def test_list(self):
        r=self.user.list()

        r=self.user.list(department_id=65)

        print(r)


    def test_get_user(self):
        # print(Utlis.parse("user_create.json",{"name":"李四", "title": "校长", "mail": "1@1.com"}))
        uid = str(time.time_ns())
        mobile = str(time.time()).replace(".", "")[0:11]
        print(str(Utlis.parse("user_create.json",{
            "userid": uid,
            "name": "Work_Shuaijie"+uid,
            "title": "master",
            "email": mobile+"qq.com",
            "mobile": mobile
            # "department": department_id
        })))

