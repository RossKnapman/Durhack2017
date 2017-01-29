import osmread
import numpy as np
import itertools
import xml.etree.ElementTree as ET


def getNodeDist(startNode, endNode):
    
    """ Returns the as-the-crow-flies distance between two nodes """
    
    return np.sqrt((startNode.lat - endNode.lat)**2 + (startNode.lon - endNode.lon)**2)


def getNodes(latStart, longStart, latEnd, longEnd, mapData, tolerance):
    
    """ Take the input starting latitude and get a nearby associated node """
    
    it1, it2 = itertools.tee(mapData, 2)  # Allows you to iterate over the generator (mapData) several times
    
    entities1 = []
    for entity in it1:
        entities1.append(entity)
        
    entities2 = []
    for entity in it2:
        entities2.append(entity)
        
    print("Getting start node...")
    shortestDistance = 100
    for entity in entities1:
        if isinstance(entity, osmread.Node):
            distance = np.sqrt((latStart - entity.lat)**2 + (longStart - entity.lon)**2)
            if distance < shortestDistance:
                shortestDistance = distance
                startNode = entity
                    
    print("Getting end node...")
    shortestDistance = 100
    for entity in entities2:
        if isinstance(entity, osmread.Node):
            distance = np.sqrt((latEnd - entity.lat)**2 + (longEnd - entity.lon)**2)
            if distance < shortestDistance:
                shortestDistance = distance
                endNode = entity
    
    return startNode, endNode
    
    
def findNearestBusStop(inputNode):
    
    """ Returns the nearest bus stop to the input node """
    
    # This doesn't work yet
    
    busStops = []  # Empty list to store nodes representing bus stops   
    
    mapData = osmread.parse_file("trimmed.osm")    
    
    bus = 0
    for entity in mapData:
        if isinstance(entity, osmread.Node) and 'highway' in entity.tags:
            if entity.tags["highway"] == "bus_stop":
                busStops.append(entity)
                bus += 1
    print("Bus", bus)
        
    shortestDistance = 100
    for busStop in busStops:
        distance = getNodeDist(inputNode, busStop)
        if distance < shortestDistance:
            shortestDistance = distance
            closestBusStop = busStop
            
    return closestBusStop
    
    
if __name__ == "__main__":
    mapData = osmread.parse_file("trimmed.osm")
    startNode, endNode = getNodes(53.798395, -1.547876, 53.790613, -1.546279, mapData, 1e-5)
    print(findNearestBusStop(startNode))