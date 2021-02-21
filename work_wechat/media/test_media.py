import logging

from requests_toolbelt import MultipartEncoder

from work_wechat.media.media import Media


class Test_Media:

    @classmethod
    def setup_class(cls):
        cls.media = Media()

    def test_get_media_id(self):
        agent = "IT Support"
        type = "file"
        filename = "batch_user_update_sample.csv"
        filepath = "../contact/batch_user_update_sample.csv"
        r = self.media.get_media_id(agent, filename, filepath, type)
        print(r["media_id"])
        assert r["errcode"] == 0

    def test_image_upload_temp(self):
        agent = "Adr"
        type = "image"
        filepath = "../agent/agent_image.png"
        filename = "agent_image.png"
        m = MultipartEncoder(
            fields={'file': (filename, open(filepath, 'rb'), type)}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        logging.info(r)
        assert r["errcode"] == 0
        return r["media_id"]

    def test_voice_upload_temp(self):
        agent = "Adr"
        type = "voice"
        filepath = "../message/test_messages/words.amr"
        filename = "word.amr"
        m = MultipartEncoder(
            fields={'file': (filename, open(filepath, 'rb'), type)}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        logging.info(r)
        assert r["errcode"] == 0
        return r["media_id"]

    def test_video_upload_temp(self):
        agent = "Adr"
        type = "video"
        filepath = "../message/test_messages/EnglishLearning.mp4"
        filename = "EnglishLearning.mp4"
        m = MultipartEncoder(
            fields={'file': (filename, open(filepath, 'rb'), type)}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        logging.info(r)
        assert r["errcode"] == 0
        return r["media_id"]

    def test_file_upload_temp(self):
        agent = "Adr"
        type = "file"
        filepath = "../message/test_messages/雅思听力-听力场景词汇汇总.pdf"
        filename = "雅思听力-听力场景词汇汇总.pdf"
        m = MultipartEncoder(
            fields={'file': (filename, open(filepath, 'rb'), type)}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        logging.info(r)
        assert r["errcode"] == 0
        return r["media_id"]

    def test_image_upload(self):
        agent = "HR"
        type = "image/png"
        filepath = "../agent/agent_image.png"
        filename = "agent_image.png"
        m = MultipartEncoder(
            fields={'file': (filename, open(filepath, 'rb'), type)}
        )
        r = self.media.media_img_upload(agent, m, m.content_type)
        logging.info(r)
        assert r["errcode"] == 0

    def test_media_temp_get(self):
        agent = "HR"
        media_id_1 = self.test_image_upload_temp()
        media_id_2 = self.test_file_upload_temp()
        # media_id_3 = self.test_video_upload_temp()
        # media_id_4 = self.test_voice_upload_temp()
        # media_id = [media_id_1, media_id_2, media_id_3, media_id_4]
        media_id = [media_id_1, media_id_2]
        # for i in media_id:
        #     print(i)
        print(media_id_1)
        print(type(media_id_1))

        r = self.media.media_temp_get(agent, media_id_1)
        logging.info(r)


    def test_media_jssdk_get(self):
        agent = "HR"
        media_id=self.test_voice_upload_temp()
        print(media_id)
        r=self.media.media_jssdk_get(agent,media_id)
        logging.info(r)
        assert r["errcode"]==0

