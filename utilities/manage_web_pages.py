from pages.web_pages.menu_page import MenuPage
from pages.web_pages.sign_in_page import SignInPage
from pages.web_pages.sign_up_page import SignUpPage
from pages.web_pages.modal_page import ModalPage

import test.conftest as conf


class ManageWebPages:
    def init_web_pages(self):
        conf.sign_in_page = SignInPage(conf.driver)
        globals()['sign_in_page'] = conf.sign_in_page
        conf.sign_up_page = SignUpPage(conf.driver)
        globals()['sign_up_page'] = conf.sign_up_page
        conf.menu_page = MenuPage(conf.driver)
        globals()['menu_page'] = conf.menu_page
        conf.modal_page = ModalPage(conf.driver)
        globals()['modal_page'] = conf.modal_page
