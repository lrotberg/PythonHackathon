import pytest

import test.conftest as conf
import workflows.web_flows as wf

from utilities.common_ops import get_data

@pytest.mark.usefixtures("init_web")
class Test_Web:
    def test_check_balance(self):
        expected_balance = "$1,681.37"
        conf.driver.get("http://localhost:9090/signin")
        wf.login("Katharina_Bernier", "s3cret")
        conf.driver.implicitly_wait(2)

        assert wf.get_balance() == expected_balance

    def test_register_user(self):
        expected_text = "Get Started with Real World App"
        conf.driver.get(get_data("url_web") + "/signup")
        wf.register("Lior", "Rotberg", "Lrotberg", "s3cret", "s3cret")
        conf.driver.implicitly_wait(2)
        wf.login("Lrotberg", "s3cret")
        conf.driver.implicitly_wait(2)

        assert wf.get_modal_text() == expected_text

