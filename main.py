import xml.etree.ElementTree as ET
import os

# Python variables for the XML file
xml_file = "main.xml"
xml_file_path = os.path.join(os.path.dirname(__file__), xml_file)
tree = ET.parse(xml_file_path)
root = tree.getroot()  # root is the root element of the XML file

# Python variables to have fun with
i = 0
print(root.tag, root.attrib, "root/parent has been found")

# Python code space
print(f"\nPython code space has initiated successfully!\n")
for child in root:
    print(child.tag, child.attrib, child.text)
    while root[i] == True:
        print("This is the" + root[i] + "child of the root element")
        i += 1
    else:
        print("all childrens are dead :C")
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
