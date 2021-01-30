import json

import requests
import pytest
import logging

class TestRequests(object):

    logging.basicConfig(level=logging.INFO)

    def test_get(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))