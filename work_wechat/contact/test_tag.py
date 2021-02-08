import logging

from work_wechat.contact.tag import Tag


class Test_tag:
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()

    def test_create_tag_t001(self):
        data = {
            "tagname": "UI",
            "tagid": 12
        }
        r = self.tag.creat(data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_update_tag_t002(self):
        data = {
            "tagid": 12,
            "tagname": "UI design"
        }
        r = self.tag.update(data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_tag_list(self):
        r = self.tag.get_tag_list()
        logging.info(r)
        assert r["errcode"] == 0

    def test_add_tag_user_t005(self):
        data = {
            "tagid": 12,
            "userlist": ["user1", "user2"],
            "partylist": [4]
        }
        r = self.tag.add_tag_user(data)
        logging.info(r)
        assert r["errcode"] == 0
    def test_get_tag_user_t004(self):
        tagid = 12
        r = self.tag.get_tag_user(tagid)
        logging.info(r)
        assert r["errcode"] == 0
    def test_delete_tag_user_t006(self):
        data = {
            "tagid": 12,
            "userlist": ["user1", "user2"],
            "partylist": [4]
        }
        r = self.tag.delete_tag_user(data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_delete_tag_t003(self):
        tagid = 12
        r = self.tag.delete(tagid)
        logging.info(r)
        assert r["errcode"] == 0




