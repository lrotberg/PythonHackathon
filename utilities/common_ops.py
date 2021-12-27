import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse("./../ExternalData.xml").getroot()
    return root.find(".//" + node_name).text
