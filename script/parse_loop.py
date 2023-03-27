import xml.etree.ElementTree as ET

# opens the file #storage.xml is original file
tree = ET.parse('views/hold_my_data.xml')
root = tree.getroot()  # gets the root of the file
storage = "views/hold_my_data.xml"  # storage.xml original

def find_my_cream():
    for x in root.findall('icecream'):
        flavor = x.find('flavor').text
        description = x.find('description').text
        price = x.find('price').text
        print(flavor, description, price)

def add_ice_cream(flavor, description, price):
    # Create a new icecream element
    new_icecream = ET.Element('icecream')

    # Create subelements for the new element
    new_flavor = ET.SubElement(new_icecream, 'flavor')
    new_flavor.text = flavor

    new_description = ET.SubElement(new_icecream, 'description')
    new_description.text = description

    new_price = ET.SubElement(new_icecream, 'price')
    new_price.text = price

    # Add the new element to the root of the tree
    root.append(new_icecream)

    # Write the modified XML tree to the original file
    tree.write(storage)

if __name__ == "__main__":
    # Call the function to add a new icecream element
    add_ice_cream('Vanilla', 'Classic vanilla ice cream', '3.50')

    # Call the function to print all the icecream elements
    find_my_cream()
