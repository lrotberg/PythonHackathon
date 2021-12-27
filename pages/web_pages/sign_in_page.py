from selenium.webdriver.common.by import By


class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def username_input(self):
        return self.driver.find_element(By.ID , "username")

    def password_input(self):
        return self.driver.find_element(By.ID, "password")

    def remember_check(self):
        return self.driver.find_element(By.NAME, "remember")

    def sign_in_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-test='signin-submit']")

    def sign_up_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/signup']")

    def login(self, username, password):
        self.username_input().send_keys(username)
        self.password_input().send_keys(password)
        self.sign_in_button().click()

    def navigate_to_signup(self):
        self.sign_up_link().click()
