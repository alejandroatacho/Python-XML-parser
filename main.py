from asyncio.windows_events import NULL
import xml.etree.ElementTree as ET
import os

# Python variables for the XML file
xml_file = 'views\main.xml'  # Path to the XML file
xml_file_path = os.path.join(os.path.dirname(__file__), xml_file)
tree = ET.parse(xml_file_path)
root = tree.getroot()  # root is the root element of the XML file

# Python variables to have fun with
i = 0
storage = None

# Python code space


def run():

    print(root.tag, root.attrib, "root/parent has been found")
    print(f"\nPython code space has initiated successfully!\n")
    for child in root:
        print(child.tag, child.attrib, child.text)
        print(len(child), f"child has been found\n")
        for subchild in child:
            print(subchild.tag, subchild.attrib, subchild.text)
            print(len(subchild), f"subchild has been found\n")


def upgrade_run():
    count = 0
    for leaf in root:
        for subleaf in leaf:
            if subleaf[count] != len(subleaf):
                print(subleaf[count].text, subleaf[count].tag,
                      subleaf[count].attrib)
                count += 1


# Run all the functions
if __name__ == '__main__':
    run()
    #  upgrade_run()

# End of file
