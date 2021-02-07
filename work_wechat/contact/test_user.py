import logging
import time
import requests

from work_wechat.contact.token import Weixin
import pystache

from work_wechat.contact.user import User
from work_wechat.contact.utlis import Utlis


class TestUser:
    depart_id = 30
    @classmethod
    def setup_class(cls):
        #todo: create depart
        cls.user =User()

    def test_create_user_t001(self):

        uid=str(time.time_ns())
        mobile = str(time.time()).replace(".", "")[0:11]
        data ={
            "userid": uid,
            "name": "Good_Shuaijie"+uid,
            "title":"master",
            "department":[self.depart_id],
            "email":mobile + "@testerhome.com",
            "mobile":mobile
        }
        r = self.user.create(data)
        logging.debug(r)
        assert r['errcode']==0


    def test_create_user_by_real_t002(self):

        useid = str(time.time_ns())
        mobile = str(time.time()).replace(".","")[0:11]
        department=26
        data = str(Utlis.parse("user_create.json",{
            "uid": useid,
            "name": "WeWork_SR_"+useid,
            "title": "master",
            "mail": mobile+"@163.com",
            "phone": mobile,
            "depart":department
        }))
        data=data.encode("UTF-8")
        print(data)
        r=self.user.create(data=data)
        logging.debug(r)
        assert r['errcode']==0


    def test_get_user_t003(self):
        # print(Utlis.parse("user_create.json",{"name":"李四", "title": "校长", "mail": "1@1.com"}))
        useid = str(time.time_ns())
        mobile = Utlis.udid()
        department=30
        print(str(Utlis.parse("user_create.json",{
            "uid": "Work_Shuaijie" + useid,
            "name": "WeWork_SR",
            "title": "master",
            "mail": mobile + "@163.com",
            "phone": mobile,
            "depart": department
        })))



    def test_update_user_by_real_t004(self):
        uid = "1612596889998873500"
        department = 10
        mobile = str(time.time()).replace(".", "")[0:11]

        data = str(Utlis.parse("user_update.json", {
            "uid": uid,
            "name": "Work_Shuaijie" + uid,
            "title": "master",
            "mail": mobile + "@126.com",
            "phone": mobile,
            "depart": department
        }))
        data = data.encode("UTF-8")
        r=self.user.update(self,data=data)
        logging.info(r)
        assert r["errcode"]==0

    def test_update_user_t005(self):
        uid = "zhangsan"
        department = 10
        mobile = str(time.time()).replace(".", "")[0:11]

        data = {
            "userid": "zhangsan",
            "name": "Work_Shuaijie" + uid,
            "position": "master",
            "email": mobile + "@126.com",
            "mobile": mobile,
        }
        print(data)
        print(type(data))
        r= requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/update",
                             params={"access_token": Weixin.get_token()},
                             data=data
                             ).json()
        # r = self.user.update(self, data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_delete_user_t006(self):
        #todo how to automatically get useid to be deleted
        uid="Tem_Shuaijie1612447178564264600"
        r= self.user.delete(uid=uid)
        logging.info(r)
        assert r['errcode'] == 0


    def test_bulk_delete_user_t007(self):
        data={
            "useridlist": ["Tem_Shuaijie1612448710225424300", "Tem_Shuaijie1612449266812698800"]
            }
        r=self.user.bulk_delete(data)

        logging.info(r)
        assert r["errcode"]==0

    def test_samplelist_t008(self):
        r = self.user.depart_user_sample_list()
        logging.debug(r)
        r = self.user.depart_user_sample_list(department_id=1)
        logging.debug(r)
        assert r["errcode"] == 0

    def test_detaillist_t009(self):
        r=self.user.depart_user_detail_list(deparment_id=2,fetch_child=1)
        logging.info(r)
        assert r["errcode"]==0

    def test_switch_userid_openid_t010(self):
        data={
            "userid": "RenShuaiJie"
            }
        r=self.user.switch_userid_openid(data)
        print(type(data))
        logging.info(r)
        assert r["errcode"]==0

    def test_second_verification_t011(self):
        data="ew_1213"
        r=self.user.second_verification(data)
        logging.info(r)
        assert r["errcode"]==0

    def test_invite_user_t012(self):
        user = ["UserID1","UserID2"]
        depart = ["1","26"]
        tag = ["1","2"]

        data={
        "user" : user,
        "party" : depart,
         "tag" : tag
            }
        print(type(data))
        print(data)
        r=self.user.invite_user(data)
        logging.info(r)
        assert r["errcode"]==0

    def test_join_qrcode(self):
        size="1"
        r=self.user.join_qrcode(size)
        logging.info(r)
        assert r["errcode"]==0


    def test_get_active_stat(self):
        data={
            "date": "2021-02-07"
            }
        r=self.user.get_active_stat(data)
        logging.info(r)
        assert r["errcode"]==0

