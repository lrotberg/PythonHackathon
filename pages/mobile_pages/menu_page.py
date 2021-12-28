from selenium.webdriver.common.by import By


class MenuPage:
    def __init__(self, driver):
        self.driver = driver

    def search_button(self):
        return self.driver.find_element(By.ID, "search")

    def search_input(self):
        return self.driver.find_element(By.ID, "search_src_text")

    def search_it(self):
        return self.driver.find_element(By.ID, "search_go_btn")

    def roi_appear(self):
        return self.driver.find_elements(By.XPATH, "//*[@text='ROI Calculator']")

    def navigate_back(self):
        return self.driver.find_element(By.XPATH,"//*[@contentDescription='Navigate up']")


    def calculator_app(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Calculator']")

    def credit_card_app(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Credit Card Minimum Payment']")
