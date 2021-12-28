import allure

import test.conftest as conf

from extentions.web_actions import click, get_text


@allure.step("Electron_test")
def click_menu():
    click(conf.demo_page.get_button_menus())


def click_open_links():
    click(conf.demo_page.get_open_external_links())

