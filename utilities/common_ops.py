from xml.etree import ElementTree as ET

def get_data(self, node_name):
    root = ET.parse("./data.xml").getroot()
    return root.find(".//" + node_name).text
