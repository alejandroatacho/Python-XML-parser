import xml.etree.ElementTree as ET

# XML python variables
xml_file = 'views\main.xml'  # Path to the XML file
tree = ET.parse(xml_file)
root = tree.getroot()
# view the XML file to see the structure
print(root.tag, root.attrib)


def __init__():
    for child in root:
        print(child.tag, child.attrib)
        for subchild in child:
            print(subchild.tag, subchild.attrib)
            for subsubchild in subchild:
                print(subsubchild.tag, subsubchild.attrib)
                # if subsubchild in subchild == True:
                #     print(subsubchild.text, subsubchild.tag,
                #           subsubchild.attrib, subsubchild.tail)
                # else:
                #     print("It failed!!")


__init__()
