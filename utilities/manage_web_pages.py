from pages.web_pages.menu_page import MenuPage
from pages.web_pages.notifications_page import NotificationsPage
from pages.web_pages.sign_in_page import SignInPage
from pages.web_pages.sign_up_page import SignUpPage
from pages.web_pages.modal_page import ModalPage
from pages.web_pages.header_page import HeaderPage
from pages.web_pages.transaction_select_page import TransactionSelectPage
from pages.web_pages.transaction_pay_page import TransactionPayPage

import test.conftest as conf


class ManageWebPages:
    def init_web_pages(self):
        conf.sign_in_page = SignInPage(conf.driver)
        conf.sign_up_page = SignUpPage(conf.driver)
        conf.menu_page = MenuPage(conf.driver)
        conf.modal_page = ModalPage(conf.driver)
        conf.header_page = HeaderPage(conf.driver)
        conf.transaction_select_page = TransactionSelectPage(conf.driver)
        conf.transaction_pay_page = TransactionPayPage(conf.driver)
        conf.notifications_page = NotificationsPage(conf.driver)

        globals()['sign_in_page'] = conf.sign_in_page
        globals()['sign_up_page'] = conf.sign_up_page
        globals()['menu_page'] = conf.menu_page
        globals()['modal_page'] = conf.modal_page
        globals()['header_page'] = conf.header_page
        globals()['transaction_select_page'] = conf.transaction_select_page
        globals()['transaction_pay_page'] = conf.transaction_pay_page
        globals()['notifications_page'] = conf.notifications_page
