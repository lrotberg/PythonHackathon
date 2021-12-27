import time

import pytest

import test.conftest as conf
import workflows.web_flows as wf

@pytest.mark.usefixtures("init_web")
class Test_Testy:
    def test_check_balance(self):
        expected_balance = "$1,681.37"
        conf.driver.get("http://localhost:9090/signin")
        wf.login("Katharina_Bernier", "s3cret")
        conf.driver.implicitly_wait(2)

        assert wf.get_balance() == expected_balance

    def test_register_user(self):
        conf.driver.get("http://localhost:9090/signup")
        wf.register("Lior", "Rotberg", "Lrotberg", "s3cret", "s3cret")
        conf.driver.implicitly_wait(2)
        wf.login("Lrotberg", "s3cret")
        conf.driver.implicitly_wait(2)

        assert wf.get_modal_text() == "Get Started with Real World App"

