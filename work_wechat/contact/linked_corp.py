import requests

from work_wechat.conf.token import Weixin


class Linked_corp(object):
    def get_perm_list(self):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/linkedcorp/agent/get_perm_list",
                             params={"access_token":Weixin.get_token()}).json()

    def get_corp_user_detail(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/linkedcorp/user/get",
                             params={"access_token":Weixin.get_token()},
                             json=dict,
                             data=data).json()

    def get_depart_user_simple(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/linkedcorp/user/simplelist",
                             params={"access_token":Weixin.get_token()},
                             json=dict,
                             data=data).json()


    def get_depart_user_detail(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/linkedcorp/user/list",
                             params={"access_token":Weixin.get_token()},
                             json=dict,
                             data=data).json()

    def get_depart_list(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/linkedcorp/department/list",
                             params={"access_token": Weixin.get_token()},
                             json=dict,
                             data=data).json()
