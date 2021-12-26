import pytest

import test

@pytest.mark.usefixtures("init_web")
class Test_Testy:
    def test_01(self):
        print(test.coftest.driver)
