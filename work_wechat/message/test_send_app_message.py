import logging

from requests_toolbelt import MultipartEncoder

from work_wechat.conf.utlis import Utlis
from work_wechat.media.media import Media
from work_wechat.message.message import Message


class Test_send_app_message(object):
    agent = "HR"
    name = "特价机票抢购群"
    name_new="淘宝特价抢购1群"
    userid_1 = "RenShuaijie"
    userid_2 = "lindon"
    userid_3 = "ew_1213"
    userid_4 = "lisi"
    userid_5 = "1612592950024059000"
    userid_6 = "zhaoer"
    chatid = "wralYAEQAAqzVWasUXPXrLSTm2gvtmLA"

    @classmethod
    def setup_class(cls):
        cls.message = Message()
        cls.media = Media()

    def test_creat_appchat(self):
        data = {
            "name": self.name,
            "userlist": [self.userid_1, self.userid_2, self.userid_3, self.userid_4],
        }

        r = self.message.creat_app_chat(self.agent, data)
        logging.info(r)
        assert r["errcode"] == 0
        return r["chatid"]

    def test_update_appchat(self):
        # chatid=self.test_creat_appchat()

        data = {
            "chatid": self.chatid,
            "name": self.name_new,
            "owner": self.userid_2,
            "add_user_list": [self.userid_5, self.userid_6],
            "del_user_list": [self.userid_4]
        }
        r = self.message.update_app_chat(self.agent, data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_appchat(self):
        # chatid=self.test_creat_appchat()
        r = self.message.get_app_chat(self.agent, self.chatid)
        logging.info(r)
        assert r["errcode"] == 0

    def test_send_text_appchat(self):
        # chatid=self.test_creat_appchat()
        path = "../message/test_app_messages/text.json"
        data = str(Utlis.parse(path,
                               {
                                   "chat_id": self.chatid
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_app_chat(self.agent, data=data)
        print(data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_send_image_appchat(self):
        # chatid = self.test_creat_appchat()
        path = "../message/test_app_messages/image.json"
        type = "image"
        filepath = "../agent/agent_image.png"
        filename = "agent_image.png"
        media_id = self.media.get_media_id(self.agent, filename, filepath, type)
        data = str(Utlis.parse(path,
                               {
                                   "chat_id": self.chatid,
                                   "media_id": media_id
                               }))

        data = data.encode("UTF-8")
        r = self.message.send_app_chat(self.agent, data=data)
        print(data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_send_voice_appchat(self):
        path = "../message/test_app_messages/voice.json"
        type = "voice"
        filepath = "../message/test_app_messages/words.amr"
        filename = "word.amr"
        media_id = self.media.get_media_id(self.agent, filename, filepath, type)

        data = str(Utlis.parse(path,
                               {
                                   "chat_id": self.chatid,
                                   "media_id": media_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_app_chat(self.agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_send_video_appchat(self):
        path = "../message/test_app_messages/video.json"
        type = "video"
        filepath = "../message/test_app_messages/EnglishLearning.mp4"
        filename = "EnglishLearning.mp4"
        media_id = self.media.get_media_id(self.agent, filename, filepath, type)

        data = str(Utlis.parse(path,
                               {
                                   "chat_id": self.chatid,
                                   "media_id": media_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_app_chat(self.agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_send_file_appchat(self):
        path = "../message/test_app_messages/file.json"
        type = "file"
        filepath = "../message/test_app_messages/雅思听力-听力场景词汇汇总.pdf"
        filename = "雅思听力-听力场景词汇汇总.pdf"
        media_id = self.media.get_media_id(self.agent, filename, filepath, type)

        data = str(Utlis.parse(path,
                               {
                                   "chat_id": self.chatid,
                                   "media_id": media_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_app_chat(self.agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_send_textcard_appchat(self):
        path = "../message/test_app_messages/textcard.json"

        data = str(Utlis.parse(path,
                               {
                                   "chat_id": self.chatid,
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_app_chat(self.agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_send_news_appchat(self):
        path = "../message/test_app_messages/news.json"

        data = str(Utlis.parse(path,
                               {
                                   "chat_id": self.chatid,
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_app_chat(self.agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_send_mpnews_appchat(self):
        path = "../message/test_app_messages/mpnews.json"
        type = "image"
        filepath = "../agent/one hour on the earth.png"
        filename = "one hour on the earth.png"
        media_id = self.media.get_media_id(self.agent, filename, filepath, type)
        data = str(Utlis.parse(path,
                               {
                                   "chat_id": self.chatid,
                                   "media_id": media_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_app_chat(self.agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_send_markdown_appchat(self):
        path = "../message/test_app_messages/markdown.json"

        data = str(Utlis.parse(path,
                               {
                                   "chat_id": self.chatid,
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_app_chat(self.agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_messsage_statistics(self):
        data = {
            "time_type": 0
        }
        r=self.message.get_message_statistics(self.agent,data)
        logging.info(r)
        assert r["errcode"]==0
