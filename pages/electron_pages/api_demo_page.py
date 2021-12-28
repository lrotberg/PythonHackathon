from selenium.webdriver.common.by import By


class APIDemoPage:

    def __init__(self, driver):
        self.driver = driver

    def get_button_menus(self):
        return self.driver.find_element(By.ID, "button-menus")

    def get_verify_menus(self):
        return self.driver.find_element(By.XPATH, "//*[@id='menus-section']/header/div/h3/code[1]")

    def get_open_external_links(self):
        return self.driver.find_element(By.ID, "button-ex-links-file-manager")

    def get_verify_links_file(self):
        return self.driver.find_element(By.XPATH, "//*[@id='ex-links-file-manager-section']/header/div/h3/code")
