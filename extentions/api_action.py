import requests
from utilities.common_ops import get_data

class API_action:
    @staticmethod
    def get_posts(url):
        response=requests.get(get_data("url_api") + url)
        return response

    @staticmethod
    def post_posts(url):
        payload = {'userId': '105', 'id': '', 'title': 'My Title', 'body': 'My Body'}
        response = requests.post(get_data("url_api") + url, json=payload, headers={'Content-Type': 'application/json'})
        return response

    @staticmethod
    def delete_posts(url):
        response = requests.delete(get_data("url_api") +url)
        return response

