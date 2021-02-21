
import pytest

from work_wechat.conf.weixin import Weixin


@pytest.fixture(scope="session")
def token():
    return Weixin.get_token_new()