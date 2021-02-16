import requests
import yaml
import logging


class Agent_token:
    logging.basicConfig(level=logging.DEBUG)
    _token = ""
    @classmethod
    def get_token(cls):
        if len(cls._token)== 0:
            cls._token = cls.get_token_new()
        return cls._token


    @classmethod
    def get_token_new(cls):
        filepath="../agent/agent.yaml"
        conf = yaml.safe_load(open(filepath))
        print(conf["env"])
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": conf["env"]["corpid"],
                                 "corpsecret": conf["env"]["secret"]}
                         ).json()
        return r["access_token"]


