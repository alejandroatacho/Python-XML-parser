import xml.etree.ElementTree as ET

tree = ET.parse('main.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.attrib)
        for subsubchild in subchild:
            print(subsubchild.tag, subsubchild.attrib)
            if subsubchild in subchild == True:
                print(subsubchild.text, subsubchild.tag,
                      subsubchild.attrib, subsubchild.tail)
