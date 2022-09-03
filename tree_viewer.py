from asyncio.windows_events import NULL
from multiprocessing.connection import wait
from time import sleep
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
            for subsubchild in subchild:
                print(subsubchild.tag, subsubchild.attrib, subsubchild.text)
                print(len(subsubchild), f"subsubchild has been found\n")
                for subsubsubchild in subsubchild:
                    print(subsubsubchild.tag, subsubsubchild.attrib,
                          subsubsubchild.text)
                    print(len(subsubsubchild),
                          f"subsubsubchild has been found\n")
                    for subsubsubsubchild in subsubsubchild:
                        print(subsubsubsubchild.tag, subsubsubsubchild.attrib,
                              subsubsubsubchild.text)
                        print(len(subsubsubsubchild),
                              f"subsubsubsubchild has been found\n")
                        for subsubsubsubsubchild in subsubsubsubchild:
                            print(subsubsubsubsubchild.tag, subsubsubsubsubchild.attrib,
                                  subsubsubsubsubchild.text)
                            print(len(subsubsubsubsubchild),
                                  "subsubsubsubsubchild has been found\n")
        else:
            print(f"No more subchild has been found\n")
            return


# Run all the functions

if __name__ == '__main__':
    sleep(0.5)
    run()
    ET.dump(tree)
    input("Press any key to exit...")
    pass
    #  upgrade_run()

    # End of file
