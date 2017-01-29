import xml.etree.ElementTree as ET


# Deletes all nodes not in a highway


data = ET.parse("mapCopy.xml")

root = data.getroot()

highwayNodes = []  # List to store node references in highways

for node in root.findall("node"):  # Keep bus stops in data
    for tag in node:
        if tag.attrib["v"] == "bus_stop":
            highwayNodes.append(node.attrib["id"])

for way in root.findall("way"):
    removeWay = True
    for tag in way:
        if tag.tag == "tag":
            if tag.attrib["k"] == "highway":
                removeWay = False
    if removeWay == True:
        root.remove(way)
        print("Way deleted")
    else:
        print("Way kept because it's a highway!")

                
for way in root.findall("way"):
    for potentialNode in way:
            if potentialNode.tag == "nd":
                highwayNodes.append(potentialNode.attrib["ref"])

                        
for node in root.findall("node"):
    if node.attrib["id"] not in highwayNodes:
        print("Removing node")
        root.remove(node)
    else:
        print("Keeping")
                
    
trimmed = data.write("trimmed.xml")
