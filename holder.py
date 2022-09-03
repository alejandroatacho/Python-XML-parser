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


class run:
    def apply():
        # Set method to add attribute
        root.set('launched', '932022')  # adds the attribute

        tree.write(storage)  # writes the file

    # apply()
    def run_id():
        id = 1
        for investor in tree.findall('investor'):
            # sets the id attribute in the investor tag as a string
            investor.set('id', str(id))
            id += 1
            print(id, investor.get('name'))

            tree.write(storage)  # save in the xml file

    def run():
        for child in root:
            print(child.tag, child.attrib, child.text)
            print(len(child), f"child has been found\n")
            for subchild in child:
                print(subchild.tag, subchild.attrib, subchild.text)
                print(len(subchild), f"subchild has been found\n")

    def add_investor():
        i = 0
        for child in root:
            # print("im working")
            print(child.attrib, child.text, child.tag)

            if i == 0:
                print("start")
                i = len(child) + 1
                investor1 = ET.Element("investor")
                investor1.text = "investor"
                print(i)
                # investor1.set("{val}".format(val=str(i)))
                # investor1 = ET.fromstring(
                #     '<investor> name="Hinamizawa"</investor> id="{val}" />').format(val=i)  # creates the investor tag
                # adds the investor tag to the root
                root.append(investor1)
                tree.write(storage)  # save in the xml file
                print("Investor has been added")
            else:
                print("Investor has not been added")

            for subchild in child:
                print(subchild.attrib, subchild.text, subchild.tag)

            else:
                print("I broke there is no subchild")

    def add_id():
        for id, investor in enumerate(root.findall('investor')):
            investor.set('id', str(id))
        tree.write(storage)  # save in the xml file

    if __name__ == '__main__':
        # run_id()
        # run()
        # add_investor()
        add_id()
