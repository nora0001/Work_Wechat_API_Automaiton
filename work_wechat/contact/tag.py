
import requests

from work_wechat.conf.weixin_token import Weixin_Token


class Tag():
    def creat(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/tag/create",
                              params={"access_token":Weixin_Token.get_token()},
                              json=dict,
                              data=data).json()

    def update(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/tag/update",
                             params={"access_token": Weixin_Token.get_token()},
                             json=dict,
                             data=data).json()

    def delete(self,tagid):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
                             params={"access_token":Weixin_Token.get_token(),
                                     "tagid": tagid}).json()
    def get_tag_user(self,tagid):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/get",
                            params={"access_token":Weixin_Token.get_token(),
                                    "tagid":tagid}
                            ).json()
    def add_tag_user(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
                             params={"access_token": Weixin_Token.get_token(),
                                     },
                             json=dict,
                             data=data).json()
    def delete_tag_user(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers",
                             params={"access_token":Weixin_Token.get_token()},
                             json=dict,
                             data=data)
    def get_tag_list(self):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/list",
                            params={"access_token":Weixin_Token.get_token()}
                            ).json()