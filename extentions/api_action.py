import allure
import requests
from utilities.common_ops import get_data

@allure.step("GET")
def get_posts_action(url):
    return requests.get(get_data("url_api") + url)

@allure.step("POST")
def post_posts_action(url):
    payload = {'userId': '105', 'id': '', 'title': 'My Title', 'body': 'My Body'}
    return requests.post(get_data("url_api") + url, json=payload, headers={'Content-Type': 'application/json'})

@allure.step("DELETE")
def delete_posts_action(url):
    return requests.delete(get_data("url_api") + url)
