from appium import webdriver
from selenium.webdriver.common.by import By


class Test_Desktop:

    def setup_class(self):
        global driver
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        desired_caps["platformName"] = "Windows"
        desired_caps["deviceName"] = "WindowsPC"
        driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
        driver.implicitly_wait(5)

    def test_01(self):
        expected_result = "6"
        driver.find_element(By.NAME,"One").click()
        driver.find_element(By.NAME,"Plus").click()
        driver.find_element(By.NAME,"Five").click()
        driver.find_element(By.NAME,"Equals").click()
        assert self.get_result() == expected_result

    def teardown_class(self):
        driver.quit()

    def get_result(self):
        return driver.find_element_by_xpath("//*[@AutomationId='CalculatorResults']").text.replace("Display is","").strip()