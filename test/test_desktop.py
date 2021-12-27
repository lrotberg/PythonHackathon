import pytest
from selenium.webdriver.common.by import By

import test.conftest as conf

@pytest.mark.usefixtures("init_desktop")
class Test_Desktop:
    def test_01(self):
        expected_result = "6"
        conf.driver.find_element(By.NAME,"One").click()
        conf.driver.find_element(By.NAME,"Plus").click()
        conf.driver.find_element(By.NAME,"Five").click()
        conf.driver.find_element(By.NAME,"Equals").click()
        assert self.get_result() == expected_result
