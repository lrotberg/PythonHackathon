from selenium.webdriver.common.by import By


class MenuPage:
    def __init__(self, driver):
        self.driver = driver

    def search_Box(self):
        return self.driver.find_element_by_xpath("xpath=//*[@id='search']")

    def search_button(self):
        return self.driver.find_element_by_xpath("//*[@id='search_src_text']")

    def Navigate_home(self):
        return self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']")

    def all_items(self):
        return self.driver.find_elements(By.XPATH,"//*[@id='colorStrip']")


    def search_function(self ,temp):
        self.search_Box().click()
        self.search_button().send_keys(temp)




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








