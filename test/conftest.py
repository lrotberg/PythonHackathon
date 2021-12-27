import pytest

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utilities.event_listener import EventListener

driver = None
action = None
browser_type = "chrome"

@pytest.fixture(scope='class')
def init_web(request):
    if browser_type == "chrome":
        edriver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_type == "firefox":
        edriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver = EventFiringWebDriver(edriver, EventListener())


    globals()['driver'] = driver
    request.cls.driver = driver
    driver.maximize_window()

    yield
    driver.close()

@pytest.fixture(scope='class')
def init_desktop(request):
    pass
