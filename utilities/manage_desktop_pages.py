from pages.desktop_pages.calculator_page import CalculatorPage

import test.conftest as conf

class ManageDesktopPages:
    def init_desktop_pages(self):
        conf.calc_page = CalculatorPage(conf.driver)
        globals()['calc_page'] = conf.calc_page
