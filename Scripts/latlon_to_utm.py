# Determines the UTM Zone that a lat/lon point is located in
# Note that Zones are every 6 degrees
# Note that bands are every 12 degrees, except for X, which is 12 degrees

def latlong_to_utmzone(point):
    """Point x and y must be in degrees
    negative indicates W and S
    positive indicates E and N"""
    # Check that x and y are accepted
    if point.x < -180 or point.x > 180:
        print("Error: x out of range -180 to 180! Exiting...")
        pass
    if point.y < -80 or point.y > 84:
        print("Error: y out of range -80 to 84! Exiting...")
        pass

    # Determine Zone
    zones = [str(item).zfill(2) for item in range(1,61)]
    zone_index = int((point.x + 180)/6)     #always rounds down
    zone = zones[zone_index]

    # Determine Band
    try:
        bands = ["C","D","E","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X"]
        band_index = int((point.y + 80)/8)
        band = bands[band_index]
    except IndexError:
        band = "X"      #this band is 12 degrees instead of 8, and so could produce an index error

    return zone+band

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

mypoint = Point(-124,50)
myzone = latlong_to_utmzone(mypoint)

print(myzone)
