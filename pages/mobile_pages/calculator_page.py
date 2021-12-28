from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def balance(self):
        return self.driver.find_element_by_xpath("xpath=//*[@id='search']")

    def rate(self):
        return self.driver.find_element_by_xpath("//*[@id='search_src_text']")

    def min_percentage(self):
        return self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']")


    def min_amount(self):
        return self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']")


    def calculate_button(self):
        return self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']")


    def test_app_two(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Calculator']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='9']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='×']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='9']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='=']").click()
        result1=self.driver.find_element_by_xpath("//*[@text='81']")
        assert result1.text=='81'
        time.sleep(3)
        self.driver.find_element_by_xpath("xpath=//*[@text='CLR']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='6']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='÷']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='6']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='=']").click()
        result2=self.driver.find_element_by_xpath("//*[@text='1']")
        assert result2.text=='1'
        self.driver.find_element_by_xpath("xpath=//*[@text='CLR']").click()

