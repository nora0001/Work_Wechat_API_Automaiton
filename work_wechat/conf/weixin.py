import requests
import yaml
import logging


class Weixin:
    logging.basicConfig(level=logging.DEBUG)
    _token = ""
    @classmethod
    def get_token(cls,agent=None,**kwargs):
        # if len(cls._token)== 0:
        cls._token = cls.get_token_new(agent)
        return cls._token


    @classmethod
    def get_token_new(cls,agent=None,**kwargs):

        conf = yaml.safe_load(open("../conf/corp_secret.yaml"))
        if agent:
            r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                                 params={"corpid": conf["env"]["corpid"],
                                         "corpsecret": conf["env"]["agent"][agent]["secret"]}
                                 ).json()

            m = {"corpid": conf["env"]["corpid"], "corpsecret":conf["env"]["agent"][agent]["secret"], "access_token": r["access_token"]}
        else:
            r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                             params={"corpid": conf["env"]["corpid"],
                                     "corpsecret": conf["env"]["secret"]}
                             ).json()

            m = {"corpid": conf["env"]["corpid"], "corpsecret": conf["env"]["secret"], "access_token": r["access_token"]}


        print(m)
        return r["access_token"]


