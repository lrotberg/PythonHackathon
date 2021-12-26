from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()




#desktop
