import xml.etree.ElementTree as ET

tree = ET.parse('views\sample.xml')  # opens the file
root = tree.getroot()  # gets the root of the file
storage = "views\sample.xml"

print(root.tag, root.attrib)


def check():
    for elm in root.findall("."):
        print(elm.tag, elm.attrib)


def country():
    for elm in root.findall("country"):
        print(elm.tag, elm.attrib)


def specific_country():
    for elm in root.findall("country[@name='Panama']"):
       # print(elm.tag, elm.attrib)
        print(elm.attrib)


def rank():
    for elm in root.findall("country/rank"):
        print(elm.tag, elm.attrib)


def direction():
    for elm in root.findall("./country[@name='Panama']/neighbor[@direction='W']"):
        print(elm.tag, elm.attrib)


def value_change():
    for elm in root.findall("./country[@name='Liechtenstein']"):
        elm.set("name", "USA")
        tree.write(storage)


if __name__ == "__main__":
    check()
    # country()
    # direction()
    # value_change()
