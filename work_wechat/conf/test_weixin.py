from work_wechat.contact.token import Weixin


def test_get_token():
    assert False


class TestWeixin:
    def test_get_token(self):
        print(Weixin.get_token())
        assert Weixin.get_token() !=""
