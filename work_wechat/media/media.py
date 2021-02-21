import requests
from requests_toolbelt import MultipartEncoder

from work_wechat.conf.weixin import Weixin


class Media(object):

    def media_temp_upload(self,agent=None,data=None,type=None,content_type=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/media/upload",
                        params={"access_token": Weixin.get_token(agent),
                                "type":type},
                        data=data,
                        headers={'Content-Type': content_type}
                             ).json()

    def get_media_id(self,agent,filename,filepath,type):

        m = MultipartEncoder(
            fields={'file': (filename, open(filepath, 'rb'), type)}
        )
        r = self.media_temp_upload(agent, m, type, m.content_type)
        return r["media_id"]

    def media_img_upload(self,agent,data,content_type):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/media/uploadimg",
                             params={"access_token":Weixin.get_token(agent)},
                             data=data,
                             headers={'Content-Type': content_type}
                             ).json()

    def media_temp_get(self,agent,media_id):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/media/get",
                            params={"access_token": Weixin.get_token(agent),
                                    "media_id": media_id}
                            ).json()

    def media_jssdk_get(self,agent,media_id):
        return  requests.get("https://qyapi.weixin.qq.com/cgi-bin/media/get/jssdk",
                             params={"access_token":Weixin.get_token(agent),
                                     "media_id":media_id
                                     }).json()

