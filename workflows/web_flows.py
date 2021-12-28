import allure
import re

from extentions.web_actions import click, clear_text, update_text, get_text
from utilities.common_ops import get_data

import test.conftest as conf


@allure.step("Login")
def login(username, password):
    conf.driver.get(get_data("url_web") + "/signin")
    update_text(conf.sign_in_page.username_input(), username)
    update_text(conf.sign_in_page.password_input(), password)
    click(conf.sign_in_page.sign_in_button())
    conf.driver.implicitly_wait(2)


@allure.step("Logout")
def logout():
    click(conf.menu_page.logout_button())


@allure.step("Navigate To Signup Page")
def navigate_to_signup():
    click(conf.sign_in_page.sign_up_link())


@allure.step("Navigate To Signin Page")
def navigate_to_signin():
    click(conf.sign_up_page.sign_in_link())


@allure.step("Register New User")
def register(first_name, last_name, username, password, confirm_password):
    update_text(conf.sign_up_page.first_name_input(), first_name)
    update_text(conf.sign_up_page.last_name_input(), last_name)
    update_text(conf.sign_up_page.username_input(), username)
    update_text(conf.sign_up_page.password_input(), password)
    update_text(conf.sign_up_page.confirm_password_input(), confirm_password)
    click(conf.sign_up_page.sign_up_button())


@allure.step("Get User String Balance")
def get_str_balance():
    return get_text(conf.menu_page.balance_heading())


@allure.step("Get User Number Balance")
def get_number_balance():
    balance = round(float(re.sub("[$,]", "", get_text(conf.menu_page.balance_heading()))), 2)
    return balance


@allure.step("Get Modal Text")
def get_modal_text():
    return get_text(conf.modal_page.get_started_heading())


@allure.step("Navigate to New Transaction")
def navigate_to_new_transaction():
    click(conf.header_page.new_transaction())


@allure.step("Navigate to Notifications")
def navigate_to_notifications():
    click(conf.menu_page.notifications_link())


@allure.step("Choose Contact")
def choose_contact(index):
    click(conf.transaction_select_page.contact_by_index(index))


@allure.step("Send Payment Request")
def send_payment_request(amount, note):
    update_text(conf.transaction_pay_page.amount_input(), amount)
    update_text(conf.transaction_pay_page.note_input(), note)
    click(conf.transaction_pay_page.request_button())


@allure.step("Send Payment")
def send_payment(amount, note):
    update_text(conf.transaction_pay_page.amount_input(), amount)
    update_text(conf.transaction_pay_page.note_input(), note)
    click(conf.transaction_pay_page.pay_button())

@allure.step("Get Notifications Number")
def get_notifications_number():
    return int(get_text(conf.header_page.notifications_bubble()))

@allure.step("Get Notifications List")
def get_notifications_list_length():
    return len(conf.notifications_page.notifications_list())
