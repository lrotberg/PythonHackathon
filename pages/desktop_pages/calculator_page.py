from selenium.webdriver.common.by import By

class CalculatorPage:

    def __init__(self,driver):
        self.driver = driver

    def get_one(self):
        return self.driver.find_element(By.NAME,"One").click()

    def get_plus(self):
        return self.driver.find_element(By.NAME,"Plus").click()

    def get_five(self):
        return self.driver.find_element(By.NAME,"Five").click()

    def get_equals(self):
        return self.driver.find_element(By.NAME,"Equals").click()

    def get_result(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='CalculatorResults']").\
            text.replace("Display is","").strip()


