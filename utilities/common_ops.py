import allure

from datetime import datetime
from xml.etree import ElementTree as ET

import test.conftest as conf

def get_data(self, node_name):
    root = ET.parse("./data.xml").getroot()
    return root.find(".//" + node_name).text

def attach_screenshot(self):
    now = datetime.now()
    image_name = "screen_" + now.strftime("%d-%b-%Y_%H%M%p")
    image = "./../screenshots/" + image_name + ".png"
    conf.driver.get_screenshot_as_file(image)
    allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
