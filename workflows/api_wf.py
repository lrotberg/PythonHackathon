from extentions.api_action import API_action


class API_wf:
    @staticmethod
    def get_posts():
        response_code = API_action.get_posts('/posts')
        return response_code

    @staticmethod
    def post_posts():
        response_code = API_action.post_posts('/posts')
        return response_code

    @staticmethod
    def delete_posts():
        response_code = API_action.delete_posts('/posts/100')
        return response_code

