import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None
action = None

@pytest.mark.fixture(scope='class')
def init_web(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    globals()['driver'] = driver
    request.cls.driver = driver
    driver.maximize_window()
    driver.get("http://facebook.com")

    yield
    driver.close()
