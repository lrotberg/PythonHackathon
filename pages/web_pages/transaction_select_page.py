from selenium.webdriver.common.by import By


class TransactionSelectPage:
    def __init__(self, driver):
        self.driver = driver

    def search_input(self):
        return self.driver.find_element(By.NAME, "q")

    def contacts_list(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "ul[data-test='users-list']>li")

    def contact(self, username):
        return self.driver.find_element(By.XPATH, "//span[text()='" + str(username) + "']/../..")

    def contact_by_index(self, index):
        return self.driver.find_element(
            By.XPATH, "//ul[@data-test='users-list']/li[" + str(index) + "]//span/span/span[1]")



