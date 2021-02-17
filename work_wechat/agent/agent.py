import requests

from work_wechat.conf.weixin_token import Weixin_Token


class Agent(object):
    def get_agent(self, agentid, agent):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/agent/get",
                             params={"access_token":Weixin_Token.get_token(agent),
                                     "agentid":agentid}).json()

    def agent_list(self, agent):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/agent/list",
                            params={"access_token":Weixin_Token.get_token(agent)}).json()

    def agent_set(self,agent,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/agent/set",
                             params={"access_token":Weixin_Token.get_token(agent)},
                             json=dict,
                             data=data).json()

    def creat_menu(self,agentid,agent,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/menu/create",
                             params={"access_token":Weixin_Token.get_token(agent),
                                     "agentid":agentid},
                             json=dict,
                             data=data).json()
    def get_meun(self,agentid,agent):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/menu/get",
                            params={"access_token":Weixin_Token.get_token(agent),
                                    "agentid":agentid}).json()

    def delete_menu(self,agentid,agent):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/menu/delete",
                            params={"access_token": Weixin_Token.get_token(agent),
                                    "agentid": agentid}).json()

    def set_workbench_template(self,agent,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/agent/set_workbench_template",
                             params={"access_token": Weixin_Token.get_token(agent)},
                             json=dict,
                             data=data).json()

    def get_workbench_template(self,agent,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/agent/get_workbench_template",
                            params={
                                "access_token": Weixin_Token.get_token(agent)},
                             json=dict,
                             data=data
                            ).json()

    def set_workbench_data(self,agent,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/agent/set_workbench_data",
                             params={"access_token": Weixin_Token.get_token(agent)},
                             json=dict,
                             data=data
                             ).json()