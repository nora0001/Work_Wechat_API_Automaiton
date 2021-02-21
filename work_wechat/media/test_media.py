import logging

from requests_toolbelt import MultipartEncoder

from work_wechat.media.media import Media


class Test_Media:

    @classmethod
    def setup_class(cls):
        cls.media=Media()


    def test_get_media_id(self):
        type = "file"
        file = "batch_user_update_sample.csv"
        m = MultipartEncoder(
            fields={file: ('file', open("../contact/batch_user_update_sample.csv", 'rb'))},
        )
        r =self.media.media_temp_upload(m, type, m.content_type)
        media_id=r["media_id"]
        print(media_id)
        return r["media_id"]

    def test_image_upload_temp(self):
        agent = "Adr"
        type = "image"
        file = "../agent/agent_image.png"
        m = MultipartEncoder(
            fields={'file': ('agent_image.png', open(file, 'rb'), 'image/png')}
        )
        r = self.media.media_temp_upload(agent, m,type, m.content_type)
        logging.info(r)
        return r["media_id"]

    def test_voice_upload_temp(self):
        agent = "Adr"
        type = "voice"
        file = "../message/test_messages/words.amr"
        m = MultipartEncoder(
            fields={'file': ('words.amr', open(file, 'rb'), 'voice')}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        logging.info(r)
        return r["media_id"]
    def test_video_upload_temp(self):
        agent = "Adr"
        type = "video"
        file = "../message/test_messages/EnglishLearning.mp4"
        m = MultipartEncoder(
            fields={'file': ('EnglishLearning.mp4', open(file, 'rb'), 'video')}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        logging.info(r)
        return r["media_id"]

    def test_file_upload_temp(self):
        agent = "Adr"
        type = "file"
        file = "../message/test_messages/雅思听力-听力场景词汇汇总.pdf"
        m = MultipartEncoder(
            fields={'file': ('雅思听力-听力场景词汇汇总.pdf', open(file, 'rb'), 'file')}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        logging.info(r)
        return r["media_id"]

    def test_image_upload(self):
        agent="HR"
        type="image/png"
        file="../agent/agent_image.png"
        m= MultipartEncoder(
            fields={'file':('agent_image.png',open(file,'rb'),'image/png')}
        )
        r = self.media.media_img_upload(agent,m, m.content_type)
        logging.info(r)
        # return r["media_id"]
