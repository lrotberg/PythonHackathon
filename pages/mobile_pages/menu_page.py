from selenium.webdriver.common.by import By


class MenuPage:
    def __init__(self, driver):
        self.driver = driver

    def search_button(self):
        return self.driver.find_element(By.ID, "search")

    def search_input(self):
        return self.driver.find_element(By.ID, "search_src_text")

    def navigate_home(self):
        return self.driver.find_element(By.XPATH, "//*[@contentDescription='Navigate up']")

    def keyboard_by_object(self):
        return (By.XPATH, "//*[@class='android.view.View' and ./parent::*[@id='inputArea']]/*["
                          "@class='bkn$a'][43]")

    def color_strip(self):
        return self.driver.find_elements(By.ID, "colorStrip")

    def calculator_app(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Calculator']")

    def credit_card_app(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Credit Card Minimum Payment']")
