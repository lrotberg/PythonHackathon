import allure

import test.conftest as conf

from extentions.web_actions import click, get_text


@allure.step("Click manu")
def click_menu():
    click(conf.demo_page.get_button_menus())


@allure.step("Check screen info")
def screen_info():
    click(conf.demo_page.get_sys_information())
    click(conf.demo_page.get_view_demo())
