from work_wechat.conf.weixin import Weixin


def test_get_token():
    assert False


class TestAgentToken:
    def test_get_token(self):
        agent="Adr"
        print(Weixin.get_token(agent))
