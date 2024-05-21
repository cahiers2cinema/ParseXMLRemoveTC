import xml.etree.ElementTree as ET

tree = ET.parse("dummytestfile_copy.xml")
root = tree.getroot()

print(root.tag)
print(len(root))