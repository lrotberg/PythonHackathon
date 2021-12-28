import pytest

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utilities.event_listener import EventListener
from utilities.manage_electron_page import ManageElectronPages
from utilities.manage_mobile_pages import ManageMobilePages
from utilities.manage_web_pages import ManageWebPages
from utilities.manage_desktop_pages import ManageDesktopPages

from utilities.common_ops import get_data

driver = None
action = None

sign_in_page = None
sign_up_page = None
menu_page = None
modal_page = None
header_page = None
transaction_select_page = None
transaction_pay_page = None
notifications_page = None

calc_page = None

demo_page = None

mobile_menu_page = None
mobile_calc_page = None
credit_card_min_page = None

@pytest.fixture(scope='class')
def init_web(request):
    if get_data("browser_type") == "chrome":
        edriver = webdriver.Chrome(ChromeDriverManager().install())
    elif get_data("browser_type") == "firefox":
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
    desired_caps["app"] = get_data("calcApp")
    desired_caps["platformName"] = get_data("platformName_desktop")
    desired_caps["deviceName"] = get_data("deviceName")

    edriver = webdriver.Remote(get_data("url_desktop"), desired_caps)
    driver = EventFiringWebDriver(edriver, EventListener())
    globals()['driver'] = driver
    request.cls.driver = driver
    ManageDesktopPages.init_desktop_pages(driver)

    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_electron(request):
    options = webdriver.ChromeOptions()
    options.binary_location = get_data("electron_app")
    edriver = webdriver.Chrome(chrome_options=options, executable_path=get_data("edriver"))
    driver = EventFiringWebDriver(edriver, EventListener())
    globals()['driver'] = driver
    request.cls.driver = driver
    ManageElectronPages.init_electron_pages(driver)

    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_mobile(request):
    desired_caps = {}
    desired_caps['reportDirectory'] = get_data("report_directory")
    desired_caps['reportFormat'] = get_data("report_format")
    desired_caps['testName'] = get_data("test_name")
    desired_caps['udid'] = get_data("udid")
    desired_caps['appPackage'] = get_data("app_package")
    desired_caps['appActivity'] = get_data("app_activity")
    desired_caps['platformName'] = get_data("platformName_mobile")

    edriver = webdriver.Remote(get_data("url_mobile"), desired_caps)
    driver = EventFiringWebDriver(edriver, EventListener())
    globals()['driver'] = driver
    request.cls.driver = driver
    ManageMobilePages.init_mobile_pages(driver)

    yield
    driver.quit()
