from selenium.webdriver.common.by import By


class TransactionPayPage:
    def __init__(self, driver):
        self.driver = driver

    def amount_input(self):
        return self.driver.find_element(By.ID, "amount")

    def note_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='description']")

    def request_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-test='transaction-create-submit-request']")

    def pay_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-test='transaction-create-submit-payment']")
