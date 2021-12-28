from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def multiply_button(self):
        return self.driver.find_element(By.XPATH, "//*[@text='×']")

    def number_9_button(self):
        return self.driver.find_element(By.XPATH, "//*[@text='9']")

    def equals_button(self):
        return self.driver.find_element(By.XPATH, "//*[@text='=']")

    def result_field(self):
        return self.driver.find_element(By.ID, "formula")
