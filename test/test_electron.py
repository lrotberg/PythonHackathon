import pytest
import workflows.electron_flows as wf
import test.conftest as conf

from extentions.web_actions import get_text


@pytest.mark.usefixtures("init_electron")
class Test_Electron:
    def test_01(self):
        wf.click_menu()
        assert get_text(conf.demo_page.get_verify_menus()) == 'Menu'


    def test_02(self):
        wf.screen_info()
        assert get_text(conf.demo_page.get_result()) == 'Your screen is: 1366px x 768px'



