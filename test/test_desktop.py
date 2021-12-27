import pytest
import test.conftest as conf
from workflows.desktop_wf import Desktop_wf


@pytest.mark.usefixtures('init_desktop')
class Test_Desktop:

    def test_01(self):
        Desktop_wf.calculation(self)
        assert conf.calc_page.get_result() == '6'
