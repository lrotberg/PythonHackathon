import time
import pytest

import test.conftest as conf
from pages.web_pages.sign_in_page import SignInPage

@pytest.mark.usefixtures("init_web")
class Test_Testy:
    def test_01(self):
        expected_balance = 168137
        conf.driver.get("http://localhost:3000/signin")
        sign_in_page = SignInPage(conf.driver)
        sign_in_page.login("Katharina_Bernier", "s3cret")
