import xml.etree.ElementTree as ET
tree = ET.parse('views\holder.xml')  # opens the file
root = tree.getroot()  # gets the root of the file
storage = "views\holder.xml"


class Holder:
    def check():
        print(root.tag, root.attrib, f"\nroot/parent has been found")

    def attribute():
        coin = root.get('coin')  # gets the value of the attribute
        print("Crypto name = {val}".format(val=coin))

    if __name__ == '__main__':
        check()
        attribute()


def apply():
    # Set method to add attribute
    root.set('launched', '932022')  # adds the attribute

    tree.write(storage)  # writes the file

    # apply()


class run:
    def run_id():
        id = 1
        for investor in tree.findall('investor'):
            investor.set('id', str(id))
            id += 1
            print(id, investor.get('name'))

            tree.write(storage)

    def run():
        for child in root:
            print(child.tag, child.attrib, child.text)
            print(len(child), f"child has been found\n")
            for subchild in child:
                print(subchild.tag, subchild.attrib, subchild.text)
                print(len(subchild), f"subchild has been found\n")
