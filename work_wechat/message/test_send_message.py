import logging
import random
import string

from requests_toolbelt import MultipartEncoder
from work_wechat.conf.utlis import Utlis
from work_wechat.media.media import Media
from work_wechat.message.message import Message


class Test_Send_Message(object):
    agent_1="caijingzhushou"
    agentid_1="1000002"

    agent_2 = "HR"
    agentid_2 = "1000003"

    agent_3 = "IT Support"
    agentid_3 = "1000004"

    agent_4 = "Adr"
    agentid_4 = "1000005"

    user_one="RenShuaijie"
    user_two="lindon"

    @classmethod
    def setup_class(cls):
        cls.message = Message()
        cls.media = Media()

    def test_text(self):
        agent = self.agent_1
        user=self.user_one
        agentid=self.agentid_1

        data = str(Utlis.parse("test_messages/text.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_image(self):
        agent = self.agent_2
        user=self.user_one
        agentid=self.agentid_2

        type = "image"
        file = "../agent/agent_image.png"
        m = MultipartEncoder(
            fields={'file': ('agent_image.png', open(file, 'rb'), 'image/png')}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        media_id = r["media_id"]
        data = str(Utlis.parse("test_messages/image.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid,
                                   "mediaid": media_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_voice(self):
        agent = self.agent_3
        user=self.user_two
        agentid=self.agentid_3

        type = "voice"
        file = "test_messages/words.amr"
        m = MultipartEncoder(
            fields={'file': ('words.amr', open(file, 'rb'), 'voice')}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        media_id = r["media_id"]
        data = str(Utlis.parse("test_messages/voice.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid,
                                   "mediaid": media_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_video(self):
        agent = self.agent_4
        user="RenShuaiJie|lindon"
        agentid=self.agentid_4

        type = "video"
        file = "test_messages/EnglishLearning.mp4"
        m = MultipartEncoder(
            fields={'file': ('EnglishLearning.mp4', open(file, 'rb'), 'video')}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        media_id = r["media_id"]
        data = str(Utlis.parse("test_messages/video.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid,
                                   "mediaid": media_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_file(self):
        agent = self.agent_2
        user="RenShuaiJie|lindon"
        agentid=self.agentid_2

        type = "file"
        file = "test_messages/雅思听力-听力场景词汇汇总.pdf"
        m = MultipartEncoder(
            fields={'file': ('雅思听力-听力场景词汇汇总.pdf', open(file, 'rb'), 'file')}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        media_id = r["media_id"]
        data = str(Utlis.parse("test_messages/file.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid,
                                   "mediaid": media_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_textcard(self):
        agent = self.agent_1
        user="RenShuaiJie|lindon"
        agentid=self.agentid_1

        type = "file"
        data = str(Utlis.parse("test_messages/textcard.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid,
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_news(self):
        agent = self.agent_3
        user="lindon"
        agentid=self.agentid_3

        type = "file"
        data = str(Utlis.parse("test_messages/news.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid,
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_mpnews(self):
        agent = self.agent_2
        user="RenShuaiJie|lindon"
        agentid=self.agentid_2

        type = "image"
        file = "../agent/agent_image.png"
        m = MultipartEncoder(
            fields={'file': ('agent_image.png', open(file, 'rb'), 'image/png')}
        )
        r = self.media.media_temp_upload(agent, m, type, m.content_type)
        media_id = r["media_id"]
        data = str(Utlis.parse("test_messages/mpnews.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid,
                                   "media_id": media_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_markdown(self):
        agent = self.agent_1
        user="RenShuaiJie|lindon"
        agentid=self.agentid_1

        type = "markdown"
        data = str(Utlis.parse("test_messages/markdown.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_miniprogram_notice(self):
        agent = self.agent_4
        user="RenShuaiJie|lindon"

        app_id = "wxcbcd6c3340a4b95d"
        type = "file"
        data = str(Utlis.parse("test_messages/miniprogram_notice.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "app_id": app_id
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_taskcard(self):
        agent = self.agent_2
        user=self.user_one
        agentid=self.agentid_2

        type = "taskcard"
        taskid = "".join([random.choice(string.ascii_letters + "\"_-@\"")
                          if random.randint(0, 1)
                          else random.choice(string.digits)
                          for i in range(10)])
        print(taskid)
        data = str(Utlis.parse("test_messages/taskcard.json",
                               {
                                   "user": user,
                                   "party": "",
                                   "tag": "",
                                   "agent_id": agentid,
                                   "taskid": taskid
                               }))
        data = data.encode("UTF-8")
        r = self.message.send_message(agent, data=data)
        logging.info(r)
        assert r["errcode"] == 0
        return taskid

    def test_update_taskcard_yes(self):
        agent = self.agent_2
        agentid=self.agentid_2

        userid=self.user_one

        clicked_key="key111"
        taskid=self.test_taskcard()
        print(taskid)
        data = {
            "userids": userid,
            "agentid": agentid,
            "task_id": taskid,
            "clicked_key": clicked_key
        }
        r=self.message.update_taskcard(agent,data)

    def test_update_taskcard_no(self):
        agent = self.agent_2
        agentid = self.agentid_2

        userid = self.user_one


        clicked_key="key222"
        taskid=self.test_taskcard()
        print(taskid)
        data = {
            "userids": userid,
            "agentid": agentid,
            "task_id": taskid,
            "clicked_key": clicked_key
        }
        r=self.message.update_taskcard(agent,data)