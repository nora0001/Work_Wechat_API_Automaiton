import requests

from work_wechat.contact.token import Weixin


class User:
    def create(self,json=dict,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          json=dict,
                            data=data

                          ).json()


    def list(self, department_id=1, fetch_child=0, **kwargs):
        requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                     params={"access_token": Weixin.get_token(),
                             "department_id": department_id,
                             "fetch_child": fetch_child
                             }
                     ).json()