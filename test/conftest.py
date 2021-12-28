import mysql as mysql
import pytest

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utilities import common_ops
from utilities.event_listener import EventListener
my_db = None
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
def init_DB():
    mydb = mysql.connector.connect(
        host=common_ops.get_data("host"),
        database=common_ops.get_data("databaseDB"),
        user=common_ops.get_data("usernameDB"),
        password=common_ops.get_data("passwordDB")
    )
    return mydb


@pytest.fixture(scope='class')
def init_mobile(request):
    pass