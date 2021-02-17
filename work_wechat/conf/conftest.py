
import pytest

from work_wechat.conf.weixin_token import Weixin_Token


@pytest.fixture(scope="session")
def token():
    return Weixin_Token.get_token_new()