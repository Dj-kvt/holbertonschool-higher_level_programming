import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Tout convertir en string pour éviter les erreurs

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}

    for child in root:
        data[child.tag] = child.text  # Toutes les valeurs sont des strings

    return data
