import requests

from work_wechat.conf.weixin import Weixin


class Media(object):

    def media_img_upload(self,agent,data,content_type):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/media/uploadimg",
                             params={"access_token":Weixin.get_token(agent)},
                             data=data,
                             headers={'Content-Type': content_type}).json()

    def media_temp_get(self):
        pass

    def media_jssdk_get(self):
        pass

    def media_temp_upload(self,agent=None,data=None,type=None,content_type=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/media/upload",
                        params={"access_token": Weixin.get_token(agent),
                                "type":type},
                        data=data,
                        headers={'Content-Type': content_type}).json()