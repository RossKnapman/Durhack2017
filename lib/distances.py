import math # update to use numpy once we're sure server has it...
from bikeracks import latlongs

def find_nearest_bike_parking(point):
    '''compare all known racks to a given point, return dist to the nearest one'''
    distance = 6e8 # a long way
    for rack in latlongs:
        thisrack = haversine(point,rack)
        if thisrack < distance:
            distance = thisrack # its closest we've found
        
    return distance

def haversine(a,b):
    '''implements haversine formula, takes 2 latlong points and returns distance between'''
    radius = 6371e3 # radius of earth
    lata = math.radians(a[0])
    longa = math.radians(a[1])
    latb = math.radians(b[0])
    longb = math.radians(b[1])
    dlat = lata-latb
    dlong = longa-longb
    
    a = math.sin(dlat/2)**2 + math.cos(lata)*math.cos(latb) + math.sin(dlong/2)**2
    
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    
    distance = radius * c
    return distance