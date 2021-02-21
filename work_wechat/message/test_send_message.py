import logging
import random
import string

from requests_toolbelt import MultipartEncoder
from work_wechat.conf.utlis import Utlis
from work_wechat.media.media import Media
from work_wechat.message.message import Message


class Test_Send_Message(object):
    agent="caijingzhushou"
    agentid="1000002"

    agent_Adr="Adr"
    agentid_Adr="1000005"

    user_one="RenShuaijie"
    user_two="lindon"

    @classmethod
    def setup_class(cls):
        cls.message = Message()
        cls.media = Media()

    def test_text(self):
        agent = self.agent
        user=self.user_one
        agentid=self.agentid
        path="../message/test_messages/text.json"

        data = str(Utlis.parse(path,
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
        agent = self.agent
        user=self.user_one
        agentid=self.agentid
        path="../message/test_messages/image.json"

        type = "image"
        filepath = "../agent/agent_image.png"
        filename="agent_image.png"

        media_id = self.media.get_media_id(agent,filename,filepath,type)

        data = str(Utlis.parse(path,
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
        agent = self.agent
        user=self.user_two
        agentid=self.agentid
        path="../message/test_messages/voice.json"
        type = "voice"
        filepath = "test_messages/words.amr"
        filename="word.amr"

        media_id=self.media.get_media_id(agent,filename,filepath,type)
        data = str(Utlis.parse(path,
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
        agent = self.agent
        user="RenShuaiJie|lindon"
        agentid=self.agentid
        path="../message/test_messages/video.json"
        type = "video"
        filepath = "../message/test_messages/EnglishLearning.mp4"
        filename = "EnglisheLearning.mp4"
        media_id= self.media.get_media_id(agent,filename,filepath,type)
        data = str(Utlis.parse(path,
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
        agent = self.agent
        user="RenShuaiJie|lindon"
        agentid=self.agentid
        path="../message/test_messages/file.json"
        type = "file"
        filepath = "../message/test_messages/雅思听力-听力场景词汇汇总.pdf"
        filename="雅思听力-听力场景词汇汇总.pdf"
        media_id = self.media.get_media_id(agent,filename,filepath,type)

        data = str(Utlis.parse(path,
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
        agent = self.agent
        user="RenShuaiJie|lindon"
        agentid=self.agentid
        path="../message/test_messages/textcard.json"
        type = "file"
        data = str(Utlis.parse(path,
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
        agent = self.agent
        user="lindon"
        agentid=self.agentid
        path="../message/test_messages/news.json"
        type = "file"
        data = str(Utlis.parse(path,
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
        agent = self.agent
        user="RenShuaiJie|lindon"
        agentid=self.agentid
        path="../message/test_messages/mpnews.json"
        type = "image"
        filepath = "../agent/agent_image.png"
        filename="agent_image.png"
        media_id=self.media.get_media_id(agent,filename,filepath,type)
        data = str(Utlis.parse(path,
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
        agent = self.agent
        user="RenShuaiJie|lindon"
        agentid=self.agentid
        path="../message/test_messages/markdown.json"
        type = "markdown"
        data = str(Utlis.parse(path,
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
        agent = self.agent_Adr
        user="RenShuaiJie|lindon"
        path="../message/test_messages/miniprogram_notice.json"
        app_id = "wxcbcd6c3340a4b95d"
        type = "file"
        data = str(Utlis.parse(path,
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
        agent = self.agent_Adr
        user=self.user_one
        agentid=self.agentid_Adr
        path="../message/test_messages/taskcard.json"
        type = "taskcard"
        taskid = "".join([random.choice(string.ascii_letters + "\"_-@\"")
                          if random.randint(0, 1)
                          else random.choice(string.digits)
                          for i in range(10)])
        print(taskid)
        data = str(Utlis.parse(path,
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
        agent = self.agent_Adr
        agentid=self.agentid_Adr

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
        agent = self.agent_Adr
        agentid = self.agentid_Adr

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