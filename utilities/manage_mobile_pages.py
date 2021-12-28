from pages.mobile_pages.menu_page import MenuPage
from pages.mobile_pages.calculator_page import CalculatorPage
from pages.mobile_pages.credit_card_minimum_page import CreditCardMinimumPage

import test.conftest as conf


class ManageMobilePages:
    def init_mobile_pages(self):
        conf.mobile_menu_page = MenuPage(conf.driver)
        conf.mobile_calc_page = CalculatorPage(conf.driver)
        conf.credit_card_min_page = CreditCardMinimumPage(conf.driver)

        globals()['mobile_menu_page'] = conf.mobile_menu_page
        globals()['mobile_calc_page'] = conf.mobile_calc_page
        globals()['credit_card_min_page'] = conf.credit_card_min_page
