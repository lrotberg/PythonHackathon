from selenium.webdriver.common.by import By


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    def first_name_input(self):
        return self.driver.find_element(By.ID, "firstName")

    def last_name_input(self):
        return self.driver.find_element(By.ID, "lastName")

    def username_input(self):
        return self.driver.find_element(By.ID, "username")

    def password_input(self):
        return self.driver.find_element(By.ID, "password")

    def confirm_password_input(self):
        return self.driver.find_element(By.ID, "confirmPassword")

    def sign_up_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-test='signup-submit']")

    def sign_in_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/signin']")


