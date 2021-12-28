from selenium.webdriver.common.by import By

class APIDemoPage:

    def __init__(self, driver):
        self.driver = driver

    def get_button_menus(self):
        return self.driver.find_element(By.ID, "button-menus")

    def get_verify_menus(self):
        return self.driver.find_element(By.XPATH, "//*[@id='menus-section']/header/div/h3/code[1]")

