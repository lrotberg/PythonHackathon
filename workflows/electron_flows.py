import allure

import test.conftest as conf

from extentions.web_actions import click, get_text


@allure.step("Electron_test")
def electron_test():
    click(conf.demo_page.get_button_menus())
    assert get_text(conf.demo_page.get_verify_menus()) == 'Menu'
