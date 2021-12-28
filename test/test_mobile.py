import allure
import pytest

import workflows.mobile_flows as wf


@pytest.mark.usefixtures("init_mobile")
class Test_Mobile:
    def test_search(self):
        wf.search("roi")
        wf.wait_keyboard_and_click()
        list_len = wf.get_color_strip_length()
        wf.navigate_home()

        assert list_len == 2

    def test_credit_app(self):
        wf.navigate_to_credit()

        result = wf.calculate_loan()
        wf.navigate_home()

        assert result

    @allure.title("Test Calculator App")
    def test_calculator_app(self):
        wf.navigate_to_calculator()
        result = wf.multiply_action()
        wf.navigate_home()

        assert result == '81'
