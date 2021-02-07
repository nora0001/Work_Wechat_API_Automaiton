import requests

from work_wechat.contact.token import Weixin



class Department(object):

    def create(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": Weixin.get_token()},
                          json=dict,
                          data=data
                          ).json()

    def update(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/update",
                             params={"access_token": Weixin.get_token()},
                             json=dict,
                             data=data).json()

    def get_list(self):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                     params={"access_token": Weixin.get_token()}
                     ).json()

    def delete(self,id):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                            params={"access_token":Weixin.get_token(),
                                    "id":id}
                            ).json()