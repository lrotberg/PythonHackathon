class Test_Mobile:
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
        self.driver.find_element_by_xpath( "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Credit Card Minimum Payment']]").click()
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
