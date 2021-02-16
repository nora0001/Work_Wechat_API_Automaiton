import logging

from work_wechat.contact.linked_corp import Linked_corp


class Test_linked_corp:

    @classmethod
    def setup_class(cls):
        cls.linked_corp = Linked_corp()

    def test_get_perm_list(self):
        r = self.linked_corp.get_perm_list()
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_corp_user_detail(self):
        data = {
            "userid": "wwe5b7d33175284f5f/zhangsan"
        }
        r = self.linked_corp.get_corp_user_detail(data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_depart_user_simple(self):
        data = {
            "department_id": "LINKEDID/3",
            "fetch_child": "true"
        }
        r = self.linked_corp.get_depart_user_simple(data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_depart_user_detail(self):
        data = {
            "department_id": "LINKEDID/3",
            "fetch_child": "true"
        }
        r = self.linked_corp.get_depart_user_detail(data)
        logging.info(r)
        assert r["errcode"] == 0

    def test_get_depart_list(self):
        data = {
            "department_id": "LINKEDID/3"
        }

        r = self.linked_corp.get_depart_list(data)
        logging.info(r)
        assert r["errcode"] == 0