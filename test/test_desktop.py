import allure
import pytest
import test.conftest as conf
from extentions.web_actions import get_result_calc
from workflows import desktop_flows


@pytest.mark.usefixtures('init_desktop')
class Test_Desktop:

    @allure.step("Test_calculate_addition")
    def test_01(self):
       desktop_wf.calculate_addition()
       assert get_result_calc(conf.calc_page.get_result()) == '6'
