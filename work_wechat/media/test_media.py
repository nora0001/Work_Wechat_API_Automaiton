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
        return r["media_id"]
