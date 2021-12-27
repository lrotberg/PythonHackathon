from workflows.api_wf import API_wf


class Test_API_Requests:
    def test_01_get(self):
        assert API_wf.get_posts().status_code == 200

    def test_02_post(self):
        assert API_wf.post_posts().status_code == 201

    def test_03_delete(self):
        assert API_wf.delete_posts().status_code == 200

