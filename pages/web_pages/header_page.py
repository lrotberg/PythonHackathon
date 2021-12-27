from selenium.webdriver.common.by import By


class HeaderPage:
    def __init__(self, driver):
        self.driver = driver

    def new_transaction(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/transaction/new']")

    def tab_everyone(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[data-test='nav-public-tab']")

    def tab_friends(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[data-test='nav-contacts-tab']")

    def tab_mine(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[data-test='nav-personal-tab']")
