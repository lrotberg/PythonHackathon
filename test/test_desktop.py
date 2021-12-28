import allure
import pytest
import test.conftest as conf
from extentions.web_actions import get_result_calc
import workflows.desktop_flows as wf


@pytest.mark.usefixtures('init_desktop')
class Test_Desktop:

    @allure.title("Test Calculate Addition")
    @allure.description("This test should make an addition calculation and then verify the result")
    def test_01(self):
        wf.calculate_addition()
        assert get_result_calc(conf.calc_page.get_result()) == '6'
