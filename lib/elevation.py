import json
import requests
import numpy

KEY ="AIzaSyAdoe3dfED8r5H6HPe51LGmvRZ78_BqxfM"
BASEURL = "https://maps.googleapis.com/maps/api/elevation/json"


def getheight(start, end, KEY, BASEURL):
    '''Function to return height between start and destination (given as coords)'''
    locations = [start, end]
        
    i=0
    for loc in locations:
        payload = {"locations":str(loc[0])+','+str(loc[1]), "key":KEY}
        r = requests.get(BASEURL, params=payload)
        data = json.loads(r.text)
        if i == 0:
            heightstart = data["results"][0]["elevation"]
            i = i + 1
        else:
            heightend = data["results"][0]["elevation"]
            heightdiff = abs(heightstart - heightend)
           
    return heightdiff
        
  

if __name__ == "__main__":
    start = [40,80]
    end = [40.05,80.05]
    print getheight(start, end, KEY, BASEURL)