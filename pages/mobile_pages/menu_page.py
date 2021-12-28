from selenium.webdriver.common.by import By


class MenuPage:
    def __init__(self, driver):
        self.driver = driver

    def search_button(self):
        return self.driver.find_element_by_xpath("xpath=//*[@id='search']")

    def search_button(self):
        return self.driver.find_element_by_xpath("xpath=//*[@id='search']")







