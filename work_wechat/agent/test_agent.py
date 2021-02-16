import logging

from work_wechat.agent.agent import Agent
from work_wechat.conf.utlis import Utlis


class Test_agent(object):
    agentid= "1000002"
    @classmethod
    def setup_class(cls):
        cls.agent = Agent()

    def test_get_agent(self):

        r = self.agent.get_agent(self.agentid)
        logging.info(r)
        # assert r["errcode"]==0

    def test_agent_list(self):
        r = self.agent.agent_list()
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
        r = self.agent.agent_set(data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_creat_menu(self):
        agentid = self.agentid
        data = str(Utlis.parse("create_menu.json",
                   {
                   }))
        data = data.encode("UTF-8")
        r=self.agent.creat_menu(agentid,data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_creat_menu_two(self):
        agentid = self.agentid
        data = str(Utlis.parse("create_menu_two.json",
                   {
                   }))
        data = data.encode("UTF-8")
        r=self.agent.creat_menu(agentid,data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_menu(self):
        r=self.agent.get_meun(self.agentid)
        logging.info(r)
        assert r["errcode"] == 0

    def test_delete_menu(self):
        r=self.agent.delete_menu(self.agentid)
        logging.info(r)
        assert r["errcode"] == 0