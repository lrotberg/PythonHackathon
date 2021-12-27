from selenium.webdriver.common.by import By


class MenuPage:
    def __init__(self, driver):
        self.driver = driver

    def home_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul>div>a[href='/']")

    def account_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul>div>a[href='/user/settings']")

    def bank_accounts_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul>div>a[href='/bankaccounts']")

    def notifications_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul>div>a[href='/notifications']")

    def logout_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[data-test='sidenav-signout']")

    def balance_heading(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h6[data-test='sidenav-user-balance']")
