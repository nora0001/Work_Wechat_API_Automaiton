import time

import pystache


class Utlis:
    @classmethod
    def parse(self, template_path, dict):
        template = "".join(open(template_path, encoding="utf-8").readlines())
        return pystache.render(template, dict)

    @classmethod
    def udid(self):
        return str(time.time()).replace(".","")[0:11]