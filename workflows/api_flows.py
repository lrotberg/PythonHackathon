from extentions.api_action import delete_posts_action, post_posts_action, get_posts_action


def get_posts():
    response_code = get_posts_action('/posts')
    return response_code

def post_posts():
    response_code = post_posts_action('/posts')
    return response_code

def delete_posts():
    response_code = delete_posts_action('/posts/100')
    return response_code

