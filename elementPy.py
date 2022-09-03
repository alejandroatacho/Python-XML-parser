import xml.etree.ElementTree as ET

tree = ET.parse('views\sample.xml')  # opens the file
root = tree.getroot()  # gets the root of the file
storage = "views\sample.xml"

print(root.tag, root.attrib)

ET.dump(tree)


def check():
    for elm in root.findall("."):
        print(elm.tag, elm.attrib)


check()
