from work_wechat.conf.weixin_token import Weixin_Token


def test_get_token():
    assert False


class TestWeixin:
    def test_get_token(self):
        print(Weixin_Token.get_token("contact"))
        assert Weixin_Token.get_token("contact") !=""
