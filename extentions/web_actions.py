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


@allure.step("Get Calculation Result")
def get_result_calc(element: WE):
    return element.text.replace("Display is", "").strip()

@allure.step("Get text")
def get_text(element: WE):
    return element.text

