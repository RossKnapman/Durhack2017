import osmread
import numpy as np
import itertools



def getNodes(latStart, longStart, latEnd, longEnd, mapData, tolerance):
    
    """ Take the input starting latitude and get a nearby associated node """
    
    it1, it2 = itertools.tee(mapData, 2)  # Allows you to iterate over the generator (mapData) several times
    
#    entities1 = []
#    for entity in it1:
#        if isinstance(entity, osmread.Way) and "highway" in entity.tags:
#            for attribute in entity:
#                print(attribute)
#        entities1.append(entity)
        
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
    
    
if __name__ == "__main__":
    mapData = osmread.parse_file("map.osm")
    getNodes(53.798395, -1.547876, 53.790613, -1.546279, mapData, 1e-5)