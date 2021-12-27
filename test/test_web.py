import pytest

import test.conftest as conf
import workflows.web_flows as wf
import test.users_ddt as ddt

from utilities.common_ops import get_data


@pytest.mark.usefixtures("init_web")
class Test_Web:
    def teardown_method(self):
        wf.logout()

    @pytest.mark.parametrize(ddt.users_headers, ddt.users)
    def test_check_balance(self, username, password, expected_balance):
        conf.driver.get(get_data("url_web") + "/signin")
        wf.login(username, password)
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
