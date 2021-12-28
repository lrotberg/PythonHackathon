import time

import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from extentions.web_actions import click, clear_text, update_text, get_text
from utilities.common_ops import get_data

import test.conftest as conf


@allure.step("Search")
def search(value):
    click(conf.mobile_menu_page.search_button())
    conf.driver.implicitly_wait(3)
    update_text(conf.mobile_menu_page.search_input(), value)


@allure.step("Search click")
def search_click():
    click(conf.mobile_menu_page.search_it())
    conf.driver.implicitly_wait(10)



@allure.step("Get Color Strip List Length")
def get_listview_length():
    lengthis=len(conf.menu_page.listview())
    time.sleep(2)
    return lengthis


@allure.step("Navigate Home")
def navigate_home():
    click(conf.mobile_menu_page.navigate_back())


@allure.step("Navigate to Calculator App")
def navigate_to_calculator():
    click(conf.mobile_menu_page.calculator_app())


@allure.step("Navigate to Credit App")
def navigate_to_credit():
    click(conf.mobile_menu_page.credit_card_app())


@allure.step("Make Multiply action")
def multiply_action():
    click(conf.mobile_calc_page.number_9_button())
    click(conf.mobile_calc_page.multiply_button())
    click(conf.mobile_calc_page.number_9_button())
    click(conf.mobile_calc_page.equals_button())
    return get_text(conf.mobile_calc_page.result_field())

@allure.step("Calculate Loan")
def calculate_loan():
    update_text(conf.credit_card_min_page.balance(), "10")
    update_text(conf.credit_card_min_page.rate(), "10")
    click(conf.credit_card_min_page.min_percentage())
    click(conf.credit_card_min_page.min_percentage_choose())
    click(conf.credit_card_min_page.calculate_button())
    expected_months = get_text(conf.credit_card_min_page.pay_off_months())
    ex_total_insert = get_text(conf.credit_card_min_page.interest_payment())
    ex_total_payment = get_text(conf.credit_card_min_page.total())

    return expected_months and ex_total_insert and ex_total_payment
