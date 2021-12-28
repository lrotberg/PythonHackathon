import workflows.api_flows as wf


class Test_API_Requests:
    def test_01_get(self):
        assert wf.get_posts().status_code == 200

    def test_02_post(self):
        assert wf.post_posts().status_code == 201

    def test_03_delete(self):
        assert wf.delete_posts().status_code == 200

