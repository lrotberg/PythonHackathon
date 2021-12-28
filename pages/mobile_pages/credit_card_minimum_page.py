from selenium.webdriver.common.by import By


class CreditCardMinimumPage:

    def __init__(self, driver):
        self.driver = driver

    def balance(self):
        return self.driver.find_element(By.ID, "balanceInput")

    def rate(self):
        return self.driver.find_element(By.ID, "interestInput")

    def min_percentage(self):
        return self.driver.find_element(By.XPATH, "//*[@text='interest + 1% of balance']")

    def min_percentage_choose(self):
        return self.driver.find_element(By.XPATH, "//*[@text='3.0%']")

    def calculate_button(self):
        return self.driver.find_element(By.XPATH, "//*[@text='CALCULATE']")

    def pay_off_months(self):
        return self.driver.find_element(By.ID, "payOffMonths")

    def interest_payment(self):
        return self.driver.find_element(By.ID, "InterestPayment")

    def total(self):
        return self.driver.find_element(By.ID, "total")
