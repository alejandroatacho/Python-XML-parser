import xml.etree.ElementTree as ET

tree = ET.parse('main.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
