import unittest
import time
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from test.conftest import driver


class Test_me:
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setup_class(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '9888d341544d313650'
        self.dc['appPackage'] = 'com.financial.calculator'
        self.dc['appActivity'] = '.FinancialCalculators'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def test_search(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='search']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='search_src_text']").send_keys('roi')
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,'(//*[@class="android.view.View" and ./parent::*[@id="inputArea"]]/*[@class="bkn$a"])[43]')))
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.view.View' and ./parent::*[@id='inputArea']]/*[@class='bkn$a'])[43]").click()
        total_items=self.driver.find_elements(By.XPATH,"//*[@id='colorStrip']")
        print("Length is  : "+ str(len(total_items)))
        assert len(total_items)==2
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']").click()


    def test_app_one(self):
        self.driver.find_element_by_xpath( "text='Credit Card Minimum Payment']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='balanceInput']").send_keys('10')
        self.driver.find_element_by_xpath("xpath=//*[@id='interestInput']").send_keys('10')
        self.driver.find_element_by_xpath("xpath=//*[@text='interest + 1% of balance']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='3.0%']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='CALCULATE']").click()
        ExpextedMonths=self.driver.find_element_by_xpath("//*[@text='2']")
        ExTotalInsert=self.driver.find_element_by_xpath("//*[@text='0.08']")
        ExTotalPayment=self.driver.find_element_by_xpath("//*[@text='10.08']")
        assert ExpextedMonths.text=='2' and ExTotalInsert.text=='0.08' and ExTotalPayment.text=='10.08'
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']").click()



    def teardown_class(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
