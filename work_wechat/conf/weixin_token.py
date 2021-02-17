import requests
import yaml
import logging


class Weixin_Token:
    logging.basicConfig(level=logging.DEBUG)
    _token = ""
    @classmethod
    def get_token(cls,agent):
        if len(cls._token)== 0:
            cls._token = cls.get_token_new(agent)
        return cls._token


    @classmethod
    def get_token_new(cls,agent):

        conf = yaml.safe_load(open("../conf/corp_secret.yaml"))
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                             params={"corpid": conf["env"]["corpid"],
                                     "corpsecret": conf["env"]["agent"][agent]["secret"]}
                             ).json()
        corpid=conf["env"]["corpid"]
        secret=conf["env"]["agent"][agent]["secret"]
        m={"corpid":corpid,"agentsecret":secret}
        print(m)
        return r["access_token"]


