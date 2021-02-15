import logging

import requests
from requests_toolbelt import MultipartEncoder

from work_wechat.contact.asynchronous_batch import Asynch
from work_wechat.media.media import Media


class Test_Asynch_batch:

    @classmethod
    def setup_class(cls):
        cls.asyn=Asynch()
        cls.media=Media()



    def test_batch_replace_depart(self):
        type = "file"
        file = "batch_party_sample.csv"
        m = MultipartEncoder(
            fields={file: ('file', open("../contact/batch_party_sample.csv", 'rb'))},
        )
        r = self.media.media_temp_upload(m, type, m.content_type)
        media_id = r["media_id"]
        data = {
            "media_id":media_id
        }
        r=self.asyn.batch_replace_depart(data)
        logging.info(r)
        assert r["errcode"]==0


    def test_batch_replace_user(self):
        type = "file"
        file = "batch_user_cover_sample.csv"
        m = MultipartEncoder(
            fields={file: ('file', open("../contact/batch_user_cover_sample.csv", 'rb'))},
        )
        r = self.media.media_temp_upload(m, type, m.content_type)
        media_id = r["media_id"]
        data = {
            "media_id" : media_id,
            "to_invite" : "true",
        }

        r = self.asyn.batch_replace_user(data)
        logging.info(r)
        assert r["errcode"] == 0


    def test_batch_update_user(self):
        type = "file"
        file = "batch_user_update_sample.csv"
        m = MultipartEncoder(
            fields={file: ('file', open("../contact/batch_user_update_sample.csv", 'rb'))},
        )
        r=self.media.media_temp_upload(m, type, m.content_type)
        media_id =r["media_id"]
        data = {
            "media_id": media_id,
            "to_invite": "true",
        }
        r=self.asyn.batch_update_user(data)
        logging.info(r)
        assert r["errcode"]==0





