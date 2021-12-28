from selenium.webdriver.common.by import By


class CreditCardMinimumPage:

    def __init__(self, driver):
        self.driver = driver

    def balance(self):
        return self.driver.find_element(By.XPATH, "//*[@id='balanceInput']")

    def rate(self):
        return self.driver.find_element(By.XPATH, "//*[@id='interestInput']")

    def min_percentage(self):
        return self.driver.find_element(By.XPATH, "//*[@text='interest + 1% of balance']")

    def min_percentage_choose(self):
        return self.driver.find_element(By.XPATH, "//*[@text='3.0%']")

    def calculate_button(self):
        return self.driver.find_element(By.XPATH, "//*[@text='CALCULATE']")

    def Navigate_home(self):
        return self.driver.find_element(By.XPATH, "//*[@contentDescription='Navigate up']")

    def test_app_one(self):
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Credit Card Minimum Payment']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='balanceInput']").send_keys('10')
        self.driver.find_element_by_xpath("xpath=//*[@id='interestInput']").send_keys('10')
        self.driver.find_element_by_xpath("xpath=//*[@text='interest + 1% of balance']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='3.0%']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='CALCULATE']").click()
        ExpextedMonths = self.driver.find_element_by_xpath("//*[@text='2']")
        ExTotalInsert = self.driver.find_element_by_xpath("//*[@text='0.08']")
        ExTotalPayment = self.driver.find_element_by_xpath("//*[@text='10.08']")
        assert ExpextedMonths.text == '2' and ExTotalInsert.text == '0.08' and ExTotalPayment.text == '10.08'
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']").click()
