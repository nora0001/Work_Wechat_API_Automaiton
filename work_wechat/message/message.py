import requests

from work_wechat.conf.weixin import Weixin


class Message(object):

    def send_message(self,agent=None,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send",
                             params={"access_token":Weixin.get_token(agent)},
                             json=dict,
                             data=data).json()

    def update_taskcard(self,agent=None,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/update_taskcard",
                             params={"access_token":Weixin.get_token(agent)},
                             json=dict,
                             data=data).json()

    def creat_app_chat(self,agent=None,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/appchat/create",
                             params={"access_token":Weixin.get_token(agent)},
                             json=dict,
                             data=data).json()

    def update_app_chat(self,agent=None,dict=None,data=None):
        return requests.post(" https://qyapi.weixin.qq.com/cgi-bin/appchat/update",
                             params={"access_token": Weixin.get_token(agent)},
                             json=dict,
                             data=data).json()

    def get_app_chat(self,agent=None,chatid=None,dict=None,data=None):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/appchat/get",
                            params={"access_token":Weixin.get_token(agent),
                                    "chatid":chatid}
                            ).json()

    def send_app_chat(self,agent=None,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/appchat/send",
                             params={"access_token":Weixin.get_token(agent)},
                             json=dict,
                             data=data
                             ).json()

    def get_message_statistics(self,agent=None,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/get_statistics",
                             params={"access_token": Weixin.get_token(agent)},
                             json=dict,
                             data=data).json()
