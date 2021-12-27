import allure
from selenium.webdriver.remote.webelement import WebElement as WE

@allure.step("Click Element")
def click(element: WE):
    element.click()

@allure.step("Update Text")
def update_text(element: WE, text: str):
    element.send_keys(text)

@allure.step("Clear Text")
def clear_text(element: WE):
    element.clear()
