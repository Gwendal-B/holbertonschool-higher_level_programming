#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    ET.indent(root, space="     ")

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=False)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for element in root:
        result[element.tag] = element.text

    return result
