from selenium.webdriver.common.by import By


class NotificationsPage:
    def __init__(self, driver):
        self.driver = driver

    def notifications_list(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "ul[data-test='notifications-list']>li")
