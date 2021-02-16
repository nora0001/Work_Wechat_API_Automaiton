import requests

from work_wechat.agent.agent_token import Agent_token


class Agent(object):
    def get_agent(self,agentid):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/agent/get",
                             params={"access_token":Agent_token.get_token(),
                                     "agentid":agentid}).json()

    def agent_list(self):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/agent/list",
                             params={"access_token":Agent_token.get_token()}).json()

    def agent_set(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/agent/set",
                             params={"access_token":Agent_token.get_token()},
                             json=dict,
                             data=data).json()

    def creat_menu(self,agentid,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/menu/create",
                             params={"access_token":Agent_token.get_token(),
                                     "agentid":agentid},
                             json=dict,
                             data=data).json()
    def get_meun(self,agentid):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/menu/get",
                            params={"access_token":Agent_token.get_token(),
                                    "agentid":agentid}).json()

    def delete_menu(self,agentid):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/menu/delete",
                            params={"access_token": Agent_token.get_token(),
                                    "agentid": agentid}).json()