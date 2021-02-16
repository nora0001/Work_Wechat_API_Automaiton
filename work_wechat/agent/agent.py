import requests

from work_wechat.conf.token import Weixin


class Agent(object):
    def get_agent(self,agentid):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/agent/get",
                             params={"access_token":Weixin.get_token(),
                                     "agentid":agentid}).json()

    def agent_list(self):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/agent/list",
                             params={"access_token":Weixin.get_token()}).json()

    def agent_set(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/agent/set",
                             params={"access_token":Weixin.get_token()},
                             json=dict,
                             data=data).json()

    def creat_menu(self,agentid,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/menu/create",
                             params={"access_token":Weixin.get_token(),
                                     "agentid":agentid},
                             json=dict,
                             data=data).json()
