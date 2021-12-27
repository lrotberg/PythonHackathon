import pytest

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utilities.event_listener import EventListener
from utilities.manage_web_pages import ManageWebPages

driver = None
action = None

sign_in_page = None
sign_up_page = None
menu_page = None
modal_page = None

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
    ManageWebPages.init_web_pages(driver)

    yield
    driver.quit()

@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    edriver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)

    driver = EventFiringWebDriver(edriver, EventListener())
    globals()['driver'] = driver
    request.cls.driver = driver

    yield
    driver.quit()
