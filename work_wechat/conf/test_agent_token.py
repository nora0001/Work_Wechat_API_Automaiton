from work_wechat.conf.weixin_token import Weixin_Token


def test_get_token():
    assert False


class TestAgentToken:
    def test_get_token(self):
        agent="Adr"
        print(Weixin_Token.get_token(agent))
