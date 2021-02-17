import logging

from work_wechat.agent.agent import Agent
from work_wechat.conf.utlis import Utlis

class Test_agent(object):
    agentid = "1000002"
    agent_name = "caijingzhushou"
    @classmethod
    def setup_class(cls):
        cls.agent = Agent()

    def test_get_agent(self):

        r = self.agent.get_agent(self.agentid,self.agent_name)
        logging.info(r)
        # assert r["errcode"]==0

    def test_agent_list(self):
        r = self.agent.agent_list(self.agent_name)
        logging.info(r)

    def test_agent_set(self):
        data = {
            "agentid": self.agentid,
            "report_location_flag": 0,
            "name": "财经助手",
            "description": "内部财经服务平台",
            "redirect_domain": "open.work.weixin.qq.com",
            "isreportenter": 0,
            "home_url": "https://open.work.weixin.qq.com"
        }
        r = self.agent.agent_set(self.agent_name,data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_creat_menu(self):
        agentname=self.agent_name
        agentid=self.agentid
        print(agentid)
        print(agentname)
        data = str(Utlis.parse("create_menu.json",
                               {
                               }))
        data = data.encode("UTF-8")
        r = self.agent.creat_menu(agentid,agentname, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_creat_menu_two(self):
        agentid = self.agentid
        data = str(Utlis.parse("create_menu_two.json",
                               {
                               }))
        data = data.encode("UTF-8")
        r = self.agent.creat_menu(self.agentid,self.agent_name,agentid, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_menu(self):
        r = self.agent.get_meun(self.agentid,self.agent_name)
        logging.info(r)
        assert r["errcode"] == 0

    def test_delete_menu(self):
        r = self.agent.delete_menu(self.agentid,self.agent_name)
        logging.info(r)
        assert r["errcode"] == 0

    def test_set_workbench_keydata_template(self):
        agentid=self.agentid
        agentname=self.agent_name
        print(agentname)
        print(agentid)
        data = str(Utlis.parse("keydata_workbench.json", {
            "agent_id": agentid}))
        data = data.encode("UTF-8")
        r = self.agent.set_workbench_template(agentname,data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_set_workbench_image_template(self):
        agentid="1000003"
        agentname="HR"
        data = {
            "agentid": agentid,
            "type": "image",
            "image": {
                "url": "https://i.loli.net/2021/02/17/AkCJzi5xW8y9IRD.png",
                "jump_url": "http://www.qq.com",
                "pagepath": "pages/index"
            },
            "replace_user_data": "true"
        }
        r = self.agent.set_workbench_template(agentname,data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_set_workbench_list_template(self):
        agentid="1000004"
        agentname="IT_support"
        data = str(Utlis.parse("list_workbench.json", {
            "agent_id": agentid}))
        data = data.encode("UTF-8")
        print(agentname)
        print(agentid)
        r = self.agent.set_workbench_template(agentname,data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_set_workbench_webview_template(self):
        agentid = "1000005"
        agentname = "Adr"
        data = {
            "agentid": agentid,
            "type": "webview",
            "webview": {
                "url": "http://www.qq.com",
                "jump_url": "http://www.qq.com",
                "pagepath": "pages/index"
            }
            ,
            "replace_user_data": "true"
        }
        print(agentname)
        print(agentid)
        r = self.agent.set_workbench_template(agentname,data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_workbench_template(self):
        agentid = "1000005"
        agentname = "Adr"
        data = {
            "agentid": agentid
        }
        r=self.agent.get_workbench_template(agentname,data)
        print(agentname)
        print(agentid)
        logging.info(r)
        assert r["errcode"]==0

    def test_set_workbench_data(self):
        agentid = "1000004"
        agentname = "IT_support"
        data = str(Utlis.parse("set_workbench_data.json", {
            "agent_id": agentid}))
        data = data.encode("UTF-8")
        print(agentname)
        print(agentid)
        r=self.agent.set_workbench_template(agentname,data=data)
        logging.info(r)
        assert r["errcode"]==0
