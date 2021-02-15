import requests

from work_wechat.contact.token import Weixin


class Media(object):

    def media_img_upload(self):
        pass

    def media_temp_get(self):
        pass

    def media_jssdk_get(self):
        pass

    def media_temp_upload(self,data,type,content_type):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/media/upload",
                        params={"access_token": Weixin.get_token(),
                                "type":type},
                        data=data,
                        headers={'Content-Type': content_type}).json()