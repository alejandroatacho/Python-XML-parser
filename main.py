import xml.etree.ElementTree as ET
import os

# Python variables for the XML file
xml_file = "main.xml"
xml_file_path = os.path.join(os.path.dirname(__file__), xml_file)
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Python variables to have fun with
family = ''
print(root.tag, root.attrib)

# Python code space
print("Python code space has initiated")
for child in root:
    print(child.tag, child.attrib, child.text)
    #print(child.attrib, child.text, child.tag)
'''

print(root.tag, root.attrib)


def __init__():
    for child in root:
        print(child.tag, child.attrib)
        for subchild in child:
            print(subchild.tag, subchild.attrib)
            for subsubchild in subchild:
                print(subsubchild.tag, subsubchild.attrib)
                if subsubchild in subchild == True:
                    print(subsubchild.text, subsubchild.tag,
                          subsubchild.attrib, subsubchild.tail)
                else:
                    print("It failed!!")


__init__()
'''

# # XML python variables
# tree = ET.parse('main.xml')
# root = tree.getroot()
# # view the XML file to see the structure
# print(root.tag, root.attrib)


# def __init__():
#     for child in root:
#         print(child.tag, child.attrib)
#         for subchild in child:
#             print(subchild.tag, subchild.attrib)
#             for subsubchild in subchild:
#                 print(subsubchild.tag, subsubchild.attrib)
#                 if subsubchild in subchild == True:
#                     print(subsubchild.text, subsubchild.tag,
#                           subsubchild.attrib, subsubchild.tail)
#                 else:
#                     print("It failed!!")


# __init__()
