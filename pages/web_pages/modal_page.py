from selenium.webdriver.common.by import By


class ModalPage:
    def __init__(self, driver):
        self.driver = driver

    def get_started_heading(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h2.MuiTypography-h6")

    def next_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-test='user-onboarding-next']")

    def bank_name_input(self):
        return self.driver.find_element(By.NAME, "bankName")

    def routing_number(self):
        return self.driver.find_element(By.NAME, "routingNumber")

    def account_number(self):
        return self.driver.find_element(By.NAME, "accountNumber")

    def save_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-test='bankaccount-submit']")

    def done_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-test='user-onboarding-next']")
