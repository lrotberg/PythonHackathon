from selenium.webdriver.common.by import By

class CalculatorPage:

    def __init__(self,driver):
        self.driver = driver

    def get_one(self):
        return self.driver.find_element(By.NAME,"One")

    def get_plus(self):
        return self.driver.find_element(By.NAME,"Plus")

    def get_five(self):
        return self.driver.find_element(By.NAME,"Five")

    def get_equals(self):
        return self.driver.find_element(By.NAME,"Equals")

    def get_result(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='CalculatorResults']")


