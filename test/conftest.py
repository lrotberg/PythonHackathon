import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.desktop_pages.calculator_page import DesktopPage
from utilities.common_ops import get_data

driver = None
action = None
calc_page = None

@pytest.mark.fixture(scope='class')
def init_web(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    globals()['driver'] = driver
    request.cls.driver = driver
    driver.maximize_window()
    driver.get("http://facebook.com")

    yield
    driver.close()


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = get_data("calcApp")
    desired_caps["platformName"] = get_data("platformName_desktop")
    desired_caps["deviceName"] = get_data("deviceName")
    driver = webdriver.Remote(get_data("url_desktop"), desired_caps)
    globals()['driver'] = driver
    request.cls.driver = driver
    calc_page = DesktopPage(driver)
    globals()['calc_page']=calc_page

    yield
    driver.quit()


