import allure

import test.conftest as conf
from extentions.web_actions import click


@allure.step("calculate_addition")
def calculate_addition():
    click(conf.calc_page.get_one())
    click(conf.calc_page.get_plus())
    click(conf.calc_page.get_five())
    click(conf.calc_page.get_equals())
