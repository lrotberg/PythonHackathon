from selenium.webdriver.common.by import By


class ModalPage:
    def __init__(self, driver):
        self.driver = driver

    def get_started_heading(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h2.MuiTypography-h6")

    def next_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a>span.MuiButton-label")
