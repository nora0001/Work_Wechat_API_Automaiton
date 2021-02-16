import logging

from work_wechat.agent.agent import Agent


class Test_agent(object):
    @classmethod
    def setup_class(cls):
        cls.agent = Agent()

    def test_get_agent(self):
        agentid = "3010084"
        r = self.agent.get_agent(agentid)
        logging.info(r)
        # assert r["errcode"]==0

    def test_agent_list(self):
        r = self.agent.agent_list()
        logging.info(r)

    def test_agent_set(self):
        data = {
            "agentid": 3010084,
            "report_location_flag": 0,
            "name": "财经助手",
            "description": "内部财经服务平台",
            "redirect_domain": "open.work.weixin.qq.com",
            "isreportenter": 0,
            "home_url": "https://open.work.weixin.qq.com"
        }
        r=self.agent.agent_set(data)
        logging.info(r)
        assert r["errcode"]==0

    def test_creat_menu(self):
        pass
