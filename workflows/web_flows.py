import allure

from extentions.web_actions import click, clear_text, update_text

import test.conftest as conf


@allure.step("Login")
def login(username, password):
    update_text(conf.sign_in_page.username_input(), username)
    update_text(conf.sign_in_page.password_input(), password)
    click(conf.sign_in_page.sign_in_button())


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


@allure.step("Get User Balance")
def get_balance():
    return conf.menu_page.balance_heading().text


@allure.step("Get Modal Text")
def get_modal_text():
    return conf.modal_page.get_started_heading().text
