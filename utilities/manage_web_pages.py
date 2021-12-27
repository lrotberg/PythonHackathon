from pages.web_pages.sign_in_page import SignInPage
from pages.web_pages.sign_up_page import SignUpPage
from pages.web_pages.menu_page import MenuPage
from test.conftest import driver

class ManageWebPages:
    sign_in_page = SignInPage(driver)
    sign_up_page = SignUpPage(driver)
    menu_page = MenuPage(driver)
