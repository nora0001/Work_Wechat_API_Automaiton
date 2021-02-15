import requests

from work_wechat.contact.token import Weixin


class Asynch(object):

    def batch_replace_depart(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/batch/replaceparty",
                             params={"access_token":Weixin.get_token()},
                             json=dict,
                             data=data).json()

    def batch_replace_user(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/batch/replaceuser",
                             params={"access_token": Weixin.get_token()},
                             json=dict,
                             data=data).json()

    def batch_update_user(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/batch/syncuser",
                             params={"access_token":Weixin.get_token()},
                             json=dict,
                             data=data).json()

    def get_batch_result(self,jobid):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/batch/getresult",
                            params={"access_token":Weixin.get_token(),
                                    "jobid":jobid}
                            ).json()








