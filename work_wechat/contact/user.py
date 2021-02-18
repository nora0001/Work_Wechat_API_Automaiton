import requests

from work_wechat.conf.weixin_token import Weixin_Token


class User:
    def create(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin_Token.get_token()},
                          json=dict,
                          data=data
                          ).json()


    def depart_user_sample_list(self, department_id=1, fetch_child=0, **kwargs):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                     params={"access_token": Weixin_Token.get_token(),
                             "department_id": department_id,
                             "fetch_child": fetch_child
                             }
                     ).json()

    def depart_user_detail_list(self,deparment_id=None,fetch_child=None,**kwargs):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/list",
                            params={
                                "access_token": Weixin_Token.get_token(),
                                "department_id":deparment_id,
                                "fetch_child":fetch_child

                            }).json()

    def get_all_users(self):
        pass

    def update(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/update",
                             params={"access_token": Weixin_Token.get_token()},
                             json=dict,
                             data=data
                             ).json()

    def delete(self,uid=None):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                            params={"access_token":Weixin_Token.get_token(),
                                    "userid":uid}
                            ).json()

    def bulk_delete(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete",
                             params={"access_token":Weixin_Token.get_token()},
                             json=dict,
                             data=data).json()

    def switch_userid_openid(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/convert_to_openid",
                             params={"access_token":Weixin_Token.get_token()},
                             json=dict,
                             data=data).json()



    def second_verification(self,data=None):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/authsucc",
                            params={"access_token":Weixin_Token.get_token(),
                                    "userid":data}).json()

    def invite_user(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/batch/invite",
                             params={"access_token":Weixin_Token.get_token()},
                             json=dict,
                             data=data).json()

    def join_qrcode(self,size):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/corp/get_join_qrcode",
                            params={"access_token":Weixin_Token.get_token(),
                                    "size_type":size},
                            ).json()

    def get_active_stat(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/get_active_stat",
                             params={"access_token":Weixin_Token.get_token()},
                             json=dict,
                             data=data).json()

